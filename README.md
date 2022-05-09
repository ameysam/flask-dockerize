# Dockerized Flask app

Dockerize a simple flask app that get 'name' variable value from Redis and say "hello" to the fetched name.


# Run


## Docker Nnetworks

### Create a new network

```Bash
$ docker network create network_name
```

---

## Redis

### Pull Redis image

```Bash
$ docker pull redis:latest
```

### Run Redis image

For run redis image, you need to use the created network as network_name and need to persist redis data
in a location on your host (storage).
Like this:

```Bash
$ docker run --rm --name redis_optionaly_name -v /tmp/redis-data:/data --network network_name redis redis-server --appendonly yes
```

---


## App

## Build app

For build the app you can assign an optionaly tag to your image and run this command:

```Bash
$ docker build -t app_name:vx .
```

## Run built image

For run the built app, you need to use the created network and you can mount your local project path
to built app project path for editing code without need to rebuild app for any changes.

```Bash
$ docker run --rm --name app_name -p80:80 -v local_path:/app  --network network_name app_name:vx
```

After create container

```Bash
$ curl http://localhost:80
```