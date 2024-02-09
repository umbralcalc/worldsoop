package archetypes

import (
	"strconv"

	"github.com/umbralcalc/stochadex/pkg/simulator"
	"golang.org/x/exp/rand"
	"gonum.org/v1/gonum/stat/distuv"
)

// ConstantValuesIteration
type ConstantValuesIteration struct {
}

func (c *ConstantValuesIteration) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
}

func (c *ConstantValuesIteration) Iterate(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	return stateHistories[partitionIndex].Values.RawRowView(0)
}

// SimpleStateTransitionIteration
type SimpleStateTransitionIteration struct {
	unitUniformDist       *distuv.Uniform
	transitionRateIndices []int64
}

func (s *SimpleStateTransitionIteration) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
	seed := settings.Seeds[partitionIndex]
	rand.Seed(seed)

	s.unitUniformDist = &distuv.Uniform{
		Min: 0.0,
		Max: 1.0,
		Src: rand.NewSource(seed),
	}
	s.transitionRateIndices =
		settings.OtherParams[partitionIndex].IntParams["transition_rates_partition_indices"]
}

func (s *SimpleStateTransitionIteration) Iterate(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	state := make([]float64, 0)
	state = append(state, stateHistories[partitionIndex].Values.RawRowView(0)...)
	cumulative := timestepsHistory.NextIncrement
	cumulatives := make([]float64, 0)
	cumulatives = append(cumulatives, cumulative)
	transitionRates :=
		stateHistories[s.transitionRateIndices[int(state[0])]].Values.RawRowView(0)
	for _, rate := range transitionRates {
		cumulative += 1.0 / rate
		cumulatives = append(cumulatives, cumulative)
	}
	transitions :=
		params.IntParams["transitions_from_"+strconv.Itoa(int(state[0]))]
	event := s.unitUniformDist.Rand()
	if event*cumulative < cumulatives[0] {
		return state
	}
	for i, c := range cumulatives {
		if event*cumulative < c {
			state[0] = float64(transitions[i-1])
			return state
		}
	}
	state[0] = float64(transitions[len(transitions)-1])
	return state
}
