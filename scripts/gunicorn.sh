#!/bin/bash
"/var/lib/jenkins/workspace/FlaskApp Example Pipeline/venv/bin/gunicorn" --workers=6 --bind=0.0.0.0:5001 app:app