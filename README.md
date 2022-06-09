# Basic commands

List active containers:
```
docker ps
```

List all containers:
```
docker ps --all
```

Create a container from a existing image without running it:
```
docker create hello-world
```

Start a container using container ID
```
docker start -a aac6236704800254081316dc004620dfaf87dd26dbb7dbc9c9a3b68ca022103c
```

Stop a container using container ID
```
docker stop aac6236704800254081316dc004620dfaf87dd26dbb7dbc9c9a3b68ca022103c
```

Run a container and append a command into it
```
docker run busybox echo hi there
```

Remove all unused containers, networks, images (both dangling and unreferenced), and optionally, volumes.
```
docker system prune
```

Show container logs using container's ID
```
docker logs 4427995665eb
```

Run the container and enter into it
```
docker exec -it 07b576c8e679 redis-cli
```

Run the container and enter specific program into it
```
docker exec -it 5db3a90586b7 sh
```

Build a custom Image from a Dockerfile
```
docker build .
```

Build a custom Image and named it
```
docker build -t image_name .
```

Run a named Image (just like regular image)

```
docker run image_name
```