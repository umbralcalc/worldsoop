package archetypes

import "github.com/umbralcalc/stochadex/pkg/simulator"

// StateNetworkNodeIteration
type StateNetworkNodeIteration struct {
}

func (s *StateNetworkNodeIteration) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
}

func (s *StateNetworkNodeIteration) Iterate(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	// params.IntParams["connected_node_partitions"]
	// this can be like the simple state transitions but the state of each
	// node is affected by the connected partitions
	return make([]float64, 0)
}
