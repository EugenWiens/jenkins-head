
- [required docker packages](#required-docker-packages)
- [build](#build)
- [start](#start)
- [update templates](#update-templates)
  - [get volume location](#get-volume-location)
  - [create generic settings](#create-generic-settings)
  - [create template jobs](#create-template-jobs)
  - [create template users](#create-template-users)
    - [user templates](#user-templates)

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

# update templates
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
## create generic settings
copy followind files 
* config.xml
* jenkins.security.apitoken.ApiTokenPropertyConfiguration.xml
* jenkins.security.QueueItemAuthenticatorConfiguration.xml
* jenkins.security.UpdateSiteWarningsConfiguration.xml

to the `jenkins` folder. Rename `config.xml` file to `config.xml.override`


## create template jobs
copy all `config.xml` files to the folder `jenkins/jobs` rename `config.xml` file to `config.xml.override`

## create template users
copy the whole content of the folder `users` to `jenkins/users` rename all `config.xml` file to `config.xml.override`

### user templates
the templates contains following user
| username | password | api key                            |
| -------- | -------- | ---------------------------------- |
| admin    | admin    | 11dfa2a017dfd5161e069a2244d43c0d9f |
| test     | test     |                                    |

