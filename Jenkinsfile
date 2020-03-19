pipeline{
    agent any

    stages{
        stage("devEnv"){
            steps{
                sh 'echo "dev-test pre-install and install"'
                sh 'chmod +x ./scripts/*'
                sh './scripts/before_installation.sh'
                sh './scripts/installation.sh'
                sh './scripts/make_service.sh'
                sh './scripts/gunicorn.sh'
            }
        }
        stage("urlTesting"){
            steps{
                sh 'echo "test page availability and status"'
                sh 'python3 -m coverage run -m pytest tests/url_testing.py'
                sh 'python3 -m coverage report -m'
            }

        }
        stage("dbTesting"){
            steps{
                sh 'echo "test database structure and connection"'
                sh './scripts/db_test.sh'
            }
        }
    }
}