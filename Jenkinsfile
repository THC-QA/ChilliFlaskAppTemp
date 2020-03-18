pipeline{
    agent any

    stages{
        stage("devEnv"){
            steps{
                sh 'echo "Dev-test pre-install and install."'
                sh 'chmod +x ./scripts/*'
                sh './scripts/before_installation.sh'
                sh './scripts/installation.sh'
                sh './scripts/make_service.sh'
            }
        }
        stage("urlTesting"){
            steps{
                sh 'python3 -m coverage run -m pytest tests/url_testing.py'
                sh 'python3 -m coverage report -m'
            }

        }
        stage("dbTesting"){
            steps{
                sh 'source /var/lib/jenkins/.bashrc'
                sh 'python3 -m coverage run -m pytest tests/db_testing.py'
                sh 'python3 -m coverage report -m'
            }
        }
    }
}