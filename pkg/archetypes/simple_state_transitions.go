package archetypes

import "github.com/umbralcalc/stochadex/pkg/simulator"

type SimpleStateTransitionsIteration struct {
	simulator.Iteration
}

func (s *SimpleStateTransitionsIteration) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
}

func (s *SimpleStateTransitionsIteration) Iterate(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	return make([]float64, 0)
}
