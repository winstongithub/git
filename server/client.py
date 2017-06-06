import socket
from select import select

SERVER_IP = ('104.224.171.245',9999)
#SERVER_IP = ('127.0.0.1',9999)
client = socket.socket()
client.connect(SERVER_IP)
input_list=[client]
output_list=[client]
while True:
    stdinput,stdoutput,stderror=select(input_list,output_list,input_list)
    for obj in stdinput:
        if obj == client:
            recv_data=obj.recv(1024)
            print(recv_data)
    a=input('input')
    client.send(a.encode())

