package archetypes

import (
	"testing"

	"github.com/umbralcalc/stochadex/pkg/simulator"
)

func TestMultiStagePipelineIteration(t *testing.T) {
	t.Run(
		"test that the multi-stage pipeline iteration runs",
		func(t *testing.T) {
			settings :=
				simulator.LoadSettingsFromYaml("./multi_stage_pipelines_config.yaml")
			iterations := []simulator.Iteration{
				&PipelineStageIteration{},
				&PipelineStageIteration{},
				&PipelineStageIteration{},
				&PipelineStageIteration{},
			}
			for index, iteration := range iterations {
				iteration.Configure(index, settings)
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
