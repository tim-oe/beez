pipeline {
    agent {label 'beez'}
    stages {
        stage('Test') {
            steps {
                sh 'echo "running tests"'
                sh "pwd" dir('monitor')
                sh 'python3 setup.py cover'
            }
        }
    }
}