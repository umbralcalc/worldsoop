<p align="center">
<img src="./assets/web-heading.png" width="400"/>
</p>

## Software to build more realistic environments for machine learning systems

Welcome to the **WorldsOOp Go/Python API**! This is an API for building and training decision-making algorithms in realistic simulation environments. The goals I'm aiming to achieve with this software are:
- To empower users in creating more realistic environments for machine learning systems to train on and test against.
- To create mini-games for human users to play with and learn about the real-world problems they represent.

## Core principles

_State observation should not be 'easy'._

These challenging environments have been designed to reflect the difficulties with handling more realistic datasets, as well as the partial state observability that is nearly always the case when working on problems in the real world.

_Realism can be gamified._

Access to real data for the systems that matter is often restricted. We want to circumvent this barrier to generalisation research into practical ML systems by generating it from environments instead. Nothing replaces a real dataset; but we can always try to emulate how messy it gets while still knowing the ground truth!

## Quickstart notes

1. Build the Go binary (needs [Go to be installed](https://go.dev/doc/install))

```bash
go mod tidy
go build -o bin/ ./cmd/worldsoop
```

2. Get the python environment sorted

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
export WORLDSOOP_PATH=/your/path/to/worldsoop
export PYTHONPATH=${PYTHONPATH}:${WORLDSOOP_PATH}
```

3. Run some examples...

```bash
python pyapi/examples/multiple_wiener_processes.py
```

## Want to learn more?

The core motivations for (and design ideas behind) this software originate from this open source book: [Worlds of Observation](https://umbralcalc.github.io/worlds-of-observation/).
