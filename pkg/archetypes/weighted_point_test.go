package archetypes

import (
	"testing"

	"github.com/umbralcalc/stochadex/pkg/phenomena"
	"github.com/umbralcalc/stochadex/pkg/simulator"
)

func TestWeightedPointIteration(t *testing.T) {
	t.Run(
		"test that the weighted point iteration runs",
		func(t *testing.T) {
			settings :=
				simulator.LoadSettingsFromYaml("./weighted_point_config.yaml")
			iterations := [][]simulator.Iteration{
				{&WeightedPointIteration{}},
				{&phenomena.WienerProcessIteration{}},
				{&phenomena.WienerProcessIteration{}},
				{&phenomena.WienerProcessIteration{}},
				{&phenomena.WienerProcessIteration{}},
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
				TimestepFunction: &simulator.ConstantTimestepFunction{Stepsize: 1.0},
			}
			coordinator := simulator.NewPartitionCoordinator(
				settings,
				implementations,
			)
			coordinator.Run()
		},
	)
}
