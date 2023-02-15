# MyToDo-Flask

## Directions for installing and running the application
1. Open Terminal.
2. Visit the following link to get docker for your operating system
   https://docs.docker.com/get-docker/
3. Pull the docker image from docker hub using the following command.
```bash
$ docker pull shivam001/my-to-do
```
4. Run the docker container using the following command.
```bash
$ docker run -d -p 5000:5000 shivam001/my-to-do
```
5. Open the browser and hit `http://<host_ip>:5000`

## Stop the container
To stop the currently running container, use the following command:
```bash
$ docker stop <container-name>
```
