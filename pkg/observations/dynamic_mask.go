package observations

import (
	"github.com/umbralcalc/stochadex/pkg/simulator"
)

type DynamicMaskStateObservation struct {
	maskIndex int
}

func (d *DynamicMaskStateObservation) Configure(
	partitionIndex int,
	settings *simulator.Settings,
) {
	d.maskIndex = int(settings.OtherParams[partitionIndex].
		IntParams["trigger_observation_partition"][0])
}

func (d *DynamicMaskStateObservation) Observe(
	params *simulator.OtherParams,
	partitionIndex int,
	stateHistories []*simulator.StateHistory,
	timestepsHistory *simulator.CumulativeTimestepsHistory,
) []float64 {
	outputValues := make([]float64, 0)
	maskValues := stateHistories[d.maskIndex]
	for i := 0; i < maskValues.StateWidth; i++ {
		if maskValues.Values.At(0, i) == 0 {
			continue
		}
		outputValues = append(
			outputValues,
			stateHistories[partitionIndex].Values.At(0, i),
		)
	}
	return outputValues
}
