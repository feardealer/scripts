#!/bin/bash
screenshot=$(date '+%Y.%m.%d.%H.%M.%S').png
scrot -F $screenshot
cat $screenshot | xclip -selection clipboard -target image/png -i 
mv $screenshot ~/images/screenshots
