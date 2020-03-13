pipeline{
    agent any

    stages{
        stage("pre-run"){
            steps{
                sh 'echo "Dev-test pre-install and install."'
                sh 'git pull'
                sh 'git status'
                sh 'chmod +x ./scripts/*'
                // sh './scripts/before_installation.sh'
                // sh './scripts/installation.sh'
            }
        }
    }
}