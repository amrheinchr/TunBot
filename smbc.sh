#!/bin/bash

curl -s -N http://smbc-comics.com | grep -m 3 "<img" | tail -n1 | awk 'BEGIN {FS = "\""} ; {print $6}' | xargs wget -O smbc.png
