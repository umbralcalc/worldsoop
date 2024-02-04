<p align="center">
<img src="./assets/web-heading.png" width="400"/>
</p>

# Go/Python API

A Go/Python API for building and training decision-making algorithms in realistic simulation environments.

## Quickstart notes

1. Get the python environment sorted

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
export PYTHONPATH={$PYTHONPATH}:.
export WORLDSOOP_PATH=your/path/to/worldsoop
```

2. Build the Go binary

```bash
go mod tidy
go build -o bin/ ./cmd/worldsoop
```

3. Run some examples...

```bash
python pyapi/examples/multiple_wiener_processes.py
```
