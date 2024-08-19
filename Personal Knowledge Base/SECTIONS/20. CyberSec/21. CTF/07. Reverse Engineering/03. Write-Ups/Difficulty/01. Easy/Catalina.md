**Платформа:** https://crackmes.one/
**Тип файла**: elf
**Уровень:** Easy

# Walkthrough using Radare2

## Вид снаружи

Запуск файла на нем показывает нам, что он удален. Действительно, запуск nm показывает мы ничто. Запуск crackme сам по себе показывает, как им пользоваться.  Супер. 

## Заглядывая внутрь

Здесь я буду использовать radare2. Crackme удален, но мы все еще можем обратиться к основной функции, так что давайте сделаем это. Вот основная функция:

```
|           0x000015e7      55             push rbp  
│           0x000015e8      4889e5         mov rbp, rsp  
│           0x000015eb      4154           push r12  
│           0x000015ed      53             push rbx  
│           0x000015ee      4881ec000100.  sub rsp, 0x100  
│           0x000015f5      89bdfcfeffff   mov dword [var_104h], edi   ; argc  
│           0x000015fb      4889b5f0feff.  mov qword [s], rsi          ; argv  
│           0x00001602      83bdfcfeffff.  cmp dword [var_104h], 2     ; if argc != 2 then exit
│       ┌─< 0x00001609      7434           je 0x163f                   ; unlikely
│       │   0x0000160b      488d3dee0a00.  lea rdi, str.Welcome_to_crackme_N1 ; 0x2100 ; "Welcome to crackme N1" ; const char *s  
│       │   0x00001612      e819faffff     call sym.imp.puts           ; int puts(const char *s)  
│       │   0x00001617      488b85f0feff.  mov rax, qword [s]  
│       │   0x0000161e      488b00         mov rax, qword [rax]  
│       │   0x00001621      4889c6         mov rsi, rax  
│       │   0x00001624      488d3deb0a00.  lea rdi, str.Usage:_n_s__password__n ; 0x2116 ; "Usage:\n%s <password>\n" ; const char *format  
│       │   0x0000162b      b800000000     mov eax, 0  
│       │   0x00001630      e81bfaffff     call sym.imp.printf         ; int printf(const char *format)  
│       │   0x00001635      b8ffffffff     mov eax, 0xffffffff         ; -1  
│      ┌──< 0x0000163a      e97e020000     jmp 0x18bd                  ; jump to the end of main
```

Если пароль не указан, то напечатайте "Usage" и выйдите, но если пароль указан:

```
│      │└─> 0x0000163f      488d05ea0a00.  lea rax, str.JTQSRyZKSB05Dh9JgH6fQJIVjJ04UpA7ezxMIHcvpX6X70NJHW4xlxSHHMuLDjCJbzl9ITfgeLbTDLExZENyYrAzn7ehjAMuZf1siTB4HBLgyJgpK38LHCq4UvpgqOxeoh72AVgDOYS8HU9xg ; 0x2130 ;  
│      │    0x00001646      488945d8       mov qword [var_28h], rax  
│      │    0x0000164a      c78550ffffff.  mov dword [var_b0h], 4  
│      │    0x00001654      c78554ffffff.  mov dword [var_ach], 4  
│      │    0x0000165e      c78558ffffff.  mov dword [var_a8h], 5  
│      │    0x00001668      c7855cffffff.  mov dword [var_a4h], 4  
│      │    0x00001672      c78560ffffff.  mov dword [var_a0h], 2  
│      │    0x0000167c      c78564ffffff.  mov dword [var_9ch], 4  
│      │    0x00001686      c78568ffffff.  mov dword [var_98h], 3  
│      │    0x00001690      c7856cffffff.  mov dword [var_94h], 4  
│      │    0x0000169a      c78570ffffff.  mov dword [var_90h], 2  
│      │    0x000016a4      c78574ffffff.  mov dword [var_8ch], 4  
│      │    0x000016ae      c78578ffffff.  mov dword [var_88h], 6  
│      │    0x000016b8      c7857cffffff.  mov dword [var_84h], 2  
│      │    0x000016c2      c74580040000.  mov dword [var_80h], 4  
│      │    0x000016c9      c74584060000.  mov dword [var_7ch], 6  
│      │    0x000016d0      c74588020000.  mov dword [var_78h], 2  
│      │    0x000016d7      c7458c050000.  mov dword [var_74h], 5  
│      │    0x000016de      c74590050000.  mov dword [var_70h], 5  
│      │    0x000016e5      c74594020000.  mov dword [var_6ch], 2  
│      │    0x000016ec      c74598030000.  mov dword [var_68h], 3  
│      │    0x000016f3      c7459c030000.  mov dword [var_64h], 3  
│      │    0x000016fa      c745a0050000.  mov dword [var_60h], 5  
│      │    0x00001701      c745a4040000.  mov dword [var_5ch], 4  
│      │    0x00001708      c745a8020000.  mov dword [var_58h], 2  
│      │    0x0000170f      c745ac030000.  mov dword [var_54h], 3  
│      │    0x00001716      c745b0040000.  mov dword [var_50h], 4  
│      │    0x0000171d      c745b4020000.  mov dword [var_4ch], 2  
│      │    0x00001724      c745b8020000.  mov dword [var_48h], 2  
│      │    0x0000172b      c745bc030000.  mov dword [var_44h], 3  
│      │    0x00001732      c745c0030000.  mov dword [var_40h], 3  
│      │    0x00001739      c745c4020000.  mov dword [var_3ch], 2  
│      │    0x00001740      c745c8040000.  mov dword [var_38h], 4  
│      │    0x00001747      c745cc050000.  mov dword [var_34h], 5  
│      │    0x0000174e      48c78520ffff.  mov qword [var_e0h], 0  
│      │    0x00001759      48c78528ffff.  mov qword [var_d8h], 0  
│      │    0x00001764      48c78530ffff.  mov qword [var_d0h], 0  
│      │    0x0000176f      48c78538ffff.  mov qword [var_c8h], 0  
│      │    0x0000177a      c68540ffffff.  mov byte [var_c0h], 0  
│      │    0x00001781      c745ec000000.  mov dword [var_14h], 0  
│      │    0x00001788      c745e8000000.  mov dword [var_18h], 0  
│      │┌─< 0x0000178f      eb32           jmp 0x17c3  
│      ││   ; CODE XREF from main @ 0x17c7(x)  
│     ┌───> 0x00001791      8b45ec         mov eax, dword [var_14h]  
│     ╎││   0x00001794      4863d0         movsxd rdx, eax  
│     ╎││   0x00001797      488b45d8       mov rax, qword [var_28h]  
│     ╎││   0x0000179b      4801d0         add rax, rdx  
│     ╎││   0x0000179e      0fb610         movzx edx, byte [rax]  
│     ╎││   0x000017a1      8b45e8         mov eax, dword [var_18h]  
│     ╎││   0x000017a4      4898           cdqe  
│     ╎││   0x000017a6      88940520ffff.  mov byte [rbp + rax - 0xe0], dl  
│     ╎││   0x000017ad      8b45e8         mov eax, dword [var_18h]  
│     ╎││   0x000017b0      4898           cdqe  
│     ╎││   0x000017b2      8b848550ffff.  mov eax, dword [rbp + rax*4 - 0xb0]  
│     ╎││   0x000017b9      83c001         add eax, 1  
│     ╎││   0x000017bc      0145ec         add dword [var_14h], eax  
│     ╎││   0x000017bf      8345e801       add dword [var_18h], 1  
│     ╎││   ; CODE XREF from main @ 0x178f(x)  
│     ╎│└─> 0x000017c3      837de81f       cmp dword [var_18h], 0x1f  
│     └───< 0x000017c7      7ec8           jle 0x1791  
│      │    0x000017c9      488d8d00ffff.  lea rcx, [var_100h]  
│      │    0x000017d0      488d8520ffff.  lea rax, [var_e0h]  
│      │    0x000017d7      ba20000000     mov edx, 0x20               ; "@" ; signed int64_t arg3  
│      │    0x000017dc      4889ce         mov rsi, rcx                ; int64_t arg2  
│      │    0x000017df      4889c7         mov rdi, rax                ; int64_t arg1  
│      │    0x000017e2      e89bfcffff     call fcn.00001482  
│      │    0x000017e7      c745ec000000.  mov dword [var_14h], 0  
│      │    0x000017ee      c745e4000000.  mov dword [var_1ch], 0  
│      │┌─< 0x000017f5      e994000000     jmp 0x188e  
│      ││   ; CODE XREF from main @ 0x1892(x)  
│     ┌───> 0x000017fa      8b45ec         mov eax, dword [var_14h]  
│     ╎││   0x000017fd      4898           cdqe  
│     ╎││   0x000017ff      0fb6840500ff.  movzx eax, byte [rbp + rax - 0x100]  
│     ╎││   0x00001807      83f041         xor eax, 0x41  
│     ╎││   0x0000180a      89c2           mov edx, eax  
│     ╎││   0x0000180c      8b45ec         mov eax, dword [var_14h]  
│     ╎││   0x0000180f      4898           cdqe  
│     ╎││   0x00001811      88940500ffff.  mov byte [rbp + rax - 0x100], dl  
│     ╎││   0x00001818      8b45ec         mov eax, dword [var_14h]  
│     ╎││   0x0000181b      4898           cdqe  
│     ╎││   0x0000181d      0fb6840500ff.  movzx eax, byte [rbp + rax - 0x100]  
│     ╎││   0x00001825      0fb6d8         movzx ebx, al  
│     ╎││   0x00001828      488b85f0feff.  mov rax, qword [s]  
│     ╎││   0x0000182f      4883c008       add rax, 8  
│     ╎││   0x00001833      4c8b20         mov r12, qword [rax]  
│     ╎││   0x00001836      488b85f0feff.  mov rax, qword [s]  
│     ╎││   0x0000183d      4883c008       add rax, 8  
│     ╎││   0x00001841      488b00         mov rax, qword [rax]  
│     ╎││   0x00001844      4889c7         mov rdi, rax                ; const char *s  
│     ╎││   0x00001847      e8f4f7ffff     call sym.imp.strlen         ; size_t strlen(const char *s)  
│     ╎││   0x0000184c      4889c2         mov rdx, rax  
│     ╎││   0x0000184f      8b45ec         mov eax, dword [var_14h]  
│     ╎││   0x00001852      4898           cdqe  
│     ╎││   0x00001854      4839c2         cmp rdx, rax  
│    ┌────< 0x00001857      7318           jae 0x1871
```

 Цикл просто заполнит массив в rbp-0xe0 (fixed_string) символами взятыми из "longstring" с i-м заданным значением в качестве индекса. Кстати, "longstring" - это:

```
"JTQSRyZKSB05Dh9JgH6fQJIVjJ04UpA7ezxMIHcvpX6X70NJHW4xlxSHHMuLDjCJbzl9ITfgeLbTDLExZENyYrAzn7ehjAMuZf1siTB4HBLgyJgpK38LHCq4UvpgqOxeoh72AVgDOYS8HU9xg"
```

А заданные значения:

```
[4,4,5,4,2,4,3,4,2,4,6,2,4,6,2,5,5,2,3,3,5,4,2,3,4,2,2,3,3,2,4,5]
```

```
│      │    0x000017c9      488d8d00ffff.  lea rcx, [var_100h]  
│      │    0x000017d0      488d8520ffff.  lea rax, [var_e0h]  
│      │    0x000017d7      ba20000000     mov edx, 0x20               ; "@" ; signed int64_t arg3  
│      │    0x000017dc      4889ce         mov rsi, rcx                ; int64_t arg2  
│      │    0x000017df      4889c7         mov rdi, rax                ; int64_t arg1  
│      │    0x000017e2      e89bfcffff     call fcn.00001482  
```

Просто вызовите функцию, которая преобразует fixed_string в какую-нибудь новую строку.  На самом деле нам не нужно знать, что происходит в этой функции, поскольку входные данные статичны, поэтому выходные данные будут одинаковыми каждый раз. Но в любом случае, для любопытных я добавлю в конце asm с комментариями. На самом деле, нам даже не нужно знать, как создаются "fixed_string" или "fixed_output", поскольку каждый раз это будет одно и то же.