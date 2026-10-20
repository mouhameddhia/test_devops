pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                bat 'python -m unittest discover -s . -p "test_*.py" -v'
            }
        }
    }
}
