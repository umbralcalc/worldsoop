package actors

import (
	"github.com/umbralcalc/stochadex/pkg/simulator"
)

type MultiplicativeActor struct {
}

func (m *MultiplicativeActor) Configure(partitionIndex int, settings *simulator.Settings) {
}

func (m *MultiplicativeActor) Act(state []float64, action []float64) []float64 {
	for i := range state {
		state[i] *= action[i]
	}
	return state
}
