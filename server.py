import socket
from kazoo import client as kz_client
import json
import logging
import uuid
import datetime
logging.basicConfig()



my_client = kz_client.KazooClient(hosts='127.0.0.1:2181')




#function to check whether the server has connected to zookeeper or not
def my_listener(state):
    if state == kz_client.KazooState.CONNECTED:
        print("Server Up and Running  !!!")

my_client.add_listener(my_listener)
#starting the client
my_client.start()


#list to store active host attributes.
active_hosts=[]
active_ips=[]
active_macs=[]
active_from=[]


#list to store in-active host attributes.
inactive_hosts=[]
inactive_ips=[]
inactive_macs=[]
inactive_from=[]


#watch function to detect active/in-active children
@my_client.ChildrenWatch("/")
def watch_children(children):
        #print(children)
        global hosts
        global ips
        #when new hosts is connected or undergoes a state change update the lists.
        if(len(children)>len(active_hosts)):
                x=my_client.get_children("/")
                #active states
                for ele in x:
                        if(ele not in  active_hosts and ele !="zookeeper"):
                                active_hosts.append(ele)
                                data=my_client.get("/"+ele)[0]
                                #print(data)
                                data=json.loads(data)
                                active_ips.append(data['ip'])
                                active_macs.append(data['mac'])
                                active_from.append(data['time'])
                                #print(data)
                #inactive state to active state.
                for ele in x:
                        if(ele in inactive_hosts):
                                inx=inactive_hosts.index(ele)
                                inactive_hosts.pop(inx)
                                inactive_ips.pop(inx)
                                inactive_macs.pop(inx)
                                inactive_from.pop(inx)
        else:
                for ele in active_hosts:
                        #print(ele)
                        if(ele not in children):
                                inx=active_hosts.index(ele)

                                inactive_ips.append(active_ips[inx])
                                inactive_hosts.append(active_hosts[inx])
                                inactive_macs.append(active_macs[inx])
                                inactive_from.append(str(datetime.datetime.today()))

                                active_hosts.pop(inx)
                                active_ips.pop(inx)
                                active_macs.pop(inx)
                                active_from.pop(inx)

        if(len(active_hosts)>0):
                print "-|-"*15
                print "active/inactive\thost\t\tip\t\t\tmac\t\t\t\tstatus"

        for i in range(0,len(active_hosts)):
                print active_from[i]+"\t"+active_hosts[i]+"\t\t"+active_ips[i]+"\t\t"+active_macs[i]+"\t\t"+"active"

        for i in  range(0,len(inactive_hosts)):
                print inactive_from[i]+"\t"+inactive_hosts[i]+"\t\t"+inactive_ips[i]+"\t\t"+inactive_macs[i]+"\t\t"+"inactive"



t=str(datetime.datetime.today())
l=(':'.join(['{:02x}'.format((uuid.getnode()>>ele)&0xff) for ele in range(0,8*6,8)][::-1]))
data={"ip":socket.gethostbyname(socket.gethostname()),"mac":l,"time":t}

#adding the pid of the current process as the data to the created ephimeral sequential znode
path=my_client.create("/server",value=json.dumps(data),ephemeral=True,sequence=False)


while(1):
        pass

#closing the client
my_client.stop()
