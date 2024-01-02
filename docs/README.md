<p align="center">
<img src="./assets/web-heading.png" width="400"/>
</p>

# Go/Python API

A Go/Python API for building and training decision-making algorithms in realistic simulation environments.

## Installation notes

Get the python environment sorted

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Get `gopy` first using

```bash
go install golang.org/x/tools/cmd/goimports@latest
go install github.com/go-python/gopy@latest
```

Then run

```bash
gopy build -output=python -vm=python3 github.com/worldsoop/worldsoop/pkg/api
```

From this point you can import stuff like this

```bash
(venv) robert@robert-MacBookAir:~/Code/worldsoop$ python
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from python.api import StepperOrRunner
>>>
```

## To do

- Complete the `pkg.api` package methods for all use-cases and make it always import another package called `user_code` - this should be entirely written and useable with a single worldsoop config struct in Golang and calling only a minimal amount of code in the user's run script
- Complete the `Dockerfile` by adding in the installation and environment steps above
- Build the image `docker build -t worldsoop-compiler .`

Once the image has been built, in other repos:

- Run the container `docker run -v /path/to/user/go/files:/app/user-go-files worldsoop-compiler /app/user-go-files/main.go`
- Copy the api bindings `docker cp container_id:/app/output-directory /path/to/local/output-directory`
- Make these steps into a standard `./generate_python_api.sh` script and maintain a version of this script in this `worldsoop` repo
