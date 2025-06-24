pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/your-repo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --junitxml=results.xml'
            }
        }

        stage('Archive Test Results') {
            steps {
                junit 'results.xml'
            }
        }
    }
}
