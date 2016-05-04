import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = socket.getservbyname('http','tcp')
s.connect(("www.baidu.com",port))
print ( "connected from" , s.getsockname())
print ( "connected to " , s.getpeername() )
