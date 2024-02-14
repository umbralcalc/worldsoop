package archetypes

import (
	"testing"

	"github.com/umbralcalc/stochadex/pkg/simulator"
)

func TestSimpleStateTransitionIteration(t *testing.T) {
	t.Run(
		"test that the simple state transition iteration runs",
		func(t *testing.T) {
			settings :=
				simulator.LoadSettingsFromYaml("./simple_state_transitions_config.yaml")
			iterations := [][]simulator.Iteration{
				{
					&simulator.ConstantValuesIteration{},
					&SimpleStateTransitionIteration{},
				},
			}
			index := 0
			for _, serialIterations := range iterations {
				for _, iteration := range serialIterations {
					iteration.Configure(index, settings)
					index += 1
				}
			}
			implementations := &simulator.Implementations{
				Iterations:      iterations,
				OutputCondition: &simulator.NilOutputCondition{},
				OutputFunction:  &simulator.NilOutputFunction{},
				TerminationCondition: &simulator.NumberOfStepsTerminationCondition{
					MaxNumberOfSteps: 100,
				},
				TimestepFunction: simulator.NewExponentialDistributionTimestepFunction(
					2.0, settings.Seeds[0],
				),
			}
			coordinator := simulator.NewPartitionCoordinator(
				settings,
				implementations,
			)
			coordinator.Run()
		},
	)
}
