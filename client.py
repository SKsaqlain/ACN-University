import socket
from kazoo import client as kz_client
import logging
import time
import json
import uuid
logging.basicConfig()
import datetime

#hosts=ip of the master instance/container followed by the port that he zk is running
#change the hosts ip addres.
my_client = kz_client.KazooClient(hosts='172.17.0.2:2181')

#function to check whether the client has connected to zookeeper or not
def my_listener(state):
    if state == kz_client.KazooState.CONNECTED:
        print("Client is connected to the SERVER !!!")

my_client.add_listener(my_listener)
#starting the client
my_client.start()

t=str(datetime.datetime.today())

#getting the mac address of the instance
l=(':'.join(['{:02x}'.format((uuid.getnode()>>ele)&0xff) for ele in range(0,8*6,8)][::-1]))

data={"ip":socket.gethostbyname(socket.gethostname()),"mac":l,"time":t}

#/client->is the name of the ephemeral node #each instance should have a unique name thus change appropriately wherever required
path=my_client.create("/client",value=json.dumps(data),ephemeral=True,sequence=False)

#infinite loop to prevetn the current process to terminate by itsel
while(1):
        pass

#closing the client when program is aborted
my_client.stop()
