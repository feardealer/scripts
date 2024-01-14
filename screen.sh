#!/bin/bash

# Created for tiling WMs
# Deps: scrot, xclip
# Change SCREENSHOTS_DIR to ur value

SCREENSHOTS_DIR=~/images/screenshots

screenshot=$(date '+%Y.%m.%d.%H.%M.%S').png
scrot -F $screenshot
cat $screenshot | xclip -selection clipboard -target image/png -i 
mv $screenshot $SCREENSHOTS_DIR
