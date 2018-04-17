
import socket , sys,time
host = "192.168.117.33"
port = 10002
s= socket.socket(socket.AF_INET , socket.SOCK_STREAM)
a=time.time()
s.connect( (host,port) )
a=time.time()
for i in range(0,100):
        buff = s.recv(2048)
        s.send(b"12121")
        #print('hello')
print("finish",time.time()-a)
	
