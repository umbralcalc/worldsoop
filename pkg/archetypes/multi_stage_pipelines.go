package archetypes

import "github.com/umbralcalc/stochadex/pkg/simulator"

type MultiStagePipelineIteration struct {
	simulator.Iteration
}

func (m *MultiStagePipelineIteration) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
}

func (m *MultiStagePipelineIteration) Iterate(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	return make([]float64, 0)
}
