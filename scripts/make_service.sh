sudo cp /var/lib/jenkins/workspace/FlaskApp Example Pipeline/service/ChilliApp.service /etc/systemd/systemd
sudo systemctl daemon-reload
sudo systemctl enable ChilliApp.service
sudo systemctl start ChilliApp.service