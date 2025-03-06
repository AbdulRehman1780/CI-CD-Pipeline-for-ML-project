pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "your-dockerhub-username/your-image-name:latest"
    }

    stages {
        stage('Checkout Repository') {
            steps {
                checkout scmGit(
                    branches: [[name: '*/main']],  
                    extensions: [], 
                    userRemoteConfigs: [[
                        url: 'https://github.com/AbdulRehman1780/CI-CD-Pipeline-for-ML-project.git'
                        // Uncomment the next line if your repository requires authentication
                        // ,credentialsId: 'github-credentials-id'
                    ]]
                )
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
                // Add deployment steps here
            }
        }
    }
}
