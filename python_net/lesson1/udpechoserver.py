import socket , traceback

host = ''
port = 51423
s = socket.socket( socket.AF_INET , socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
s.bind( (host , port )
while 1:
	message , address = s.recvfrom( 8192 )
	s.sendto( message , address)

