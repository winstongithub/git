import socket
import queue
from select import select
import time
SERVER_IP = ('104.224.171.245',9999)
#SERVER_IP = ('127.0.0.1',9999)

message_queue={}
input_list=[]
output_list=[]
client_list=[]

if __name__=="__main__":
    server=socket.socket()
    server.bind(SERVER_IP)
    server.listen(3)
    server.setblocking(False)
    input_list.append(server)
    while True:
        time.sleep(1)
        stdinput , stdoutput,stderror = select(input_list,output_list,input_list)

        for obj in stdinput:
            if obj == server:
                conn,addr = server.accept()
                print("client{0}connected!".format(addr))
                input_list.append(conn)
                message_queue[conn]=queue.Queue()
                client_list.append(conn)
            else:
                try:
                    recv_data=obj.recv(1024)
                    if recv_data:
                        print("received{0} from client{1}".format(recv_data.decode(),addr))
                        for client in client_list:
                            if client!= obj:
                                message_queue[client].put(recv_data)
                                if obj not in output_list:
                                    output_list.append(client)

                except ConnectionResetError:
                    input_list.remove(obj)
                    client_list.remove(obj)
                    if obj in output_list:
                        output_list.remove(obj)
                    del message_queue[obj]
                    print("[input] client {0} disconnected".format(addr))

        for sendobj in output_list:
            try:
                if not message_queue[sendobj].empty():
                    send_data = message_queue[sendobj].get()
                    sendobj.sendall(send_data)
                else:
                    output_list.remove(sendobj)
            except ConnectionResetError:
                del message_queue[sendobj]
                output_list.remove(sendobj)
                print("\n[output] Client  {0} disconnected".format(addr)) 
                              
