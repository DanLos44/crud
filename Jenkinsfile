
pipeline {
    agent {
        label 'docker'
    }
    environment {
    	DOCKERHUB_CREDENTIALS = credentials('daniellosev-dockerhub')
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
	     	sh 'python3 -m unittest test_app.py'
             }
          }
       }
 }
       post {
         always {
          sh 'sudo docker logout'          
          }
        success {
                slackSend ( channel: '#successful-build', token: 'y3BoT2qJbqZXhyLfgWAMULI4', message: "Everything is good")
        }
        failure {
                slackSend( channel: "#devops-alerts", token: 'y3BoT2qJbqZXhyLfgWAMULI4', message: "Test failed")
        }
          }
 }
