# Development setup

This is a collection of notes to setup a development environment.

## Jenkins instance

To test the jenkins-head-controller we need a jenkins instance to run the tests.
This jenkins instance is also needed to test if the `jenkins api handler` works properly.

### Docker container
On the [jenkins website](https://jenkins.io/download/) you find the [docker image](https://hub.docker.com/r/jenkins/jenkins).
This was used to setup a jenkins test instance. The created container is not stored here.

Here is a quick summary to start the instance

    # docker installation finished
    docker pull jenkins/jenkins:lts
    docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
    # finish installation procedure

