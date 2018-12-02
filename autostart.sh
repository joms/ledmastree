#!/bin/sh
git pull
export FLASK_APP=/home/pi/code/ledmastree/backend/app.py
python3 -m flask run --host=0.0.0.0
