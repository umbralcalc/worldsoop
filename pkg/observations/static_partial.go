package observations

import (
	"github.com/umbralcalc/stochadex/pkg/simulator"
)

type StaticPartialStateObservation struct {
}

func (p *StaticPartialStateObservation) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
}

func (p *StaticPartialStateObservation) Observe(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	outputValues := make([]float64, 0)
	for _, index := range params.IntParams["state_value_observation_indices"] {
		outputValues = append(
			outputValues,
			stateHistories[partitionIndex].Values.At(0, int(index)),
		)
	}
	return outputValues
}
