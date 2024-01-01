<p align="center">
<img src="./assets/web-heading.png" width="400"/>
</p>

# Python API

A python API for building and training decision-making algorithms in realistic simulation environments

## Installation notes

Get the python environment sorted

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Get `gopy` first using

```bash
cd pkg
go install golang.org/x/tools/cmd/goimports@latest
go install github.com/go-python/gopy@latest
cd ..
```

Then run

```bash
cd pkg
gopy build -output=python -vm=python3 github.com/worldsoop/worldsoop/pkg/test_sim
cd ..
```

From this point you can import stuff like this

```bash
(venv) robert@robert-MacBookAir:~/Code/worldsoop$ python
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pkg.python.test_sim import StepperOrRunner
>>>
```
