#!/bin/sh

# Make sure you've pulled down the docker image before trying to run it:
# docker pull wpscanteam/wpscan

docker run -it --rm wpscanteam/wpscan "$@"