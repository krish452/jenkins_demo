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
                bat 'docker -v'
                bat 'docker-compose -v'
            }
        }

        stage('Build') {
            agent any
            steps {
                script {
                    try {
                        // Build Docker images using docker-compose
                        bat 'docker-compose -f docker-compose.yml build'
                    } catch (Exception e) {
                        error "Build failed: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Test') {
            agent any
            steps {
                script {
                    try {
                        // Run unit tests
                        bat 'python -m unittest discover tests/'
                    } catch (Exception e) {
                        error "Tests failed: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Deploy to Staging') {
            agent { label 'staging' }
            steps {
                script {
                    try {
                        // Deploy Docker containers to Staging environment
                        bat "docker rm -f flask_app_staging || true"
                        bat 'docker-compose -f docker-compose.yml up -d staging'
                    } catch (Exception e) {
                        error "Staging deployment failed: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Deploy to Production') {
            agent { label 'production' }
            when {
                branch 'main' // Ensure this step runs only on the main branch
                expression { 
                    return currentBuild.previousBuild.result == 'SUCCESS' // Run only if Staging deploy is successful
                }
            }
            steps {
                script {
                    try {
                        // Deploy Docker containers to Production environment
                        bat "docker rm -f flask_app_production || true"
                        bat 'docker-compose -f docker-compose.yml up -d production'
                    } catch (Exception e) {
                        error "Production deployment failed: ${e.getMessage()}"
                    }
                }
            }
        }

        // Handle pull requests from feature branches
        stage('Handle Pull Requests') {
            when {
                branch 'feature/*'
            }
            steps {
                script {
                    echo 'Handling pull request...'
                    // Add any integration steps here, e.g., merging changes
                    bat 'git fetch origin'
                    bat 'git checkout main'
                    bat 'git merge origin/feature/*'
                }
            }
        }
    }
    post {
        always {
            node('') {
                cleanWs()
            }
        }
        success {
            node('') {
                echo 'Pipeline executed successfully!'
            }
        }
        failure {
            node('') {
                echo 'Pipeline execution failed!'
            }
        }
    }
}
