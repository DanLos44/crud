CRUD(Create, Read, Update, Delete) pipeline project 
==========================

General
------------

It implements a pipeline in Jenkins using an agent that on each run:
1)Builds an image for a CRUD project(Create, Read, Update, and Delete operatinos on a mongoDB database) runs a test and uploads updated image to dockerhub.

2)Deploys the app to an EKS cluster.

3)Sendings logs to an elastic-search server using filebeat and showing graphs using kibana.

It saves the data in a mongo-DB server and reading secrets from a vault server

How to build
------------

First of all make sure you have the folowing:
1)Jenkins server with a webhook

You can install it running the following command:

 `docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk11`

2)Docker installed on the agent
- You can visit this site on how to install docker: https://docs.docker.com/engine/install/ubuntu/

3)DockerHub repository

4)Fully operational AWS EKS
- You can visit this site on how to install EKS: https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html


5)Install AWS cli 
 `- curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"`
 
 `- unzip -u awscliv2.zip`
 
 `- sudo ./aws/install`
 
 `- aws --version`

6)Vault server

You can use the following command to run it as docker container:

 `- docker run -d --cap-add=IPC_LOCK -e 'VAULT_LOCAL_CONFIG={"storage": {"file": {"path": "/vault/file"}}, "listener": [{"tcp": { "address": "0.0.0.0:8200", "tls_disable": true}}], "default_lease_ttl": "168h", "max_lease_ttl": "720h", "ui": true}' -p 8200:8200 vault server`

7)MongoDB server, you can even use the one they provide for free on their website

8)ELK stack server

Note:he ELK stack requires a change on the mmap counts to not run out of virtual memory during installation and use. 
To run as a docker container use these commands:

  `- sudo sysctl -w vm.max_map_count=262144`
  
  `- sudo docker run -p 5601:5601 -p 9200:9200 -p 5044:5044 -it --name elk sebp/elk`

9)Filebeat
- Visit this site fore more info: https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation-configuration.html

How to run
------------

1)Set the vault secrets and edit these parts of the code in app.py:

response = client.secrets.kv.v2.read_secret_version(
    mount_point='(secret engine)',
    path='(your/path)'
)

`password = response['data']['data']['(your password secret name)']`

`user = response['data']['data']['(your username secret name)']`

2)In your Jenkins server setup the secrets in this line in the Jenkinsfile
`VAULT_CREDENTIALS = credentials('(your_VAULT_CREDENTIALS)')`

and edit VAULT_ADDR=(yourVaultIP) in the right places

3)Edit this line with your cluster info as well
`- sh 'kubectl config use-context arn:aws:eks:us-east-1:342375422541:cluster/my-cluster'`



How to interact
------------
The service type is a load balancer
You can access it using your AWS load-balancer url
And view logs on your elk stack server

