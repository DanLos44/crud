
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
			withCredentials([usernamePassword(credentialsId: 'MONGO_CREDENTIALS', usernameVariable: 'mongo_username', passwordVariable: 'mongo_password')]) {
    			sh "echo ${mongo_username}"
    			sh "echo ${mongo_password}"
                        sh 'echo Running app'
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
