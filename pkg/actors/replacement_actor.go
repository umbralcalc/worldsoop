package actors

import (
	"github.com/umbralcalc/stochadex/pkg/simulator"
)

type ReplacementActor struct {
}

func (r *ReplacementActor) Configure(partitionIndex int, settings *simulator.Settings) {
}

func (r *ReplacementActor) Act(state []float64, action []float64) []float64 {
	for i := range state {
		state[i] = action[i]
	}
	return state
}
