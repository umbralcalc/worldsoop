package observations

import (
	"strconv"

	"github.com/umbralcalc/stochadex/pkg/simulator"
	"golang.org/x/exp/rand"
	"gonum.org/v1/gonum/stat/distuv"
)

type BinomialStaticPartialStateObservationIteration struct {
	binomialDist               *distuv.Binomial
	partitionToObserve         int
	stateObservationProbsIndex int
}

func (b *BinomialStaticPartialStateObservationIteration) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
	b.binomialDist = &distuv.Binomial{
		N:   0,
		P:   1.0,
		Src: rand.NewSource(settings.Seeds[partitionIndex]),
	}
	b.partitionToObserve = int(settings.OtherParams[partitionIndex].
		IntParams["partition_to_observe"][0])
	b.stateObservationProbsIndex = int(settings.OtherParams[partitionIndex].
		IntParams["state_value_observation_probs_partition"][0])
}

func (b *BinomialStaticPartialStateObservationIteration) Iterate(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	outputValues := make([]float64, 0)
	stateValues := params.FloatParams["partition_"+strconv.Itoa(b.partitionToObserve)]
	probs := params.FloatParams["partition_"+strconv.Itoa(b.stateObservationProbsIndex)]
	for i, index := range params.IntParams["state_value_observation_indices"] {
		b.binomialDist.N = stateValues[index]
		b.binomialDist.P = probs[i]
		outputValues = append(outputValues, b.binomialDist.Rand())
	}
	return outputValues
}
