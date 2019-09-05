# Docker

- Building the image: `docker build -t doodle-summer:v1 . `
- Running image: `docker run --rm doodle-summer:v1` vs `docker run doodle-summer:v1`
- List image: `docker images`
- List containers: `docker container ls -a`
- List running containers: `docker ps`
- Running with an attached session:  `docker run -it doodle-summer:v1`
- Running with custom entry: `docker run -it --entrypoint /bin/bash doodle-summer:v1`
- Possible to connect to running instances as well with docker exec. 

```dockerfile
FROM golang:1.11

# Installing dependencies
RUN apt install awesome-package
RUN export TERM=xterm-color
RUN go get github.com/pdevine/go-asciisprite

# Making sure files are available in the container
WORKDIR /project
COPY summer.go .

# Building
RUN go build -o summer summer.go                                 

# Exposing internals
EXPOSE 8080

# Where to start
ENTRYPOINT ["/summer"]     
```

- Exposing a port: `docker run doodle-summer:v1 -p 8090:8080`