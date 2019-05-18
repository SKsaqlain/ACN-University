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
To view the topology Open the topo.pkt file using Cisco Packet Tracer
<br/>Link to download Cisco Packet Tracer
```
https://www.netacad.com/courses/packet-tracer
```
Link to download docker on ubuntu 16.04
```
https://docs.docker.com/install/linux/docker-ce/ubuntu/
```
Create a docker container with ubuntu  image on it
the above command is used to create a server system similarly create containers with changing the name like client1, client2..
```
$ sudo docker run --it --name server ubuntu:16.04 bin/bash 
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
