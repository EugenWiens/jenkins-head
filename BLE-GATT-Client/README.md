
- [General](#general)
  - [Installation](#installation)
  - [systemd service](#systemd-service)
- [System Overview](#system-overview)
    - [Client Configuration](#client-configuration)
- [Development](#development)
  - [listing all sessions](#listing-all-sessions)
  - [executing all default sessions](#executing-all-default-sessions)
  - [executing special session](#executing-special-session)
    - [executing special session with parameter for the session](#executing-special-session-with-parameter-for-the-session)

# General

The **GATT client** is a **python3** daemon designed to run on a system with BLE support.

It polls the REST-API of jenkins servers to read the job states.
A jenkins-head (GATT server) represents the state of a group.

## Installation

TODO

## systemd service

To set up the `jenkins-head-controller` to run on boot we prepared a systemd service file.
The following lines will install and enable automatic startup on boot.

    # run the following as root
    # install the service file
    cp  BLE-GATT-Client/templates/jenkins-head-controller.service /etc/systemd/system
    # start the service
    systemctl start jenkins-head-controller
    # check if it is up and running as expected
    systemctl status jenkins-head-controller
    # enable the service on boot
    systemctl enable jenkins-head-controller

# System Overview

![Class Diagram](./doc/diagrams/out/ClassDiagramOverview/GATT-Client_overview.png)


### Client Configuration
The configuration of the client address and the jobs that should be monitored are represented as a YAML file e.g.
```yaml
heads:
  - name: "client Name (jenkins head1)"
    ble_mac: "BLE MAC"  # 00:11:22:33:FF:EE
    jobs:
      jenkins_server1:  # reference id of the server region
        - "job/path/1"  # path of the job
        - "job/path/2"  # path of the job
      jenkins_server2:
        - "job/path"    # path of the job
  - name: "jenkins head"
    ble_mac: "BLE MAC"  # 00:11:22:33:FF:EE
    jobs:
      jenkins_server1:
        - "http://..."  # optional user text
        - "http://..."
servers:
  jenkins_server1:      # server id that can be reference in the jobs area of the heads region
    name: "human readable name or description"
    url: "http://<hostname>[:port]"
    authentication:
      - "username": ""
      - "secret": ""
  jenkins_server2:
    name: "human readable name or description"
    url: "http://<hostname>[:port]"
    authentication:
     - "username": "bot-user"
     - "secret": "secret"
```

# Development
This python project uses [nox](https://nox.thea.codes/en/stable/index.html) as a system to manage the virtual environment and execute commands in it. 

## listing all sessions
```bash
nox --list
```

this output is an example of a list of sessions
```bash
* lint -> run linter for this project
- dev-venv -> create a virtual environment for the development
- build -> build: what ever sdist and bdist_wheels do :)
* tests -> run tests for this project
- deploy-test-pypi -> deploy this package for testing to the pypi test server
- deploy-pypi -> deploy this package to the official pypi server
- distclean -> this command removes all auto generated files

sessions marked with * are selected, sessions marked with - are skipped.
``` 

## executing all default sessions
When executing `nox` in the project path all default selected sessions are executed.

## executing special session
```bash
nox -s lint
```

### executing special session with parameter for the session
Sometimes it is necessary to forward a parameter to the session. e.g. activate extra coverage report to the terminal
```bash
nox -s tests -- --cov-report=term
```
