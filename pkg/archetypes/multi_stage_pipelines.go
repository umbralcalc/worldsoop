package archetypes

import (
	"github.com/umbralcalc/stochadex/pkg/simulator"
	"golang.org/x/exp/rand"
	"gonum.org/v1/gonum/stat/distuv"
)

// PipelineStageIteration
type PipelineStageIteration struct {
	unitUniformDist *distuv.Uniform
}

func (p *PipelineStageIteration) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
	seed := settings.Seeds[partitionIndex]
	rand.Seed(seed)

	p.unitUniformDist = &distuv.Uniform{
		Min: 0.0,
		Max: 1.0,
		Src: rand.NewSource(seed),
	}
}

func (p *PipelineStageIteration) Iterate(
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
	for _, rate := range params.FloatParams["downstream_partition_flow_rates"] {
		cumulative += 1.0 / rate
		cumulatives = append(cumulatives, cumulative)
	}
	event := p.unitUniformDist.Rand()
	if event*cumulative < cumulatives[0] {
		// minus number indicates nothing sent this step
		state[len(state)-1] = -1.0
		return state
	}
	objectCumulative := 0.0
	objects := make([]int, 0)
	objectCumulatives := make([]float64, 0)
	stateHistory := stateHistories[partitionIndex]
	for i := 0; i < stateHistory.StateWidth-2; i++ {
		prob := stateHistory.Values.At(0, i)
		if prob == 0 {
			continue
		}
		prob *= params.FloatParams["object_dispatch_probabilities"][i]
		objectCumulative += prob
		objects = append(objects, i)
		objectCumulatives = append(objectCumulatives, objectCumulative)
	}
	if len(objects) == 0 {
		return state
	}
	whichObject := objects[len(objects)-1]
	objectEvent := p.unitUniformDist.Rand()
	for i, c := range objectCumulatives {
		if objectEvent*objectCumulative < c {
			whichObject = objects[i]
			break
		}
	}
	state[whichObject] -= 1
	state[len(state)-2] = float64(whichObject)
	downstreams := params.IntParams["downstream_partitions"]
	for i, c := range cumulatives {
		if event*cumulative < c {
			state[len(state)-1] = float64(downstreams[i-1])
			return state
		}
	}
	state[len(state)-1] = float64(downstreams[len(downstreams)-1])
	return state
}
