#!/bin/bash

# Created for tiling WMs
# Deps: scrot, xclip
# Change SCREENSHOTS_DIR to ur value


# full screen ./screen.sh
# selected area ./screen.sh -s

SCREENSHOTS_DIR=$HOME/Pictures/Screenshots

screenshot=$(date '+%Y.%m.%d.%H.%M.%S').png

if [ "$1" == "-s" ]; then
	scrot -s $screenshot
else
	scrot -F $screenshot
fi

cat $screenshot | xclip -selection clipboard -target image/png -i 
mv $screenshot $SCREENSHOTS_DIR
