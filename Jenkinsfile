pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: '6ce3eea9-0605-4ef7-bcde-71d036e6f342', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'docker login -u $USERNAME -p $PASSWORD'
                    sh 'docker tag flask-app dejourford/flask-app:latest'
                    sh 'docker push dejourford/flask-app:latest'
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'kubectl apply -f flask-deployment.yml'
            }
        }
    }
}
