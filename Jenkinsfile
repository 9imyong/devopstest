pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'python:3.11-slim'
                }
            }
            steps {
                sh 'pip install -r app/requirements.txt pytest'
                sh 'pytest -q'
            }
        }

        stage('Build & Push') {
            steps {
                sh 'docker build -t $REGISTRY/devops-starter:latest .'
                sh 'echo $REGISTRY_PASSWORD | docker login $REGISTRY -u $REGISTRY_USER --password-stdin'
                sh 'docker push $REGISTRY/devops-starter:latest'
            }
        }

        stage('Deploy (kubectl)') {
            when {
                expression { return params.DEPLOY == true }
            }
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }

    parameters {
        booleanParam(name: 'DEPLOY', defaultValue: false)
    }
}
