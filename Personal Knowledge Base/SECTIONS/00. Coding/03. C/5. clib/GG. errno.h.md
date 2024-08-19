# Описание 

Заголовочный _<errno.h>_ определяет целочисленную переменную _errno_ , 
        который задается системными вызовами и некоторыми библиотечными функциями в 
        событие ошибки, чтобы указать, что пошло не так. 

   **ошибаться** Значение в _errno_ имеет значение только тогда, когда возвращаемое значение 
        вызов указал на ошибку (т. е. -1 для большинства системных вызовов; -1 
        или NULL из большинства библиотечных функций); функция, которая удалась _,_ разрешено изменить _errno_ . Значение _errno_ никогда не устанавливается равным нулю  любым системным вызовом или библиотечной функцией. 

 Для некоторых системных вызовов и библиотечных функций (например,   [getpriority(2)](https://man7.org/linux/man-pages/man2/getpriority.2.html) ), -1 является действительным возвратом в случае успеха. В таких случаях,  успешное возвращение можно отличить от возврата с ошибкой по установка _errno_ в ноль перед вызовом, а затем, если вызов  возвращает статус, указывающий на то, что могла произойти ошибка,  проверка, имеет ли _errno_ ненулевое значение. 

     _errno_ определяется стандартом ISO C как изменяемое значение lvalue. 
        типа _int_ и не должен быть явно объявлен; _может_ быть 
        макрос. _errno_ является локальным для потока; установка его в одном потоке не 
        влияет на его значение в любом другом потоке. 

   **Номера и названия ошибок** Допустимые номера ошибок — все положительные числа. > _<ошибка.h_ заголовочный файл определяет символические имена для каждой из возможных ошибок 
        числа, которые могут появиться в _errno_ . 

        Все имена ошибок, указанные в POSIX.1, должны иметь разные имена. 
        значения, за исключением **EAGAIN** и **EWOULDBLOCK** , которые могут 
        быть таким же. В Linux эти два параметра имеют одинаковое значение на всех 
        архитектуры. 
Заголовок _<errno.h>_ должен предоставлять объявление для _errno_ и давать положительные значения для следующих символические константы. Их значения должны быть уникальными, за исключением случаев, указанных ниже.

The _<errno.h>_ header shall provide a declaration for _errno_ and give positive values for the following symbolic constants. Their values shall be unique except as noted below.

[E2BIG]

Argument list too long.

[EACCES]

Permission denied.

[EADDRINUSE]

Address in use.

[EADDRNOTAVAIL]

Address not available.

[EAFNOSUPPORT]

Address family not supported.

[EAGAIN]

Resource unavailable, try again (may be the same value as [EWOULDBLOCK]).

[EALREADY]

Connection already in progress.

[EBADF]

Bad file descriptor.

[EBADMSG]

Bad message.

[EBUSY]

Device or resource busy.

[ECANCELED]

Operation canceled.

[ECHILD]

No child processes.

[ECONNABORTED]

Connection aborted.

[ECONNREFUSED]

Connection refused.

[ECONNRESET]

Connection reset.

[EDEADLK]

Resource deadlock would occur.

[EDESTADDRREQ]

Destination address required.

[EDOM]

Mathematics argument out of domain of function.

[EDQUOT]

Reserved.

[EEXIST]

File exists.

[EFAULT]

Bad address.

[EFBIG]

File too large.

[EHOSTUNREACH]

Host is unreachable.

[EIDRM]

Identifier removed.

[EILSEQ]

Illegal byte sequence.

[EINPROGRESS]

Operation in progress.
The _<errno.h>_ header shall provide a declaration for _errno_ and give positive values for the following symbolic constants. Their values shall be unique except as noted below.

[E2BIG]

Argument list too long.

[EACCES]

Permission denied.

[EADDRINUSE]

Address in use.

[EADDRNOTAVAIL]

Address not available.

[EAFNOSUPPORT]

Address family not supported.

[EAGAIN]

Resource unavailable, try again (may be the same value as [EWOULDBLOCK]).

[EALREADY]

Connection already in progress.

[EBADF]

Bad file descriptor.

[EBADMSG]

Bad message.

[EBUSY]

Device or resource busy.

[ECANCELED]

Operation canceled.

[ECHILD]

No child processes.

[ECONNABORTED]

Connection aborted.

[ECONNREFUSED]

Connection refused.

[ECONNRESET]

Connection reset.

[EDEADLK]

Resource deadlock would occur.

[EDESTADDRREQ]

Destination address required.

[EDOM]

Mathematics argument out of domain of function.

[EDQUOT]

Reserved.

[EEXIST]

File exists.

[EFAULT]

Bad address.

[EFBIG]

File too large.

[EHOSTUNREACH]

Host is unreachable.

[EIDRM]

Identifier removed.

[EILSEQ]

Illegal byte sequence.

[EINPROGRESS]

Operation in progress.

[EINTR]

Interrupted function.

[EINVAL]

Invalid argument.

[EIO]

I/O error.

[EISCONN]

Socket is connected.

[EISDIR]

Is a directory.

[ELOOP]

Too many levels of symbolic links.

[EMFILE]

Too many open files.

[EMLINK]

Too many links.

[EMSGSIZE]

Message too large.

[EMULTIHOP]

Reserved.

[ENAMETOOLONG]

Filename too long.

[ENETDOWN]

Network is down.

[ENETRESET]

Connection aborted by network.

[ENETUNREACH]

Network unreachable.

[ENFILE]

Too many files open in system.

[ENOBUFS]

No buffer space available.

[ENODATA]

[XSR] ![[Option Start]](https://pubs.opengroup.org/onlinepubs/009695399/images/opt-start.gif) No message is available on the STREAM head read queue. ![[Option End]](https://pubs.opengroup.org/onlinepubs/009695399/images/opt-end.gif)

[ENODEV]

No such device.

[ENOENT]

No such file or directory.

[ENOEXEC]

Executable file format error.

[ENOLCK]

No locks available.

[ENOLINK]

Reserved.

[ENOMEM]

Not enough space.

[ENOMSG]

No message of the desired type.

[ENOPROTOOPT]

Protocol not available.

[ENOSPC]

No space left on device.

[ENOSR]

[XSR] ![[Option Start]](https://pubs.opengroup.org/onlinepubs/009695399/images/opt-start.gif) No STREAM resources. ![[Option End]](https://pubs.opengroup.org/onlinepubs/009695399/images/opt-end.gif)

[ENOSTR]

[XSR] ![[Option Start]](https://pubs.opengroup.org/onlinepubs/009695399/images/opt-start.gif) Not a STREAM. ![[Option End]](https://pubs.opengroup.org/onlinepubs/009695399/images/opt-end.gif)

[ENOSYS]

Function not supported.

[ENOTCONN]

The socket is not connected.

[ENOTDIR]

Not a directory.

[ENOTEMPTY]

Directory not empty.

[ENOTSOCK]

Not a socket.

[ENOTSUP]

Not supported.

[ENOTTY]

Inappropriate I/O control operation.

[ENXIO]

No such device or address.

[EOPNOTSUPP]

Operation not supported on socket.

[EOVERFLOW]

Value too large to be stored in data type.

[EPERM]

Operation not permitted.

[EPIPE]

Broken pipe.

[EPROTO]

Protocol error.

[EPROTONOSUPPORT]

Protocol not supported.

[EPROTOTYPE]

Protocol wrong type for socket.

[ERANGE]

Result too large.

[EROFS]

Read-only file system.

[ESPIPE]

Invalid seek.

[ESRCH]

No such process.

[ESTALE]

Reserved.

[ETIME]

[XSR] ![[Option Start]](https://pubs.opengroup.org/onlinepubs/009695399/images/opt-start.gif) Stream [_ioctl_()](https://pubs.opengroup.org/onlinepubs/009695399/functions/ioctl.html) timeout. ![[Option End]](https://pubs.opengroup.org/onlinepubs/009695399/images/opt-end.gif)

[ETIMEDOUT]

Connection timed out.

[ETXTBSY]

Text file busy.

[EWOULDBLOCK]

Operation would block (may be the same value as [EAGAIN]).

[EXDEV]

Cross-device link.
[EINTR]

Interrupted function.

[EINVAL]

Invalid argument.

[EIO]

I/O error.

[EISCONN]

Socket is connected.

[EISDIR]

Is a directory.

[ELOOP]

Too many levels of symbolic links.

[EMFILE]

Too many open files.

[EMLINK]

Too many links.

[EMSGSIZE]

Message too large.

[EMULTIHOP]

Reserved.

[ENAMETOOLONG]

Filename too long.

[ENETDOWN]

Network is down.

[ENETRESET]

Connection aborted by network.

[ENETUNREACH]

Network unreachable.

[ENFILE]

Too many files open in system.

[ENOBUFS]

No buffer space available.

[ENODATA]

[XSR] ![[Option Start]](https://pubs.opengroup.org/onlinepubs/009695399/images/opt-start.gif) No message is available on the STREAM head read queue. ![[Option End]](https://pubs.opengroup.org/onlinepubs/009695399/images/opt-end.gif)

[ENODEV]

No such device.

[ENOENT]

No such file or directory.

[ENOEXEC]

Executable file format error.

[ENOLCK]

No locks available.

[ENOLINK]

Reserved.

[ENOMEM]

Not enough space.

[ENOMSG]

No message of the desired type.

[ENOPROTOOPT]

Protocol not available.

[ENOSPC]

No space left on device.

[ENOSR]

[XSR] ![[Option Start]](https://pubs.opengroup.org/onlinepubs/009695399/images/opt-start.gif) No STREAM resources. ![[Option End]](https://pubs.opengroup.org/onlinepubs/009695399/images/opt-end.gif)

[ENOSTR]

[XSR] ![[Option Start]](https://pubs.opengroup.org/onlinepubs/009695399/images/opt-start.gif) Not a STREAM. ![[Option End]](https://pubs.opengroup.org/onlinepubs/009695399/images/opt-end.gif)

[ENOSYS]

Function not supported.

[ENOTCONN]

The socket is not connected.

[ENOTDIR]

Not a directory.

[ENOTEMPTY]

Directory not empty.

[ENOTSOCK]

Not a socket.

[ENOTSUP]

Not supported.

[ENOTTY]

Inappropriate I/O control operation.

[ENXIO]

No such device or address.

[EOPNOTSUPP]

Operation not supported on socket.

[EOVERFLOW]

Value too large to be stored in data type.

[EPERM]

Operation not permitted.

[EPIPE]

Broken pipe.

[EPROTO]

Protocol error.

[EPROTONOSUPPORT]

Protocol not supported.

[EPROTOTYPE]

Protocol wrong type for socket.

[ERANGE]

Result too large.

[EROFS]

Read-only file system.

[ESPIPE]

Invalid seek.

[ESRCH]

No such process.

[ESTALE]

Reserved.

[ETIME]

[XSR] ![[Option Start]](https://pubs.opengroup.org/onlinepubs/009695399/images/opt-start.gif) Stream [_ioctl_()](https://pubs.opengroup.org/onlinepubs/009695399/functions/ioctl.html) timeout. ![[Option End]](https://pubs.opengroup.org/onlinepubs/009695399/images/opt-end.gif)

[ETIMEDOUT]

Connection timed out.

[ETXTBSY]

Text file busy.

[EWOULDBLOCK]

Operation would block (may be the same value as [EAGAIN]).

[EXDEV]

Cross-device link.



# Разбор


errno.h — [заголовочный файл](https://en.wikipedia.org/wiki/Header_file) в [стандартной библиотеке](https://en.wikipedia.org/wiki/C_standard_library) языка [C.](https://en.wikipedia.org/wiki/C_(programming_language)) программирования. Он определяет [макросы](https://en.wikipedia.org/wiki/Macro_(computer_science)) для сообщения и получения ошибок с помощью символа `errno`(сокращение от «номер ошибки»).

`errno` действует как целочисленная переменная. Значение (номер ошибки) хранится в `errno`некоторыми [библиотечными функциями](https://en.wikipedia.org/wiki/Library_function) , когда они обнаруживают ошибки. При запуске программы сохраненное значение равно нулю. Библиотечные функции хранят только значения больше нуля. Любая библиотечная функция может изменить значение, сохраненное перед возвратом, независимо от того, обнаруживают ли они ошибки. [[2]](https://en.wikipedia.org/wiki/Errno.h#cite_note-C99-2) Большинство функций сообщают об обнаружении ошибки, возвращая специальное значение, обычно [NULL](https://en.wikipedia.org/wiki/Null_pointer) для функций, возвращающих [указатели](https://en.wikipedia.org/wiki/Pointer_(computer_programming)) , и -1 для функций, возвращающих целые числа. Некоторые функции требуют от вызывающего абонента предварительной настройки. `errno`на ноль и затем проверьте его, чтобы увидеть, была ли обнаружена ошибка.

  
  

Заголовочный _<errno.h>_ определяет целочисленную переменную _errno_ , 
        который задается системными вызовами и некоторыми библиотечными функциями в 
        событие ошибки, чтобы указать, что пошло не так. 

**ошибаться** 
        Значение в _errno_ имеет значение только тогда, когда возвращаемое значение вызов указал на ошибку (т. е. -1 для большинства системных вызовов; -1 или NULL из большинства библиотечных функций); функция, которая удалась_,_ разрешено изменить _errno_ . Значение _errno_ никогда не устанавливается равным нулю  любым системным вызовом или библиотечной функцией. 


  

## Системный вызов **perror().**

## Описание

Библиотечная функция C **void perror(const char *str)** выводит описательное сообщение об ошибке в stderr. строка **str** печатается

## Декларация

Ниже приведено объявление функции perror().

void perror(const char *str)

## Параметры

-   **str** — это строка C, содержащая пользовательское сообщение, которое будет напечатано перед самим сообщением об ошибке.
    

## Возвращаемое значение

Эта функция не возвращает никакого значения.

Ниже приведено объявление функции perror().

void perror(const char *str)использование функции perror().

[Живая демонстрация](http://tpcg.io/PNUmJR)

>
**#include <stdio.h>**
>
**int main () {**
   **FILE *fp;**
>
   **/* first rename if there is any file */**
   **/* now let's try to open same file */**
   **fp = fopen("file.txt", "r");**
   **if( fp == NULL ) {**
      **perror("Error: ");**
      **return(-1);**
   **}**
   **fclose(fp);**
  >    
   **return(0);**
**}**

Давайте скомпилируем и запустим вышеуказанную программу, которая даст следующий результат, потому что мы пытаемся открыть несуществующий файл:

Error: : No such file or directory
>
   **rename("file.txt", "newfile.txt");**
>
   **/* now let's try to open same file */**
   **fp = fopen("file.txt", "r");**
   **if( fp == NULL ) {**
      **perror("Error: ");**
      **return(-1);**
   **}**
   **fclose(fp);**
  >    
   **return(0);**
**}**

Давайте скомпилируем и запустим вышеуказанную программу, которая даст следующий результат, потому что мы пытаемся открыть несуществующий файл:

Error: : No such file or directory