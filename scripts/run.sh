#!/bin/bash

source ~/.bashrc

python3 "/var/lib/jenkins/workspace/FlaskApp Example Pipeline/app.py"

/var/lib/jenkins/workspace/"FlaskApp Example Pipeline"/venv/bin/gunicorn --workers=4 --bind=0.0.0.0:5001 app:app