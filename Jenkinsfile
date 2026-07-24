pipeline {
  agent any
  stages {
     stage('Checkout Code') {
       steps {
          git branch: 'main', url: 'https://github.com/Anupriya-t-71/Week2_miniproject.git'
       }
     }
     stage('Build Docker Image') {
       steps {
          sh 'docker build -t week2_project .'
       }
     }
     stage('Run App') {
       steps{
          sh 'docker stop week2-app || true'
          sh 'docker rm week2-app || true'
          sh 'docker run -d --name week2-app -p 8081:8080 week2_project'
       }
     }
   } 
 }
