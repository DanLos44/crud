
pipeline {
    agent {
        label 'docker'
    }
    environment {
    	DOCKERHUB_CREDENTIALS = credentials('daniellosev-dockerhub')
    	MONGO_CREDENTIALS = credentials('MONGO_PASSWORD')
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
             dir('/home/ubuntu/workspace/crud'){    	
                sh 'echo $MONGO_PASSWORD | export MONGO_PASSWORD="$(< /dev/stdin)"'
	     	sh 'python3 -m unittest test_app.py'
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
