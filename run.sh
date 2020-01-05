#!/bin/bash
ECHO Starting ReMarkable edition add-on software...
source bin/activate
remarkable_addons
rm new.svg new.png resized.jpg
rm temp/*
deactivate