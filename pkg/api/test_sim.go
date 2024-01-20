package api

import (
	"fmt"
	"net/http"
	"os"
	"os/exec"
	"sync"

	"github.com/gorilla/websocket"
	"github.com/umbralcalc/stochadex/pkg/interactions"
	"github.com/umbralcalc/stochadex/pkg/phenomena"
	"github.com/umbralcalc/stochadex/pkg/simulator"
)

var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool { return true },
}

func startVizApp() (*os.Process, error) {
	cmd := exec.Command("serve", "-s", "build")
	cmd.Dir = "../viz/"
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	if err := cmd.Start(); err != nil {
		return nil, fmt.Errorf("failed to start dashboard app: %w", err)
	}

	return cmd.Process, nil
}

type StepperOrRunner interface {
	Run()
	Step(wg *sync.WaitGroup)
	ReadyToTerminate() bool
}

func LoadStepperOrRunner(
	settings *simulator.LoadSettingsConfig,
	implementations *simulator.LoadImplementationsConfig,
	agents []*interactions.AgentConfig,
) StepperOrRunner {
	if len(agents) == 0 {
		return simulator.NewPartitionCoordinator(
			simulator.NewStochadexConfig(
				settings,
				implementations,
			),
		)
	} else {
		return interactions.NewPartitionCoordinatorWithAgents(
			&interactions.LoadConfigWithAgents{
				Settings:        settings,
				Implementations: implementations,
				Agents:          agents,
			},
		)
	}
}

func RunSimulator() {
	settings := simulator.NewLoadSettingsConfigFromYaml("./cfg/config.yaml")
	iterations := []simulator.Iteration{&phenomena.WienerProcessIteration{}}
	for partitionIndex := range settings.StateWidths {
		iterations[partitionIndex].Configure(partitionIndex, settings)
	}
	implementations := &simulator.LoadImplementationsConfig{
		Iterations:           iterations,
		OutputCondition:      &simulator.EveryStepOutputCondition{},
		OutputFunction:       &simulator.StdoutOutputFunction{},
		TerminationCondition: &simulator.NumberOfStepsTerminationCondition{MaxNumberOfSteps: 100},
		TimestepFunction:     &simulator.ConstantTimestepFunction{Stepsize: 1.0},
	}
	agents := []*interactions.AgentConfig{}
	// agents := []*interactions.AgentConfig{
	// 	{
	// 		Actor:       &interactions.DoNothingActor{},
	// 		Generator:   &interactions.DoNothingActionGenerator{},
	// 		Observation: &interactions.GaussianNoiseStateObservation{},
	// 	},
	// }
	stepperOrRunner := LoadStepperOrRunner(settings, implementations, agents)
	stepperOrRunner.Run()
}
