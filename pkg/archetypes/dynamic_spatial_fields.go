package archetypes

import "github.com/umbralcalc/stochadex/pkg/simulator"

// SpatialFieldPointIteration
type SpatialFieldPointIteration struct {
}

func (s *SpatialFieldPointIteration) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
}

func (s *SpatialFieldPointIteration) Iterate(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	// params.IntParams["neighbour_partitions"]
	// params.FloatParams["neighbour_weightings"]
	return make([]float64, 0)
}
