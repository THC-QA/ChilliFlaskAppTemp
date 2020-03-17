#!/bin/bash

source ~/.bashrc

python3 "/var/lib/jenkins/workspace/FlaskApp Example Pipeline/app.py"

gunicorn --workers=4 --bind=0.0.0.0:5001 app:app