package iterations

import (
	"github.com/umbralcalc/stochadex/pkg/simulator"
)

// HistogramNodeIteration
type HistogramNodeIteration struct {
}

func (h *HistogramNodeIteration) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
}

func (h *HistogramNodeIteration) Iterate(
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
