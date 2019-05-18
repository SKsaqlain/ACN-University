# ACN-University
The project was carried out as a part of the ACN course offered at PES University 2019.

# Description 
The objective of the project was to design a network topology for the given problem scenario and implement some requirements using coding.
One of the requirements of the given scenario was to implement a network monitor system that would monitor the current active hosts that are connected with the server, thus to implement this zookeeper along with docker containers were used.

# Requirements
* cisco packet tracer 
* ubuntu 16.04 
* Docker
* Python 3.5


# Usage 
To clone this repository
```
$git clone https://github.com/SKsaqlain/ACN-University
```
To view, the topology Open the topo.pkt file using Cisco Packet Tracer
<br/>Link to download Cisco Packet Tracer
```
https://www.netacad.com/courses/packet-tracer
```
Link to download docker on ubuntu 16.04
```
https://docs.docker.com/install/linux/docker-ce/ubuntu/
```
Create a docker container with ubuntu  image on it
the above command is used to create a server system similarly create containers with changing the name like client1, client2...
```
$ sudo docker run -it --name server ubuntu:16.04 bin/bash 
```
To stop the container execute the below command
```
$sudo docker stop container-name
```
Install zookeeper server on the server container 
```
$sudo docker start server
$sudo docker exec -it server bin/bash
$sudo mkdir server
```
then follow the  below link
```
https://medium.com/@ryannel/installing-zookeeper-on-ubuntu-9f1f70f22e25
```
Install  kazoo on all the containers
```
$pip install kazoo
```
create a folder called client #(host number) on all  the client containers
<br/>for example on client1 container, similarly on other containers
```
$sudo mkdir client1
```
Move the server.py code from the host to the server container
```
$sudo docker cp /ACN-University/server.py server:/server/
```
Move the client.py code to all the client containers
<br/>_before moving the code make appropriate changes wherever required_
```
$sudo docker cp /ACN-University/client.py client1:/client1/
```
Move into the server container and start the zookeeper server and run the server.py script
```
$sudo docker exec -it server bin/bash
$cd server
$./zookeeper/bin/zkServer.sh start
$python server.py
```
Move into the client containers and run the client.py script
```
$sudo docker exec -it client1 bin/bash
$cd client1
$python client.py
```
As soon as the script is run the client registers itself with the server, thus the server displays the _type_ of the host, the _IP_, the _MAC_ address, the _status_ of the host whether _active_ or _in-active_, the _time_ when it initiated a connection and the _time_ the connection was lost.
<br/>To stop a container, remove a container and remove an image.
```
$sudo docker stop container-name
$sudo docker rm container-name
$sudo docker rmi image-name
```
# License
This project is licensed under the [MIT License](https://github.com/SKsaqlain/ACN-University/master/LICENSE.md)
