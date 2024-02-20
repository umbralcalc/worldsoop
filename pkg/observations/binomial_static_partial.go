package observations

import (
	"strconv"

	"github.com/umbralcalc/stochadex/pkg/simulator"
	"golang.org/x/exp/rand"
	"gonum.org/v1/gonum/stat/distuv"
)

type BinomialStaticPartialStateObservation struct {
	binomialDist               *distuv.Binomial
	stateObservationProbsIndex int
}

func (b *BinomialStaticPartialStateObservation) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
	b.binomialDist = &distuv.Binomial{
		N:   0,
		P:   1.0,
		Src: rand.NewSource(settings.Seeds[partitionIndex]),
	}
	b.stateObservationProbsIndex = int(settings.OtherParams[partitionIndex].
		IntParams["state_value_observation_probs_partition"][0])
}

func (b *BinomialStaticPartialStateObservation) Observe(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	outputValues := make([]float64, 0)
	for i, index := range params.IntParams["state_value_observation_indices"] {
		b.binomialDist.N = stateHistories[partitionIndex].Values.At(0, int(index))
		b.binomialDist.P = params.FloatParams["partition_"+
			strconv.Itoa(b.stateObservationProbsIndex)][i]
		outputValues = append(outputValues, b.binomialDist.Rand())
	}
	return outputValues
}
