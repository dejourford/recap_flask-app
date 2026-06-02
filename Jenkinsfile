pipeline {
    agent any
    
    environment {
        IMAGE_TAG = "dejourford/flask-app:${BUILD_NUMBER}"
    }

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build') {
            steps {
                sh "docker build -t ${IMAGE_TAG} ."
            }
        }

        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'docker login -u $USERNAME -p $PASSWORD'
                    sh "docker push ${IMAGE_TAG}"
                }
            }
        }

        stage('Deploy') {
            steps {
                sh "kubectl set image deployment/flask-deployment flask=${IMAGE_TAG}"
            }
        }
    }
}
