package archetypes

import "github.com/umbralcalc/stochadex/pkg/simulator"

type DistributedStateNetworkIteration struct {
	simulator.Iteration
}

func (d *DistributedStateNetworkIteration) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
}

func (d *DistributedStateNetworkIteration) Iterate(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	return make([]float64, 0)
}
