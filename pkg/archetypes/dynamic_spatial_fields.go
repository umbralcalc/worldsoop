package archetypes

import "github.com/umbralcalc/stochadex/pkg/simulator"

// DynamicSpatialFieldIteration
type DynamicSpatialFieldIteration struct {
}

func (d *DynamicSpatialFieldIteration) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
}

func (d *DynamicSpatialFieldIteration) Iterate(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	return make([]float64, 0)
}
