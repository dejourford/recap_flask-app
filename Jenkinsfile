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
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'docker login -u $USERNAME -p $PASSWORD'
                    sh 'docker tag flask-app dejourford/flask-app:latest'
                    sh 'docker push dejourford/flask-app:latest'
                }
            }
        }

        stage('Deploy') {
    steps {
        sh 'kubectl apply -f flask-deployment.yaml --validate=false'
    }
}
    }
}
