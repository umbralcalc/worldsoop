package archetypes

import "github.com/umbralcalc/stochadex/pkg/simulator"

// CentralNodeIteration
type CentralNodeIteration struct {
}

func (c *CentralNodeIteration) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
}

func (c *CentralNodeIteration) Iterate(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	return make([]float64, 0)
}

// SatelliteNodeIteration
type SatelliteNodeIteration struct {
}

func (s *SatelliteNodeIteration) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
}

func (s *SatelliteNodeIteration) Iterate(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	return make([]float64, 0)
}
