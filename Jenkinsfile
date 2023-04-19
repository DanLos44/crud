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
                sh 'docker push daniellosev/weather:mongoapp'
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
        
        stage('Deploy') {
    steps {
        withCredentials([usernamePassword(credentialsId: 'MONGO_CREDENTIALS', usernameVariable: 'mongo_username', passwordVariable: 'mongo_password')]) {
            sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            sh 'kubectl config use-context arn:aws:eks:us-east-1:342375422541:cluster/my-cluster'
	    sh 'kubectl apply -f mongo-app-deployment.yaml'
            sh 'kubectl set env deployment/mongo-app MONGO_PASSWORD=${mongo_password}'
        }
    }
}

}
}

    post {
        always {
            sh 'sudo docker logout'
        }
    }

