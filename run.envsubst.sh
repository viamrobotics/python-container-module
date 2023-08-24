#!/usr/bin/env bash
# entrypoint for running container

SOCKET_DIR=`dirname $1`

exec podman run --volume ${DOLLAR}SOCKET_DIR:${DOLLAR}SOCKET_DIR $TAG python -m module $@
