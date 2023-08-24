# py-container-module

This is an example of using docker to bundle a python module as a container, and then running it on a robot using podman. (Podman is a lightweight docker alternative).

Use this as a reference for:
- Shipping hard-to-bundle python dependencies
- Other docker bundling

Note: unlike our other module examples, this one doesn't store the whole contents in Viam's registry. The uploaded module is a stub that downloads an image from ghcr, the github container registry (see [run.envsubst.sh](run.envsubst.sh)). There are pros and cons to this approach.

## Your container must be public

If you fork this and run into module startup errors, it may be because github packages made your container private.

In your forked repo:
- click your package (bottom right of homepage)
- go to 'package settings' (bottom right of package page)
- hit the 'change visibility' button and make it public

(Another way to solve this is to include credentials in your module, or log in to ghcr on your robot).

## Robot setup

The device you're deploying *to* needs to have podman or docker installed. On the raspberry pi (or any debian based system), you can run:

```sh
sudo apt-get install podman
```

## Robot config

Replace `module_id` and `model` with the values you choose for your module.

```json
{
  "modules": [
    {
      "type": "registry",
      "version": "latest",
      "name": "disk",
      "module_id": "viam:python-container-example"
    }
  ],
  "components": [
    {
      "depends_on": [],
      "name": "my-sensor",
      "type": "sensor",
      "attributes": {},
      "model": "viam:disk_sensor:linux"
    }
  ]
}
```

## Quick tour of this repo

- `module/`: python code for the viam module
- `Dockerfile`: the container. You can run `docker build -t whatever .` on your laptop to watch this work
- `Pipfile` and `Pipfile.lock`: dependency information. These are used in the Dockerfile to bundle dependencies
- `.github/workflows` CI logic to upload the module when you create a github release

## Bundling the container instead of using a registry

This example repo uses ghcr.io as a package registry. An alternative is to use docker / podman `save` and `load` commands to bundle the container image with the module and restore it on the target machine.
