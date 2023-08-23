MODULE_NAME ?= python-container-module
VERSION ?= 0.0.1
REPO ?= viam-labs/$(MODULE_NAME)
TAG = ghcr.io/$(REPO):$(VERSION)

build: Dockerfile module/*
	podman build -t $(TAG) .

push: build
	podman push $(TAG)

run.sh: run.envsubst.sh
	# render entrypoint script from template
	cat $< | TAG=$(TAG) envsubst > $@
	chmod +x $@

module.tar.gz: run.sh
	# bundle module
	tar czf $@ $^

.PHONY: build push
