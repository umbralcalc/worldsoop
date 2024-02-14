package archetypes

import (
	"github.com/umbralcalc/stochadex/pkg/simulator"
)

// NodeStateHistogramIteration
type NodeStateHistogramIteration struct {
}

func (n *NodeStateHistogramIteration) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
}

func (n *NodeStateHistogramIteration) Iterate(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	histogramValues := stateHistories[partitionIndex].Values.RawRowView(0)
	for _, index := range params.IntParams["connected_partitions"] {
		for _, valueIndex := range params.IntParams["connected_value_indices"] {
			histogramValues[int(stateHistories[index].Values.At(0, int(valueIndex)))] += 1
		}
	}
	return histogramValues
}
