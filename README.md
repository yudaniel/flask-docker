# flask-docker
Example docker flask project to test fortanix

## Build the docker
```docker build -t <username>/docker-flask .```

## Push the docker image to dockerhub
```docker push <username>/docker-flask```

## Run the docker
```docker run <username>/docker-flask```

## To run the docker on the fortanix agent node
Install docker
```sudo apt install docker.io```

Run docker
```sudo docker run --device /dev/isgx:/dev/isgx --device /dev/gsgx:/dev/gsgx -v /var/run/aesmd/aesm.socket:/var/run/aesmd/aesm.socket -e NODE_AGENT_BASE_URL=http://<ip>:<port>/v1/ docker.io/<username>/docker-flask-fortanix```