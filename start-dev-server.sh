#!/bin/bash

# Start a development registry with authentication.
# This is intended for development or testing oras-py.
# You must generate an auth.htpasswd first.

if [ ! -f "auth.htpasswd" ]; then
    printf "You need to generate an auth.htpasswrd first.\n"
    printf "See https://oras.land/implementors/#using-docker-registry-with-authentication\n"
    exit
fi

docker run -it --rm -p 5000:5000 \
    -v $(pwd)/auth.htpasswd:/etc/docker/registry/auth.htpasswd \
    -e REGISTRY_AUTH="{htpasswd: {realm: localhost, path: /etc/docker/registry/auth.htpasswd}}" \
    registry
