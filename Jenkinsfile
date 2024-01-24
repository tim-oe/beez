pipeline {
    /* use pi beez node for builds */
    agent {label 'beez'}
    stages {
        stage('Test') {
            steps {
                sh 'echo "running tests"'
                dir("monitor") {
                    sh 'pwd'
                    sh 'python3 ./setup.py cover'
                    sh 'python3 ./setup.py sonar'
                }
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}