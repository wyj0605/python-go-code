#!/usr/bin/python
import socket
import time
from sms import sms
import logging
import time
def port_try(host,port):
    shijian=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    sk.settimeout(1)  
    try:  
        sk.connect((host,port))  
        t=host+"服务器 "+str(port)+" 连接正常 "+str(shijian)
        #sms(t)
        #print t
    except Exception:  
        w=host+" 服务器 "+str(port)+" 无法连接 "+str(shijian)
        #print w
        sms(w)
    sk.close()  

file = open("/root/script/ip.txt")

while True:
	line = file.readline().strip('\n')
	if len(line)==0:break
	ip=str(line.split(':',1)[0])
	port=int(line.split(':',1)[1])
	port_try(ip,port)
	#time.sleep(2)
