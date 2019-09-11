
pipeline {

    agent {
        docker 'gcr.io/organic-storm-201412/docker-tac-develop:latest'
    }

    stages {

        stage('Unit Tests & Code Style Check') {

            parallel {

                stage('Code Style Check') {

                    steps {
                        sh 'pip3 install tox'
                        sh 'tox -e flake8'
                    }

                } // code style check

                stage('Static Type Check') {

                    steps {
                        sh 'pip3 install mypy'
                        sh 'mypy sandbox scripts simulation/v1 tac tests templates'
                    }

                } // static type check

                stage('Unit Tests') {

                    steps {
                        sh 'pip3 install tox'
                        sh 'tox -e py37 -- --no-oef'
                    }

                } // unit tests

            } // stages

        }  // unit tests & code style check

    } // stages

} // pipeline
