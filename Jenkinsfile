pipeline {
    agent any

    environment {
        KUBECONFIG = "C:\\Users\\Aashrith\\.kube\\config"
    }

    stages {

        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flask-devops .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s/ --validate=false'
            }
        }
    }

    post {
        success {
            echo '✅ Jenkins CI/CD pipeline completed successfully'
        }
        failure {
            echo '❌ Jenkins pipeline failed'
        }
    }
}
