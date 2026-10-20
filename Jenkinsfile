pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s . -p "test_*.py" -v'
            }
        }
    }
}
