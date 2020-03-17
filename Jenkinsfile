pipeline{
    agent any

    stages{
        stage("devEnv"){
            steps{
                sh 'echo "Dev-test pre-install and install."'
                sh 'chmod +x ./scripts/*'
                sh './scripts/before_installation.sh'
                sh './scripts/make_service.sh'
            }
        }
        stage("urlTesting"){
            steps{
                sh coverage run -m pytest tests/url_testing.py
                sh coverage report -m
            }

        }
    }
}