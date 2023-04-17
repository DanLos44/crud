pipeline {
    agent {
        label 'docker'
    }
    environment {
    	DOCKERHUB_CREDENTIALS = credentials('daniellosev-dockerhub')
    	MONGO_CREDENTIALS = credentials('MONGO_CREDENTIALS')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building image'
                sh 'docker build -t daniellosev/weather:mongoapp .'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing site'
                withCredentials([usernamePassword(credentialsId: 'MONGO_CREDENTIALS', usernameVariable: 'mongo_username', passwordVariable: 'mongo_password')]) {
                    sh 'docker run --rm -e MONGO_PASSWORD=${mongo_password} daniellosev/weather:mongoapp python3 -m unittest test_app.py'
                }
            }
        }
    }
    post {
        always {
            sh 'sudo docker logout'
        }
    }
}

