FROM golang:latest

# Install dependencies and set up your project's environment

WORKDIR /app
COPY . /app

CMD ["bash"]
