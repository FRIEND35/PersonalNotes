# Описание

Язык программирования C предоставляет множество стандартных б [[OO. POSIX | POSIX]] течных функций для ввода и вывода файлов. Эти функции составляют большую часть заголовка стандартной библиотеки C. `<stdio.h>`.

Функционал ввода/вывода языка C по современным стандартам довольно низок; C абстрагирует все файловые операции в операции над потоками байтов, которые могут быть «входными потоками» или «выходными потоками». В отличие от некоторых более ранних языков программирования, C не имеет прямой поддержки файлов данных с произвольным доступом; чтобы прочитать из записи в середине файла, программист должен создать поток, перейти к середине файла, а затем последовательно прочитать байты из потока.

Потоковая модель файлового ввода-вывода была популяризирована операционной системой Unix, которая разрабатывалась одновременно с самим языком программирования C. Подавляющее большинство современных операционных систем унаследовали потоки от Unix, а многие языки семейства языков программирования C унаследовали файловый интерфейс ввода-вывода C с небольшими изменениями, если они вообще были изменены (например, PHP). Стандартная библиотека C++ отражает концепцию «потока» в своем синтаксисе; смотрите iostream.

  
Заголовок **stdio.h** определяет три типа переменных, несколько макросов и различные функции для выполнения ввода и вывода.

The `stdio.h` заголовочный файл объявляет функции, которые имеют дело со стандартными ввод и вывод. Одна из этих функций, `fdopen()`, поддерживается только в  [[OO. POSIX | POSIX]] программа.


# Функции stdio.h

Функции, объявленные в `stdio.h`, в общем случае могут быть разделены на две категории: функции для операций с файлами и функции для операций ввода-вывода.


| Имя                    | Примечания                                                                                            |
| ---------------------- | ----------------------------------------------------------------------------------------------------- |
|                        | **Функции для файловых операций**                                                                     |
| fclose                 | закрывает файл, ассоциированный с переданным ей значением FILE *                                      |
| fopen, freopen, fdopen | открывают файл для определённых типов чтения и записи                                                 |
| remove                 | удаляет файл (стирая его)                                                                             |
| rename                 | переименовывает файл                                                                                  |
| rewind                 | работает аналогично fseek (stream, 0L, SEEK_SET), вызванному для потока, со сбросом индикатора ошибок |
| tmpfile                | создает и открывает временный файл, удаляемый при закрытии через fclose()                             |


|          | Функции для операций ввода-вывода                                                                                            |
| -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| clearerr | очищает EOF и индикаторы ошибок для данного потока                                                                           |
| feof     | проверяет, установлен ли индикатор EOF для данного потока                                                                    |
| ferror   | проверяет, установлен ли индикатор ошибок для данного потока                                                                 |
| fflush   | принудительно записывает вывод, предназначенный для помещения в буфер, в файл, ассоциированный с данным потоком              |
| fgetpos  | сохраняет позицию указателя файла потока, ассоциированный с его первым аргументом (FILE *), в его второй аргумент (fpos_t *) |


| gets                        | считывает символы из stdin до символа перевода строки и хранит их в своём единственном аргументе                                                                                                                  |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| printf, vprintf             | используются для вывода в стандартный поток вывода                                                                                                                                                                |
| fprintf, vfprintf           | используются для вывода в файл                                                                                                                                                                                    |
| sprintf, snprintf, vsprintf | используются для вывода в массив типа char (Строка в языке Си)                                                                                                                                                    |
| perror                      | записывает сообщение об ошибке в stderr                                                                                                                                                                           |
| putc                        | записывает и возвращает символ в поток и изменяет указатель позиции файла на него; можно использовать как макрос с теми же свойствами, что и fputc, кроме того, что он может обрабатывать поток более одного раза |
| putchar, fputchar           | аналогичны putc(stdout)                                                                                                                                                                                           |
| scanf, vscanf               | используются для ввода из стандартного потока ввода                                                                                                                                                               |
| fscanf, vfscanf             | используются для ввода из файла                                                                                                                                                                                   |
| sscanf, vsscanf             | используются для ввода из массива char (то есть Строка в языке Си)                                                                                                                                                |
| setbuf                      | указывает буфер, который будет использоваться ука­занным потоком                                                                                                                                                  |
| setvbuf                     | устанавливает режим буферизации для данного потока                                                                                                                                                                |
| tmpnam                      | создает имя временного файла                                                                                                                                                                                      |
| ungetc                      | помещает символ обратно в поток                                                                                                                                                                                   |
| puts                        | выводит символьную строку в stdout                                                                                                                                                                                |

| fgetc   | возвращает один символ из файла                                                                                                                 |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| fgets   | получает строку (оканчивающуюся символом перевода строки или конца файла) из потока (например файла или stdin)                                  |
| fputc   | записывает один символ в поток                                                                                                                  |
| fputs   | записывает строку в поток                                                                                                                       |
| ftell   | возвращает указатель позиции файла, который может быть передан fseek                                                                            |
| fseek   | производит смещение от текущей позиции в файле на указанное количество байт, или от его начала или конца, в указанном направлении.              |
| fsetpos | устанавливает указатель позиции файла потока, ассоциированный с его первым аргументом (FILE *), как хранимый во втором его аргументе (fpos_t *) |

| fread   | читает данные из файла                                                                                                                                                                                            |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| fwrite  | записывает данные в файл                                                                                                                                                                                          |
| getc    | считывает и возвращает символ из данного потока и изменяет указатель позиции файла; позволяет использоваться как макрос с теми же эффектами, что и fgetc, кроме того, что может вычислять поток более одного раза |
| getchar | имеет аналогичный эффект, что и getc(stdin)                                                                                                                                                                       |



# Пример использование:


####  функция printf()
  

Функция библиотеки C **int printf(const char *format, ...)** отправляет форматированный вывод на стандартный вывод. В программировании на языке C `printf()`является одной из основных выходных функций. Функция отправляет форматированный вывод на экран.


**Example 1:** 

```c
#include <stdio.h>    
```

**Output****:**

**C Programming**

**Как работает это программа?**

-   Все допустимые программы C должны содержать `main()` функция. Выполнение кода начинается с начала `main()` функция.
    
-   `printf()`это библиотечная функция для отправки форматированного вывода на экран. Функция печатает строку внутри кавычек.
    
-   Использовать `printf()` в нашей программе нам нужно включить `stdio.h`заголовочный файл с помощью `#include <stdio.h>`утверждение.
    
-   `return 0;` заявление внутри `main()`функция является «статусом выхода» программы. Это необязательно.

  

#### **sprintf() **
  

```c
int sprintf(char *str, const char *string,...); 
```

**str – Где будет сохранятся результат.**
**string – Что будем записывать.**

sprintf означает «печать строк». Вместо того, чтобы печатать на консоли, он сохраняет вывод в буфере char, указанном в sprintf.

**Пример:**

```c
char buffer[80];
char text[] = “Hello World!”;
sprintf(buffer, text);
puts(buffer);
```

_Output:_

**Hello World!**

Мы записали в buffer значение text.

---


## Буферизация

**Буферизация** (от англ. buffer) — метод организации обмена, в частности, ввода и вывода данных в компьютерах и других вычислительных устройствах, который подразумевает использование буфера для временного хранения данных.  

Буферизация потока - это процесс, при котором данные из потока (например, музыкальная или видео информация) временно сохраняются в буфере, прежде чем быть воспроизведенными или использованными. Это позволяет устранить задержки и обеспечить плавное воспроизведение, даже если скорость передачи данных недостаточна для непрерывного воспроизведения. Когда буферизация завершена, данные из буфера передаются в приемник или проигрыватель для отображения или воспроизведения.

Буферизация памяти - это процесс временного хранения данных в специальной области памяти, называемой буфером, перед тем как эти данные будут обработаны или записаны в другое место. Буферизация позволяет ускорить доступ к данным, так как операции чтения или записи в буфер происходят быстрее, чем прямой доступ к основной памяти. Это особенно полезно, когда скорость обработки данных отличается от скорости доступа к памяти. Например, буферизация памяти часто используется при чтении данных с жесткого диска, чтобы уменьшить задержку, связанную с обращением к медленному устройству хранения информации.

Буферизация используется для временного хранения данных или информации в памяти, чтобы облегчить и улучшить процесс обмена данными между различными компонентами системы. Она помогает согласовать скорости передачи данных между быстрыми и медленными устройствами, компенсировать задержки в обработке и снижать нагрузку на систему.
Основные цели буферизации включают:

1. Устранение различий в скорости работы между источником данных и потребителем, позволяя им работать независимо друг от друга.
2. Оптимизация использования ресурсов, уменьшение задержек и улучшение производительности системы.
3. Обеспечение непрерывного потока данных, даже при возникновении временных задержек или скачков в процессе передачи.
4. Обеспечение возможности восстановления данных в случае сбоев или ошибок в процессе передачи.

Буферизация применяется в различных сферах, включая компьютерные сети, мультимедиа, базы данных, операционные системы и другие области, где требуется эффективная передача и обработка данных.

Буферизация - это процесс временного хранения данных в буфере перед их дальнейшей обработкой или передачей. Когда данные поступают в систему, они не обрабатываются немедленно, а сохраняются в буфере. Это позволяет оптимизировать процесс обработки данных и снизить нагрузку на ресурсы.

В случае потоковой передачи данных, буферизация позволяет накапливать данные в буфере до определенного объема или до достижения определенных условий передачи, прежде чем начать их передачу или обработку. Это позволяет уменьшить задержку и улучшить эффективность передачи данных.

Буферы могут использоваться в различных областях, включая сетевые соединения, чтение и запись на диск, обработку видео и аудио, а также в программировании для оптимизации процессов чтения и записи данных.

#### функция setbuf()

Функция setbuf() управляет буферизацией для указанного потока, если операционная система поддерживает пользовательские буферы. Указатель потока должен ссылаться на открытый файл до того, как будут выполнены какие-либо операции ввода-вывода или изменения положения.

```c
void setbuf(FILE *stream, char *buffer)
```

**Параметры**

- **stream** — это указатель на объект FILE, который идентифицирует открытый поток. Параметр stream идентифицирует адрес файлового дескриптора, представляющего собой область памяти, связанную с входным или выходным потоком.
    
- **buffer** — это выделенный пользователем буфер. Он должен иметь длину не менее BUFSIZ байтов, что является константой макроса, используемой в качестве длины этого массива. Укажите указатель на буфер для использования потоком или нулевой указатель, чтобы отключить буфер.
    

**Возвращаемое значение**

Эта функция не возвращает никакого значения.

**Пример**

В следующем примере показано использование функции setbuf().

```c
#include <stdio.h>

int main () {
   char buf[BUFSIZ];

   setbuf(stdout, buf);
   puts("Hello World!");

   fflush(stdout);
   return(0);
}
```

Давайте скомпилируем и запустим вышеуказанную программу, чтобы получить следующий результат. Здесь программа отправляет вывод в STDOUT непосредственно перед тем, как он выйдет, в противном случае он продолжает буферизировать вывод. Вы также можете использовать функцию fflush() для сброса вывода.

```output
Hello World!
```


**Пример 2:**

```c
#include <stdio.h>

int main() {
  char buf[50];

  setbuf(stdout, buf);
  printf("Hello"); //The buffer contains "Hello" //but nothing is written to stdout yet
  fflush(stdout);  //Now "Hello" is written to stdout

  setbuf(stdout, NULL);
  printf(" World!"); //" World!" is written to stdout
  //there is no buffering

  return 0;
}
```

Вывод приведенного выше кода будет:

```output
Hello World!
```


### Функция fflush()

Библиотечная функция C **int fflush(FILE *stream)** очищает выходной буфер потока. fflush() обычно используется только для выходного потока. Его цель — очистить (или сбросить) выходной буфер и переместить буферизованные данные на консоль (в случае stdout) или на диск (в случае файлового потока вывода). Ниже приведен его синтаксис.

**Декларация**

Ниже приведено объявление функции fflush().

```
int fflush(FILE *stream)
```

## Параметры

- **поток** — это указатель на объект FILE, который указывает буферизованный поток.
 

**Возвращаемое значение**

Эта функция возвращает нулевое значение в случае успеха. Если происходит ошибка, возвращается EOF и устанавливается индикатор ошибки (например, feof).

**Пример**

В следующем примере показано использование функции fflush().

```c
#include <stdio.h>
#include <string.h>

int main () {

   char buff[1024];
   
   memset( buff, '\0', sizeof( buff ));
   
   fprintf(stdout, "Going to set full buffering on\n");
   setvbuf(stdout, buff, _IOFBF, 1024);

   fprintf(stdout, "This is tutorialspoint.com\n");
   fprintf(stdout, "This output will go into buff\n");
   fflush( stdout );

   fprintf(stdout, "and this will appear when programm\n");
   fprintf(stdout, "will come after sleeping 5 seconds\n");
   
   sleep(5);
   
   return(0);
}
```

Давайте скомпилируем и запустим вышеуказанную программу, которая даст следующий результат. Здесь программа продолжает буферизовать вывод в **buff** до тех пор, пока не столкнется с первым вызовом **fflush()** , после чего снова начинает буферизировать вывод и, наконец, засыпает на 5 секунд. Он отправляет оставшийся вывод в STDOUT до того, как программа выйдет.

```output
Going to set full buffering on
This is tutorialspoint.com
This output will go into buff
and this will appear when programm
will come after sleeping 5 seconds
```