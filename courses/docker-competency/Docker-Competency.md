# Docker Competency

## Installation
[Windows](https://docs.docker.com/desktop/install/windows-install/)

## Section 1: Creating your first Dockerfile
**What is a Dockerfile?**

Basic Dockerfile commands:
| Command     | Description |
|-------------|-------------|
| **FROM**    | specifies a base image |
| **CMD**     | the default command executed by the resulting container image |

```
FROM <base image>
CMD [ "???", "???" ]
```

Once your Dockerfile is ready you can use it to build a container image

```
docker build -t helloworld .
```
> **QUESTION??:** what does the -t option do?

> **ASSIGNMENT:** Create a Dockerfile using the commands above to display "Hello World!" when the container is ran.
> In the snippet provided above supply the linux command that will echo "Hello World!" to the console


## Section 2: Running a python script
**What is a Dockerfile?**

Basic Dockerfile commands:
| Command     | Description |
|-------------|-------------|
| **FROM**    | specifies a base image |
| **RUN**     | specifies a command to be run to modify a given base image |
| **CMD**     | the default command executed by the resulting container image |

```
FROM <base image>
RUN <install needed package(s)>
COPY ./path/to/python/script /path/to/script
CMD [ "???", "???" ]
```

> **Assignment:** Create a Dockerfile using the commands above that executes the python script below.

```
# Simple Python Script to print current date and time
from datetime import datetime

def display_datetime():
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_time}")

if __name__ == "__main__":
    display_datetime()
```

## Section 3: Running a service in a container
In this exercise you will:
- create a simple python rest service
- bundle the rest service in a docker container
- run the resulting container image
- verify the service endpoints in a browser

Please see the corresponding [Section 3 exercise](./Section3-exercise/)
