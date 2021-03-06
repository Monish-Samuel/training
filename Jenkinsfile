node{
  stage('SCM Checkout'){
    git 'https://github.com/Monish-Samuel/training.git'
  }
  stage('Compile-Package'){
    sh 'mvn package'
  }
}
