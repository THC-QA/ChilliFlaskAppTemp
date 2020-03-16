pipeline{
    agent any

    stages{
        stage("devEnv"){
            steps{
                sh 'echo "Dev-test pre-install and install."'
                sh 'chmod +x ./scripts/*'
                sh './scripts/before_installation.sh'
                sh './scripts/installation.sh'
            }
        }
    }
}