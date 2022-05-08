# Jupyter - Math Notebooks

## About
Here is a docker image built on the work of the Jupyter team to provide the ability to do work with symbolic mathematics programmatically.

I have built on top of the [jupyter/scipy-notebook](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-scipy-notebook).

The most notable packages included (both by the original and by me) are:

- [sympy](https://github.com/sympy/sympy)
- [handcalcs](https://github.com/connorferster/handcalcs)

## Usage

### Dependencies
Make sure that you have Docker installed. If you need information:

- [Docker Overview](https://docs.docker.com/get-started/overview/)

### Run Notebook Container

Both of the options below run a container based on the image jllovet/math-notebook (defined here), with a web server hosting the jupyter notebook on port 3000 and a volume mounted between the current directory on the host 

```SHELL
docker run -it -p 3000:3000 -v "${PWD}/work":/home/jovyan/work jllovet/math-notebook
```

Alternatively, you use Docker Compose to make using this image easier. It provides a wrapper for creating more elaborate Docker environments, for instance, that use multiple services, require inter-container networks, volumes, and other features. There is no requirement to use Docker Compose to use the Docker image defined here, but it will make your experience smoother if you want to include any additional services in the environment.

- [Docker Compose](https://docs.docker.com/compose/)

If you have Docker Compose installed, from a directory containing `docker-compose.yml`:

```SHELL
docker-compose up --build
```

