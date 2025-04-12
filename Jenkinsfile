pipeline {
    agent none
    environment {
        APP_NAME = 'flask-app'
    }
    stages {
        stage('Verify Docker Setup - Staging') {
            agent { label 'staging' }
            steps {
                bat 'docker -v'
                bat 'docker-compose -v'
            }
        }

        stage('Verify Docker Setup - Production') {
            agent { label 'production' }
            steps {
                sh 'docker -v'
                sh 'docker-compose -v'
            }
        }

        stage('Build') {
            agent any
            steps {
                script {
                    // Build Docker images using docker-compose
                    sh 'docker-compose -f docker-compose.yml build'
                }
            }
        }

        stage('Test') {
            agent any
            steps {
                script {
                    // Run unit tests
                    sh 'python -m unittest discover tests/'
                }
            }
        }

        stage('Deploy to Staging') {
            agent { label 'staging' }
            steps {
                script {
                    // Deploy Docker containers to Staging environment
                    sh 'docker-compose -f docker-compose.yml up -d staging'
                }
            }
        }

        stage('Deploy to Production') {
            agent { label 'production' }
            steps {
                script {
                    // Deploy Docker containers to Production environment
                    sh 'docker-compose -f docker-compose.yml up -d production'
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline execution failed!'
        }
    }
}
