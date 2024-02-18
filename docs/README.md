<p align="center">
<img src="./assets/web-heading.png" width="400"/>
</p>

# Go/Python API

A Go/Python API for building and training decision-making algorithms in realistic simulation environments.

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
