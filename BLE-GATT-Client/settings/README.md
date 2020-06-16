# required docker packages
- docker

# build
```bash
cd BLE-GATT-Client/settings/jenkins/
docker build . -t jenkins-test-server:lts
```

# start 
```bash
docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins-test-server:lts
```

# update job templates
## get volume location
```bash
[mic@x1 jenkins]$ docker volume inspect jenkins_home
Emulate Docker CLI using podman. Create /etc/containers/nodocker to quiet msg.
[
     {
          "Name": "jenkins_home",
          "Driver": "local",
          "Mountpoint": "/home/mic/.local/share/containers/storage/volumes/jenkins_home/_data",
          "CreatedAt": "2020-04-23T22:59:42.868657393+02:00",
          "Labels": {
               
          },
          "Scope": "local",
          "Options": {
               
          }
     }
]
```
## create template jobs
copy all `config.xml` files to the folder `jenkins/jobs` rename `config.xml` file to `config.xml.override`
