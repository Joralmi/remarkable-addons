#!/bin/bash
ECHO Installing ReMarkable edition add-on software...
# Creating python3 venv
python3 -m venv .
# Activate venv
source bin/activate
# Installing app and external packages
pip install .
# Exit installation 
deactivate
