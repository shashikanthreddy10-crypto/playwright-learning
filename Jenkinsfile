pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                bat 'python -m playwright install'
            }
        }

        stage('Run Playwright Tests') {
            steps {
                bat 'python -m pytest'
            }
        }
    }
}