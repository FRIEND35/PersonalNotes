Написание макроса — это еще один способ обеспечения модульного программирования в [**Ассемблере**](https://ravesli.com/assembler-vstuplenie/).

   - **Макрос** — это последовательность инструкций с именем, которая может использоваться в любом месте программы.

   - В [**NASM**](https://ravesli.com/assembler-nastrojka-sredy-razrabotki/) макросы определяются с помощью директив `%macro` (начало) и `%endmacro` (конец).

Синтаксис для определения макросов следующий:

>`%macro имя_макроса количество_параметров   <тело_макроса>   %endmacro`

Чтобы вызвать макрос, нужно использовать имя макроса вместе с необходимыми параметрами. Когда вам нужно многократно использовать некоторую последовательность инструкций в программе, вы можете поместить эти инструкции в макрос и использовать его вместо постоянного написания этих инструкций.

Например, очень часто в программах требуется выводить [**строки**](https://ravesli.com/assembler-stroki/) символов на экран, для этого можно использовать следующую последовательность инструкций:

>
mov edx,len     ; длина сообщения
mov ecx,msg     ; сообщение для вывода на экран
mov ebx,1       ; файловый дескриптор (stdout)
mov eax,4       ; номер системного вызова (sys_write)
int 0x80        ; вызов ядра
>

Здесь [**регистры**](https://ravesli.com/assembler-segmenty-pamyati-i-registry/) `EAX`, `EBX`, `ECX` и `EDX` были использованы при вызове функции `INT 80H`. Таким образом, каждый раз, когда вам нужно вывести строки на экран, вам нужно сохранить эти регистры в [**стеке**](https://ravesli.com/assembler-protsedury/), вызвать `INT 80H` и затем восстановить исходное значение регистров из стека. Поэтому здесь может быть полезно написать два макроса: для сохранения и для восстановления данных.

Некоторые инструкции, такие как `IMUL`, `IDIV`, `INT` и т.д., требуют сохранения некоторой информации в определенных регистрах. Если программа уже использовала эти регистры для хранения важных данных, то существующие данные из этих регистров должны быть сохранены в стеке и восстановлены после выполнения инструкции.

Рассмотрим следующую программу, в которой продемонстрировано определение и использование макросов:


```
; Макрос с двумя параметрами, который реализует системный вызов sys_write

   %macro write_string 2

      mov   eax, 4
      mov   ebx, 1
      mov   ecx, %1
      mov   edx, %2
      int   80h

   %endmacro

section .text

   global _start            ; объявляем для использования gcc

_start:                     ; сообщаем линкеру входную точку

   write_string msg1, len1              
   write_string msg2, len2    
   write_string msg3, len3  
   mov eax,1                ; номер системного вызова (sys_exit)
   int 0x80                 ; вызов ядра

section .data

msg1 db 'Hello, programmers!',0xA,0xD
len1 equ $ - msg1

msg2 db 'Welcome to the world of,', 0xA,0xD
len2 equ $- msg2

msg3 db 'Linux assembly programming! '
len3 equ $- msg3

```

**Результат выполнения программы:

`Hello, programmers!   Welcome to the world of,   Linux assembly programming!`