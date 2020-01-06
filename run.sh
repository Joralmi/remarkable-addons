#!/bin/bash
ECHO Starting ReMarkable edition add-on software...
source bin/activate
remarkable_addons
rm temp/new.svg temp/new.png temp/resized.jpg
rm temp/*.pdf
deactivate