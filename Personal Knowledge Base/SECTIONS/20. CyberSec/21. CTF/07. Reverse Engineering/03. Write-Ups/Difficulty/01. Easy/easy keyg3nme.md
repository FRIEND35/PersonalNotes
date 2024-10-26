
**Платформа:** https://crackmes.one/
**Тип файла**: elf
**Уровень:** Easy

**Описание:*** Легко, вам просто нужно понять логику проверки ключа. это должно быть довольно легко даже с уродливым отладчиком. Я здесь новичок, поэтому рейтинг сложности может быть немного неверным.

Примечание. Эта статья не будет рассматривать что-либо подробно, скорее, это всего лишь мой способ решения проблем (в основном вызовов Linux RE).

Задачи Linux RE также потребуют базового понимания ассемблера. Вы можете посмотреть это [**потрясающее 10-минутное видео,**](https://youtu.be/75gBFiFtAb8) чтобы усвоить основные понятия. Ассемблер может показаться вам немного сложным, но вскоре вы полюбите ассемблер ❤.
## Требуемый набор навыков

1. Базовое понимание команд Linux
2. Знакомство со сборкой (x86)
3. Понимание кода C/C++.
4. И, конечно же, Brain.exe и catchy_eyes.exe.
## Необходимые инструменты

### IDA

IDA - IDA (Interactive Disassembler) - это программное обеспечение для обратной разработки и анализа программного кода. Оно позволяет анализировать исполняемые файлы и исследовать их структуру, функции, алгоритмы и другие аспекты. IDA позволяет дизассемблировать машинный код и предоставляет различные инструменты для работы с ним, такие как проверка переходов, аннотации, создание графов потока управления и т.д. IDA является широко используемым инструментом при анализе и реверс-инжиниринге программного обеспечения.
### [Ghidra](https://github.com/NationalSecurityAgency/ghidra)

Ghidra — это платформа обратного проектирования программного обеспечения (SRE), созданная и поддерживаемая Исследовательским управлением [**Агентства национальной безопасности**](https://www.nsa.gov/) . Эта платформа включает в себя набор полнофункциональных высококачественных инструментов анализа программного обеспечения, которые позволяют пользователям анализировать скомпилированный код на различных платформах, включая Windows, macOS и Linux.
### [Radare2](https://github.com/radareorg/radare2)

**Radare2** (также известный как **r2** ) — это полноценная [**платформа**](https://en.wikipedia.org/wiki/Framework_(software)) для [**обратного проектирования**](https://en.wikipedia.org/wiki/Reverse-engineering) и анализа двоичных файлов; состоит из набора небольших утилит, которые можно использовать вместе или независимо из [**командной строки.**](https://en.wikipedia.org/wiki/Command_line)

**Интересный факт** : Radare2 тоже появился в **Mr.Robot** , я имею в виду, разве это не круто?

# Начало работы

Вы можете скачать этот файл отсюда [(](https://crackmes.one/static/crackme/5da31ebc33c5d46f00e2c661.zip) пароль: crackmes.one). После распаковки загруженного zip-файла вы увидите файл с именем «keyg3nme». Сейчас мы понятия не имеем, что это за файл, поэтому давайте запустим команду **file** для данного файла.

Команда **file** используется для определения типа файла. Тип **_файла .file_** может быть удобочитаемым (например, «текст ASCII») или типом MIME (например, «текст/обычный; charset=us-ascii»). Эта команда проверяет каждый аргумент, пытаясь классифицировать его.

[Подробнее о команде file: [https://www.geeksforgeeks.org/file-command-in-linux-with-examples/]](https://www.geeksforgeeks.org/file-command-in-linux-with-examples/)

Вывод команды файла:

![[Pasted image 20240518190829.png]]

Из команды **file** ясно, что **keyg3nme** — это 64-битный исполняемый файл ELF (не удаленный). Давайте запустим этот двоичный файл.

![[Pasted image 20240518190948.png]]

При запуске этого двоичного файла нас просят ввести ключ, и, очевидно, мы не знаем правильный ключ, и при вводе любого случайного ключа мы получаем сообщение «нет». Наша цель здесь — найти правильный ключ. Давайте запустим команду **strings** , чтобы найти строки, которые можно распечатать, в этом двоичном файле.

![[Pasted image 20240518191005.png]]

Я нашел несколько интересных строк:

1. **Enter your key :**
2. **Good job mate, now go keygen me** - это отобразится, когда пользователь введет правильный ключ
3. **nope** - это будет отображаться, когда пользователь введет неверный ключ

Но, к сожалению, в двоичном файле нет ни **жестко запрограммированного ключа , ни каких-либо функций strcmp.

**Интересный факт**: проблемы CTF касаются не только`strings challfile | grep flag`

Давайте откроем этот файл в **Ghidra** для декомпиляции и анализа определений функций. Можно так же использовать  **IDA**, **Cutter** или же **Ghidra**, что вам удобнее.

Найдите **main** функцию и начните анализировать функцию **main**.

**Примечание**. Поскольку это первая задача в этой серии, поэтому я анализирую декомпилированный код C, в дальнейших задачах я могу напрямую анализировать ассемблерный код (с использованием radare2).

Во время работы у меня возникла идея, решить задачу с **IDA** и **Ghidra** для того чтобы понять какой из инструментов более удобный, и который из них выбрать.

# Дизассемблирования



# Декомпиляция

## IDA decompiler

Легче читать код с синтаксисом языка Си чем ассемблер. Именно поэтому давайте мы сразу декомпилируем код с п.м. **IDA** для анализа. При декомпиляции получаем вот такой код:

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  unsigned int v4; // [rsp+4h] [rbp-Ch] BYREF
  unsigned __int64 v5; // [rsp+8h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  printf("Enter your key:  ");
  __isoc99_scanf("%d", &v4);
  if ( (unsigned int)validate_key(v4) == 1 )
    puts("Good job mate, now go keygen me.");
  else
    puts("nope.");
  return 0;
}
```

Давайте разберем его по частям и объясним, что он делает.
### Разбор кода 

#### 1. Объявление функции main:

```c
int __fastcall main(int argc, const char **argv, const char **envp)
```

Функция `main` является точкой входа в программу. Она принимает три параметра: количество аргументов командной строки (`argc`), массив указателей на аргументы (`argv`) и массив указателей на переменные окружения (`envp`).  Ключевое слово `__fastcall` указывает на использование определенного соглашения о вызовах, при котором аргументы передаются через регистры для ускорения выполнения. 
#### 2. Объявление переменных:

```c
unsigned int v4; // [rsp+4h] [rbp-Ch] BYREF 
unsigned __int64 v5; // [rsp+8h] [rbp-8h]
```

Объявлены две переменные:  `v4` (целое число без знака) и `v5` (64-битное целое число без знака).
#### 3. Считывание значения из специального регистра:

```c
v5 = __readfsqword(0x28u);
```

Эта строка читает значение из специального регистра `fs` по смещению `0x28` и сохраняет его в `v5`. Это часто используется для получения адреса структуры данных, связанной с потоком, такой как блок управления потоком (TCB) в системах на базе Windows.
#### 4. Запрос ввода ключа:

```c
printf("Enter your key: ");
__isoc99_scanf("%d", &v4);
```

Программа выводит сообщение "Enter your key:" и ожидает ввода целого числа, которое сохраняется в переменную `v4`.
#### 5. Валидация ключа:

```c
if ( (unsigned int)validate_key(v4) == 1 ) 
    puts("Good job mate, now go keygen me."); 
else 
    puts("nope.");
```

Введенное значение передается функции `validate_key`, которая возвращает целое число. Если результат равен `1`, выводится сообщение "Good job mate, now go keygen me.". В противном случае выводится "nope.".
##### Что такое **validate_key** ?

Функция `validate_key` упоминается, но ее код мы не анализировали. Эта функция, вероятно, проверяет корректность введенного ключа по каким-то критериям. Без ее кода мы не можем точно сказать, как именно происходит валидация.
##### Разбор функции validate_key

```c
_BOOL8 __fastcall validate_key(int a1)
{
  return a1 % 1223 == 0;
}
```

Функция `validate_key` проверяет, делится ли введенный ключ на 1223 без остатка. Если ключ делится на 1223, функция возвращает истинное значение (true), иначе ложное (false). Это очень простая проверка, которая может использоваться в учебных или тестовых целях.

1. a1 % 1223: Оператор % выполняет операцию вычисления остатка от деления. Он возвращает остаток, который остается, если a1 делится на 1223.

2. == 0: Это выражение проверяет, равен ли остаток нулю. Если остаток равен нулю, значит, a1 кратно 1223.


```
Операция деления по модулю (также известная как операция взятия остатка от деления) в программировании возвращает остаток от деления двух чисел. Это означает, что результатом деления по модулю будет остаток, который остается после того, как одно число было разделено на другое.

В большинстве языков программирования операция деления по модулю обозначается символом "%" (например, a % b). Например, если мы выполним деление по модулю 10 % 3, то результат будет 1, так как остаток от деления числа 10 на число 3 равен 1. 

Операция деления по модулю часто используется в программировании для проверки четности или нечетности числа, вычисления дней недели, циклического изменения значений и других задач.
```
#### 6. Завершение программы:

```c
return 0;
```

Функция `main` завершает выполнение и возвращает `0`, что обычно означает успешное завершение программы.
#### Полный разбор кода

Теперь, когда у нас есть определение функции `validate_key`, мы можем собрать весь код вместе и объяснить его.
#### Код программы:

```c
#include <stdio.h>
#include <stdlib.h>

// Функция validate_key проверяет, делится ли число a1 на 1223 без остатка
_BOOL8 __fastcall validate_key(int a1) {
    return a1 % 1223 == 0;
}

int __fastcall main(int argc, const char **argv, const char **envp) {
    unsigned int v4; // Переменная для хранения введенного ключа

    printf("Enter your key:  ");
    scanf("%d", &v4) );  // Считывание целого числа
    
    // Проверка введенного ключа
    if (validate_key(v4)) {
        puts("Good job mate, now go keygen me."); // Сообщение при успешной проверке
    } else {
        puts("nope."); // Сообщение при неудачной проверке
    }

    return 0; // Завершение программы
}
```

### Объяснение работы программы

1. **Ввод и проверка ключа**: Программа выводит сообщение "Enter your key: " и ожидает ввода целого числа пользователем. Введенное число сохраняется в переменной `v4`.
    
2. **Валидация ключа**: Введенное число передается функции `validate_key`, которая проверяет, делится ли число на 1223 без остатка. Если делится, функция возвращает истину (true), иначе ложь (false).
    
3. **Вывод результата**: Если `validate_key` возвращает истину, программа выводит "Good job mate, now go keygen me.". В противном случае выводится "nope.".
    
### Пример работы

- Если пользователь введет `2446`, программа выведет "Good job mate, now go keygen me.", потому что 2446 делится на 1223 (2446 / 1223 = 2).
- Если пользователь введет любое число, которое не делится на 1223, например, `1234`, программа выведет "nope.".
### Резюме

Код стал более безопасным и устойчивым к некорректному вводу. Мы также узнали, что функция `validate_key` проверяет кратность числа 1223. В результате весь процесс проверки ключа стал прозрачным и понятным.

---

## Ghidra decompiler

Давайте декомпилируем с п.м. Ghidra:

```c
undefined8 main(void)

{
  int iVar1;
  long in_FS_OFFSET;
  undefined4 local_14;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  printf("Enter your key:  ");
  __isoc99_scanf(&DAT_0010201a,&local_14);
  iVar1 = validate_key(local_14);
  if (iVar1 == 1) {
    puts("Good job mate, now go keygen me.");
  }
  else {
    puts("nope.");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```

Как можно понять у Ghidra код чуть более развернутый по сравнению с IDA. Декомпилятор IDA более завернутый и компактый, а у Ghidra наоборот.
### Разбор кода

#### 1. Объявление функции main

```c
undefined8 main(void)
```

Функция `main` является точкой входа в программу. Тип возвращаемого значения `undefined8` указывает на 64-битное целое число (аналогично `uint64_t` или `unsigned long long`).
#### 2. Объявление переменных

```c
int iVar1;
long in_FS_OFFSET;
undefined4 local_14;
long local_10;
```

- `iVar1`: Целочисленная переменная для хранения результата вызова функции `validate_key`.
- `in_FS_OFFSET`: Переменная, используемая для работы с регистром `FS`, специфичным для архитектуры x86-64.
- `local_14`: 32-битная переменная (аналогична `int`), используемая для хранения введенного ключа.
- `local_10`: 64-битная переменная (аналогична `long`), используемая для хранения значения, считываемого из регистра `FS`.
#### 3. Инициализация переменной **local_10**

```c
local_10 = *(long *)(in_FS_OFFSET + 0x28);
```

Значение по адресу `in_FS_OFFSET + 0x28` (обычно указатель на текущую структуру управления потоком, такую как TCB) считывается и сохраняется в `local_10`.
#### 4. Ввод ключа

```c
printf("Enter your key:  ");
__isoc99_scanf(&DAT_0010201a, &local_14);
```

Эти строки кода управляют вводом ключа пользователем. Программа выводит сообщение "Enter your key: " и ожидает ввода целого числа, которое сохраняется в `local_14`. Форматная строка `&DAT_0010201a` скорее всего указывает на строку формата **"%d"**.

Функция `__isoc99_scanf` является вариантом стандартной функции `scanf` из библиотеки C, используемой для считывания форматированного ввода. Префикс `__isoc99` указывает на то, что эта функция совместима с C99 стандартом. В данном контексте она используется для считывания ввода пользователя и сохранения его в переменной `local_14`.
##### Анализ строки

```c
__isoc99_scanf(&DAT_0010201a, &local_14);
```
###### Разбор аргументов

1. `&DAT_0010201a`:
    
    - Это строка формата, используемая функцией `scanf` для интерпретации ввода.
    - Судя по названию, `DAT_0010201a` это глобальная переменная, содержащая строку формата.
    - Обычно строка формата для целого числа это `"%d"` или `"%u"`, если предполагается вводить только положительные числа.

2. `&local_14`:
    
    - Это указатель на переменную, в которую будет сохранено значение, введенное пользователем.
    - В данном случае `local_14` объявлена как `undefined4`, что соответствует 32-битному целому числу.
###### Пример строки формата

Предположим, что `DAT_0010201a` определена как строка формата для целого числа:

```c
const char DAT_0010201a[] = "%d"; // Определение строки формата
```
###### Вызов **scanf**

Функция `__isoc99_scanf` с этим форматом и указателем на переменную `local_14` работает так же, как стандартная `scanf`:

```c
__isoc99_scanf("%d", &local_14);
```

Эта строка кода делает следующее:

1. Ожидает ввода пользователя.
2. Интерпретирует ввод как целое число согласно строке формата `"%d"`.
3. Сохраняет введенное значение в переменной `local_14`.
#### 5. Валидация ключа

```c
iVar1 = validate_key(local_14);
if (iVar1 == 1) {
    puts("Good job mate, now go keygen me.");
} else {
    puts("nope.");
}
```

Функция `validate_key` проверяет ключ и возвращает результат, который используется для определения вывода сообщения пользователю.

Функция `validate_key` вызывается с аргументом `local_14`. Если функция возвращает 1, программа выводит "Good job mate, now go keygen me.". В противном случае выводится "nope.". 
##### Разбор функции validate_key

Для полной картины приведем определение функции `validate_key`, предположительно. Ghidra картину показывает вот так:

```c
bool validate_key(int param_1)
{
  return param_1 % 0x4c7 == 0;
}
```

Этот код представляет функцию `validate_key`, которая принимает целочисленное значение key в качестве аргумента и возвращает булево значение (true/false). В данном случае, функция возвращает true, если остаток от деления ключа на 1223 равен 0, иначе она возвращает false. Это означает, что функция проверяет является ли ключ кратным 1223 или нет.

Например, если вы вызываете функцию `validate_key(1223)`, она вернет true, так как 1223 делится на 1223 без остатка. Если вы вызовете функцию с другим значением, которое не является кратным 1223, то она вернет false.
#### 6. Проверка целостности стека

```c
if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
    __stack_chk_fail();
}
```

Эти строки кода обеспечивают проверку целостности стека для защиты от переполнения. После основной логики программы, происходит проверка значения `local_10` с текущим значением по адресу `in_FS_OFFSET + 0x28`. Эта проверка используется для обнаружения переполнения стека. Если значения не совпадают, вызывается функция `__stack_chk_fail`, которая обычно завершает программу аварийно.

#### 7. Возвращение значения

```c
return 0;
```

Функция завершает выполнение и возвращает 0. Функция `main` возвращает 0, что указывает на успешное завершение программы.

#### Полный пример

Для лучшего понимания представим полный контекст:

```c
#include <stdio.h>
#include <stdlib.h>

int validate_key(int key) {
    return key % 1223 == 0;
}

int main(void) {
    int iVar1;
    long in_FS_OFFSET;
    int local_14; // 32-битная переменная для хранения ключа
    long local_10;
  
    // Симуляция чтения из специального регистра для проверки целостности стека
    in_FS_OFFSET = 0;
    local_10 = *(long *)(in_FS_OFFSET + 0x28);
  
    // Вывод запроса на ввод ключа
    printf("Enter your key:  ");
  
    // Считывание введенного ключа и сохранение его в local_14
    __isoc99_scanf("%d", &local_14);
  
    // Валидация введенного ключа
    iVar1 = validate_key(local_14);
    if (iVar1 == 1) {
        puts("Good job mate, now go keygen me.");
    } else {
        puts("nope.");
    }
  
    // Проверка целостности стека
    if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
        __stack_chk_fail();
    }
  
    // Завершение программы
    return 0;
}
```

### Итоговое объяснение каждой переменной и их назначения

- `iVar1`: Переменная для хранения результата вызова функции `validate_key`, используется в условной проверке.
- `in_FS_OFFSET`: Переменная, используемая для работы с регистром `FS`, специфична для архитектуры x86-64.
- `local_14`: Переменная для хранения введенного пользователем ключа.
- `local_10`: Переменная для хранения значения, считываемого из регистра `FS`, используемая для проверки целостности стека.

Код запрашивает у пользователя ввод ключа, проверяет его с помощью функции `validate_key`, выводит сообщение в зависимости от результата проверки и выполняет проверку целостности стека для защиты от переполнения.

### Резюме

- `__isoc99_scanf(&DAT_0010201a, &local_14);` использует строку формата, хранящуюся в `DAT_0010201a`, для считывания целого числа из ввода и сохранения его в `local_14`.
- Строка формата, скорее всего, содержит `"%d"`, чтобы считывать целое число.
- Переменная `local_14` затем используется для проверки в функции `validate_key`.

И паролем является любое число которое делится на число 1223 без остатка.
## Заключение 

Основные различия между декомпиляцией IDA и Ghidra включают следующее:

1. Лицензия и стоимость: Ghidra - бесплатный и открытый исходный код инструмент, который разрабатывается Национальным центром кибербезопасности США. IDA, с другой стороны, является коммерческим продуктом от Hex-Rays, и требует платную лицензию для полного доступа ко всем функциям.

2. Удобство использования: IDA Pro считается более удобным и пользовательским приложением, благодаря своему долгому сроку разработки и широкому распространению. Ghidra, тем не менее, становится все более популярным благодаря своим мощным функциям и обновлениям.

3. Функциональность: Оба инструмента предлагают схожие возможности для декомпиляции, но могут иметь различия в точности результатов и поддержке различных архитектур процессора.

4. Сообщество и поддержка: Ghidra имеет активное сообщество разработчиков и пользователей, которые делают его лучше, а также предоставляют различные плагины. IDA Pro также имеет широкое сообщество, но сторонние плагины и ресурсы могут быть ограничены в сравнении с Ghidra.

Таким образом, выбор между IDA и Ghidra будет зависеть от ваших предпочтений, потребностей и бюджета. Оба инструмента обладают мощными функциями для реверс-инжиниринга программного обеспечения и могут быть полезны в различных сценариях.

