# Section 3 exercise
In this exercise you will deploy a simple python rest service to a docker container and verify its accessibility from a browser.

## Fix the broken Dockerfile
Edit the [Dockerfile](./Dockerfile) to fix all the broken or missing instructions. Check you progress by building / rebuilding the container image and running it.

From the `Section3-exercise` directory run:
```
docker build -t simpleapi .
```
or
```
podman build -t simpleapi .
```

to build a container image and then run:

```
docker run -p 5000:5000 simpleapi
```
or
```
podman run -p 5000:5000 simpleapi
```
to run the service container locally. You should see output similar to the following:

```
podman run -p 5000:5000 simpleapi
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

## Verify the service
Open a browser window and test the two service endpoints:
- http://localhost:5000/
- http://localhost:5000/hello/<name>


## Additional thought
How might you map the service's container port to a differnt port on your host?
