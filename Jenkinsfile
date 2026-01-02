pipeline {
    agent any
    environment {
        IMAGE_NAME = "image-app"
        TARGET_SERVER = "vaishnavi.asutkar@172.25.3.113"
    }

    stages {
        stage("Clone Code") {
            steps {
                git branch: 'main',
                    url: 'https://github.com/vasutkar-0/Python-app-code.git'
            }
        }

        stage("Build Docker Image") {
            steps {
                sh "docker build -t $IMAGE_NAME ."
            }
        }

        stage("Save Image") {
            steps {
                sh "docker save $IMAGE_NAME > image-app.tar"
            }
        }

        stage("Deploy to Target Server") {
            steps {
                sh """
                scp image-app.tar $TARGET_SERVER:/home/vaishnavi.asutkar/
                ssh $TARGET_SERVER '
                  docker load < image-app.tar
                  docker stop image-app || true
                  docker rm image-app || true
                  docker run -d --name image-app -p 5000:5000 image-app
                '
                """
            }
        }
    }

    post {
        success {
            echo "🎉 Deployment Successful!"
        }
    }
}

