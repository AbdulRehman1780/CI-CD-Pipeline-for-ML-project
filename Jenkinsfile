pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "your-dockerhub-username/your-image-name:latest"
    }

    stages {
        stage('Checkout Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/AbdulRehman1780/CI-CD-Pipeline-for-ML-project.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'  // Ensure dependencies are installed
                    sh 'pytest tests/'  // Run unit tests
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                        sh 'docker push $DOCKER_IMAGE'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }

    post {
        success {
            emailext (
                subject: "Jenkins Deployment Successful",
                body: "The deployment of CI/CD Pipeline for ML Project was successful!\n\nJenkins Job URL: ${env.BUILD_URL}",
                to: "i211780@nu.edu.pk"
            )
        }

        failure {
            emailext (
                subject: "Jenkins Deployment Failed",
                body: "The deployment failed. Please check Jenkins logs.\n\nJenkins Job URL: ${env.BUILD_URL}",
                to: "i211780@nu.edu.pk"
            )
        }
    }
}
