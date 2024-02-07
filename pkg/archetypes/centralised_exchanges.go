package archetypes

import "github.com/umbralcalc/stochadex/pkg/simulator"

// CentralisedExchangeIteration
type CentralisedExchangeIteration struct {
}

func (c *CentralisedExchangeIteration) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
}

func (c *CentralisedExchangeIteration) Iterate(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	return make([]float64, 0)
}
