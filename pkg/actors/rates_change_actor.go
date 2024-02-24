package actors

import "github.com/umbralcalc/stochadex/pkg/interactions"

type PartitionRatesChangeActor struct {
	interactions.Actor
}

// Types of actor:
// - sports team manager & other game player
//   - substitute players
//   - changes to tactics

// - public health authority & wildlife/national park control authority & livestock/crop farmer
//   - spatially detect disease or damage
//   - change state of a subset of the population

// - brain doctor & traffic light controller & city infrastructure maintainer
//   - change the state of a subset of nodes in the network

// - supply/relief chain controller & hospital logistics manager & data pipeline controller
//   - modify the relative flows between different pipeline stages

// - financial/betting/other market trader & market exchange mediator
//   - interact with the market using an agent or collection of agents
