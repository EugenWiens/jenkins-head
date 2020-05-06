# required docker packages
- docker

# build
cd BLE-GATT-Client/settings/jenkins/
docker build . -t jenkins-test-server:lts

# start 
docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins-test-server:lts
