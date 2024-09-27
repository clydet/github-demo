# Section 4 exercise
In this exercise you will create a DockerHub account and push an image using your account information.

## Create an account on DockerHub
Navigate to https://hub.docker.com/ and "Sign up"

## Build a container image
You can use one of the container images from a prior lesson

## Tag and push your image to dockerhub
```
docker login docker.io --username ${DH_USER} --password ${DH_PASS}
docker build -t hello .

docker tag hello docker.io/iamclyde/hello:v1.0.0

docker push docker.io/iamclyde/hello:v1.0.0
```

> **Questions:**    
> Can you associate multiple tags with the same container image?   
> Can you delete a container image from your account on dockerhub?   
> Can you use your published image on dockerhub as a base image for a new Dockerfile?

