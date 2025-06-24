pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Rohit-jayaraj/python_test.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\Users\rohit\AppData\Local\Programs\Python\Python313\python.exe" -m pip install -r requirements.txt'
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
