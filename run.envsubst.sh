#!/usr/bin/env bash
# entrypoint for running container

exec podman run $TAG $@
