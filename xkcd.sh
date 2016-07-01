#!/bin/bash

curl http://xkcd.com/ | grep "Image URL (for hotlinking/embedding):" | awk '{print $(NF)}' | xargs wget -O tmp.png
