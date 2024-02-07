package archetypes

import (
	"github.com/umbralcalc/stochadex/pkg/simulator"
	"golang.org/x/exp/rand"
	"gonum.org/v1/gonum/stat/distuv"
)

// MultiStagePipelineIteration
type MultiStagePipelineIteration struct {
	unitUniformDist *distuv.Uniform
}

func (m *MultiStagePipelineIteration) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
	seed := settings.Seeds[partitionIndex]
	rand.Seed(seed)

	m.unitUniformDist = &distuv.Uniform{
		Min: 0.0,
		Max: 1.0,
		Src: rand.NewSource(seed),
	}
}

func (m *MultiStagePipelineIteration) Iterate(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	state := make([]float64, 0)
	state = append(state, stateHistories[partitionIndex].Values.RawRowView(0)...)
	for _, index := range params.IntParams["upstream_partitions"] {
		stateHistory := stateHistories[int(index)]
		if int(stateHistory.Values.At(0, stateHistory.StateWidth-1)) ==
			partitionIndex {
			state[int(stateHistory.Values.At(0, stateHistory.StateWidth-2))] += 1
		}
	}
	cumulative := timestepsHistory.NextIncrement
	cumulatives := make([]float64, 0)
	cumulatives = append(cumulatives, cumulative)
	downstreams := params.IntParams["downstream_partitions"]
	for _, index := range downstreams {
		rate := params.FloatParams["downstream_partition_flow_rates"][index]
		cumulative += 1.0 / rate
		cumulatives = append(cumulatives, cumulative)
	}
	event := m.unitUniformDist.Rand()
	if event*cumulative < cumulatives[0] {
		// minus number indicates nothing sent this step
		state[len(state)-1] = -1.0
		return state
	}

	// Now that the event is happening you still need to randomly find one of
	// the objects to send according to probabilities and whether or not they
	// exist in this stage

	for i, c := range cumulatives {
		if event*cumulative < c {
			state[len(state)-1] = float64(downstreams[i-1])
			return state
		}
	}
	state[len(state)-1] = float64(downstreams[len(downstreams)-1])
	return state
}
