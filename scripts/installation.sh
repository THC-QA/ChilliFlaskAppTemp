#!/bin/bash

source venv/bin/activate

sudo python3 -m pip install flask

sudo python3 -m pip install flask_mysqldb

sudo python3 -m pip install Flask-WTF

source ~/.bashrc

sudo python3 app.py