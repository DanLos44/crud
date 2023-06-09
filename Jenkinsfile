pipeline {
    agent {
        label 'docker'
    }
    environment {
        DOCKERHUB_CREDENTIALS = credentials('daniellosev-dockerhub')
        VAULT_CREDENTIALS = credentials('your_VAULT_CREDENTIALS')
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
                withCredentials([string(credentialsId: 'VAULT_CREDENTIALS', variable: 'token')]) {
                    sh 'docker run --rm -e VAULT_TOKEN=${token} -e VAULT_ADDR=(yourVaultIP) daniellosev/weather:mongoapp python3 -m unittest test_app.py'
                }
            }
        }
              
        stage('Deploy') {
            steps {
                withCredentials([string(credentialsId: 'VAULT_CREDENTIALS', variable: 'token')]) {
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    sh 'kubectl config use-context arn:aws:eks:us-east-1:342375422541:cluster/my-cluster'
                    sh 'kubectl apply -f mongo-app-deployment.yaml'
                    sh 'kubectl set env deployment/mongo-app VAULT_TOKEN=${token} VAULT_ADDR=(yourVaultIP)'
                    sh 'kubectl rollout restart deployment/mongo-app'
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


