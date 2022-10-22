from socket import *
import os
import json
save_path=r'\\wsl$\Ubuntu-20.04\home\client_save'
def client_send():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(("127.0.0.1", 12000))
    filename=input()
    if os.path.isfile(filename):
        file_obj = open(filename, "rb")
        base_filename = filename.split("/")[-1]
        print(base_filename, os.path.getsize(filename))
        # 文件属性
        data_header = {

            "filename": base_filename,
            "size": os.path.getsize(filename)
        }
        client.send(json.dumps(data_header).encode())

        # # new add
        # received_size = int(client.recv(1024).decode())
        # file_obj.seek(received_size)

        # for line in file_obj:
        while True:
            file_data = file_obj.read(1024)
            client.send(file_data)
    else:
        print("file is not valid")


client_send()