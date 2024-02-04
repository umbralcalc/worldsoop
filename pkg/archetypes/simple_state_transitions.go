package archetypes

import "github.com/umbralcalc/stochadex/pkg/simulator"

type DiscreteStates []string
type ContinuousState string

type SimpleStateTransitionIteration struct {
	indices map[string]int
	types   map[string]interface{}
}

func (s *SimpleStateTransitionIteration) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
}

func (s *SimpleStateTransitionIteration) Iterate(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	return make([]float64, 0)
}
