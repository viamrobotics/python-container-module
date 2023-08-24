# py-container-module

> [!NOTE]
> Work in progress -- not officially released yet

This is an example of using Docker to bundle a Python module as a container, and then running it on a robot using Podman. (Podman is a lightweight Docker alternative).

## Packages must be public

The `podman run` step will fail if your ghcr package is not public. Look in 'package settings' (bottom right) for your package.

## Target system setup

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

## Bundling the container instead of using a registry

This example repo uses ghcr.io as a package registry. An alternative is to use docker / podman `save` and `load` commands to bundle the container image with the module and restore it on the target machine.
