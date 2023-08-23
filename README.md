# py-container-module

This is an example of using Podman to bundle a python module as a container.

(Podman is a lightweight docker alternative).

## System setup

The device you're deploying *to* needs to have podman installed. On the raspberry pi (or any debian based system), you can run:

```sh
sudo apt-get install podman
```

## Using docker instead of podman

The save, load and run commands should be approximately the same. Post an issue if you run into trouble.

## Using a registry instead of bundling the 

If you have a preferred container registry (for example ghcr.io on github), you can use the registry instead of bundling the entire module.

Post an issue to this repo if you want instructions for this.
