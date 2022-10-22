from socket import *
import os
import json
ip='192.168.56.1'
server_port=12000
save_path=r'\\wsl$\Ubuntu-20.04\home\server_save'
def server_receive():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(2)
    print('The server is ready to receive')
    while True:
        connect, client_adr = server_socket.accept()
        print("got a new conn:", client_adr)
        while True:
            data = connect.recv(1024)
            print("recev:", data)
            data = json.loads(data.decode())
            if not os.path.exists(data["filename"]):
                    file_obj = open("/mnt/d/XJTLU/CAN201/tcp/xjtlu1.jpg", "wb")
                    received_size = 0
                    while received_size < data["size"]:
                        rece_data = connect.recv(4096)
                        file_obj.write(rece_data)
                        received_size += len(rece_data)
                    else:
                        print("----successful received file [%s]---", data["filename"])
                        file_obj.close()
            else:

                    received_size = os.path.getsize(data["filename"])
                    connect.send(str(received_size).encode())

                    file_obj = open(data["filename"], "ab")
                    while received_size < data["size"]:

                        rece_data = connect.recv(4096)
                        file_obj.write(rece_data)
                        received_size += len(rece_data)
                    else:
                        print("----successful received file [%s]---", data["filename"])
                        file_obj.close()





server_receive()