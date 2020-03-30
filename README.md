# jenkins-head
This repository contains gatt-server and gatt-client software. The Main goal of this project is, to visualize the Jenkins state with a jenkins figure :) 

TODO: add picture of the jenkins head

# system overview

![System Overview](./docs/diagrams/out/system-overview/system-overview.png)


## GATT Client
The GATT Client collects the state of all registered Jenkins jobs. (see more details [here](BLE-GATT-Client/README.md))
The Jobs are organised in groups. The state of a group is visualized with a Jenkins head (BLE Server)
A state is represented as an **RGB** value pushed by the GATT Client to the GATT Server (Jenkins Head).

### Client Configuration
The configuration of the client address and the jobs that should be monitored are represented as a YAML file e.g.
```yaml
groups:
  - name: "client Name (jenkins head1)"
    ble_mac: "BLE MAC"
    jenkins_jobs:
      jenkins_server1:
        - "/job/path/1" # optional user text
        - "/job/path/2" # this just the path without hostname
      jenkins_server2:
        - "/job/path" # optional user text
  - name: "jenkins head"
    ble_mac: "BLE MAC"
      jenkins_server1:
        - "http://..." # optional user text
        - "http://..."
jenkins_servers:
  jenkins_server1:
    name: "human readable name or discription"
    url: "http://<hostname>[:port]"
    authentication:
      - "username":
      - "key":
  jenkins_server2:
    name: "human readable name or discription"
    url: "http://<hostname>[:port]"
    authentication:
     - "username": "bot-user"
     - "key": "secret"
```

## GATT Sever
The GATT Server is colouring the jenkins head regarding the **RGB** value that is set from the GATT client. For further information see the documentation of the [GATT Server](BLE-GATT-Server/README.md) documentation.

# Sequence

![Sequence Diagram](./docs/diagrams/out/sequence-diagram/sequence-diagram.png)
