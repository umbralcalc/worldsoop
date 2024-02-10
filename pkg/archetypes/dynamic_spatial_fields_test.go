package archetypes

import (
	"testing"

	"github.com/umbralcalc/stochadex/pkg/phenomena"
	"github.com/umbralcalc/stochadex/pkg/simulator"
)

func TestDynamicSpatialFieldIteration(t *testing.T) {
	t.Run(
		"test that the dynamic spatial field iteration runs",
		func(t *testing.T) {
			settings :=
				simulator.LoadSettingsFromYaml("./dynamic_spatial_fields_config.yaml")
			iterations := []simulator.Iteration{
				&SpatialFieldPointIteration{},
				&phenomena.WienerProcessIteration{},
				&phenomena.WienerProcessIteration{},
				&phenomena.WienerProcessIteration{},
				&phenomena.WienerProcessIteration{},
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
