import socket , sys
textport = sys.argv[2]
s= socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
port = int(textport)
s.connect( (host,port) )
print( "enter data to transmit:" )
data = sys.stdin.readline().strip()
s.sendall(data)
print ("looking for replies")
while 1:
	buf = s.recv(2048)
	if not len( buf ):
		break;
	sys.stdout.write(buf)
	
