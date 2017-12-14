#!/bin/sh
git clone
cd /home/pi/ledmastree/frontend
npm install && npm build
export export FLASK_APP=/home/pi/ledmastree/backend/app.py
python3 -m flask run --host=0.0.0.0
