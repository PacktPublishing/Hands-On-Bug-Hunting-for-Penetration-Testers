#!/bin/sh

retire --path $1 --outputformat json --outputpath $2; python -m json.tool $2