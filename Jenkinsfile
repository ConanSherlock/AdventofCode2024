env.BUILD_MACHINE = "agent-1"
env.WORK_SPACE = "C:/Jenkins/workspace/AdventofCode2024"
env.SUCCESS = 0
env.BUILD_ERROR_STRING = "Error in build step"
env.TEST_ERROR_STRING = "Error in running tests"
env.DEPLOY_ERROR_STRING = "Error in deployment"

def BRANCH_NAME = "${env.JOB_NAME.substring(env.JOB_NAME.lastIndexOf('/') + 1, env.JOB_NAME.length())}"

pipeline {
    agent {
        node {
            label env.BUILD_MACHINE
            customWorkspace env.WORK_SPACE
        }
    }

    stages {
        stage('Set up Environment') {
            steps {
                script {
                    jenkins_functions = load "jenkins_functions.groovy"
                }
                sh 'python -m venv /venv'
                sh 'source /venv/Scripts/activate && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing..'
                script {
                    def result = jenkins_functions.runVenvUnix("pytest")
                    if(result != env.SUCCESS) {
                        currentBuild.result = 'FAIL'
                        result = "FAIL"
                        error(env.TEST_ERROR_STRING)
                    }
                }
            }
        }
    }
    post
    {
        failure
        {
            mail bcc: '',
                  cc: '',
                  charset: 'UTF-8',
                  mimeType: 'text/html',
                  replyTo: '',
                  subject: "Advent of Code 2024 Jenkins FAILURE: -> ${env.JOB_NAME}",
                  to: "${env.DEFAULT_MAIL_RECIPIENTS}",
                  from: "Jenkins",
                  body: "<b>Jenkins Pipeline has failed</b><br>\n\n<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br>Build URL: ${env.BUILD_URL}<br>";
        }

        success
        {
            mail bcc: '',
                  cc: '',
                  charset: 'UTF-8',
                  mimeType: 'text/html',
                  replyTo: '',
                  subject: "Advent of Code 2024 Jenkins SUCCESS: -> ${env.JOB_NAME}",
                  to: "${env.DEFAULT_MAIL_RECIPIENTS}",
                  from: "Jenkins",
                  body: "<b>Jenkins Pipeline has succeeded</b><br>\n\n<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br>Build URL: ${env.BUILD_URL}<br>";
        }
    }
}
