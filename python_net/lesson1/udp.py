import socket , sys,time
host = "192.168.117.33"
port = 10001
s= socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
s.connect( (host,port) )
a=time.time()
for i in range(0,100):
	s.sendall(b"hello world")
	buf = s.recv(2048)
	#print(buf)
print("finish",time.time()-a)
	
