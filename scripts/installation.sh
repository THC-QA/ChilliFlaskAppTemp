#!/bin/bash

source venv/bin/activate

pip3 install flask -y

pip3 install flask_mysqldb -y

pip3 install Flask-WTF -y

source ~/.bashrc

python3 app.py