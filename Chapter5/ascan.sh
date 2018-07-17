#!/bin/sh

arachni $1 \
    --checks=*,-emails* \
    --scope-include-subdomains \
    --timeout 0:05:00 \
    --http-request-concurrency 10