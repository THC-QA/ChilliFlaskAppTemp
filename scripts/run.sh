#!/bin/bash

source ~/.bashrc

# python3 "/var/lib/jenkins/workspace/FlaskApp Example Pipeline/app.py"

"/var/lib/jenkins/workspace/FlaskApp Example Pipeline/venv/bin/gunicorn" --workers=6 --bind=0.0.0.0:5000 app:app

# Production will use a gunicorn swarm, testing can continue to use app.py in debug mode