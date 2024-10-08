# Описание

  
```
Заголовок _<signal.h>_ должен определять следующие макросы, которые 
        должны расширяться до постоянных выражений с различными значениями, которые 
        иметь тип, совместимый со вторым аргументом, и 
        возвращаемое значение функции _signal_ (), и чьи значения должны 
        сравните unequal с адресом любой объявляемой функции. 

        SIG_DFL Запрос на обработку сигнала по умолчанию. 

        SIG_ERR Возвращает значение из _signal_ () в случае ошибки. 

        SIG_HOLD Запрос удержания сигнала. 

        SIG_IGN Запрос на игнорирование сигнала. 

        Заголовок _<signal.h>_ должен определять **pthread_t** , **size_t** и 
        **uid_t** , как описано в _<sys/типы.h>_ . 

        Заголовок _<signal.h>_ должен определять **timespec** как 
        описано в _<time.h>_ . 

        Заголовок _<signal.h>_ должен определять следующие типы данных: 

        **sig_atomic_t** Возможно целочисленный тип с указанием volatile 
                      объект, к которому можно получить доступ как к атомарной сущности, 
                      даже при наличии асинхронных прерываний. 

        **sigset_t** Целочисленный или структурный тип объекта, используемый для 
                      представлять наборы сигналов. 

        **pid_t** Как описано в _<sys/types.h>_ . 

        Заголовок _<signal.h>_ должен определять **pthread_attr_t** как 
        описано в _<sys/types.h>_ . 

        Заголовок _<signal.h>_ должен определять **sigevent** , которая 
        должен включать как минимум следующих членов: 

            int sigev_notify Тип уведомления. 
            int sigev_signo Номер сигнала. 
            union sigval sigev_value Значение сигнала. 
            void (*sigev_notify_function)(союзный сигнал) 
                                                     Функция уведомления. 
            pthread_attr_t *sigev_notify_attributes Атрибуты уведомлений. 

         _<signal.h>_ должен определять следующие символические 
        константы для значений _sigev_notify_ : 

        SIGEV_NONE Асинхронное уведомление не доставляется, когда 
                      происходит интересное событие. 

        SIGEV_SIGNAL Сигнал в очереди со значением, определяемым приложением, 
                      генерируется, когда происходит интересующее событие. 

        SIGEV_THREAD Функция уведомления вызывается для выполнения 
                      уведомление. 

        Сигвал **-** объединение определяется как: 

            int sival_int Целочисленное значение сигнала. 
            void *sival_ptr Значение сигнала указателя. 

        Заголовок _<signal.h>_ должен объявлять SIGRTMIN и SIGRTMAX. 
        макросы, которые должны расширяться до положительных целочисленных выражений с 
        тип **int** , но необязательно должны быть константными выражениями. Эти 
        макросы задают диапазон номеров сигналов, которые зарезервированы для 
        использование приложения и для которого поведение сигнала в реальном времени 
        указанный в этом томе POSIX.1‐2017, поддерживается. Сигнал 
        числа в этом диапазоне не перекрываются ни с одним из указанных сигналов 
        в следующей таблице. 

        Диапазон от SIGRTMIN до SIGRTMAX включительно должен включать 
        наименьшее количество сигналов {RTSIG_MAX}. 

        Реализация определяет, является ли поведение сигнала в реальном времени 
        поддерживается для других сигналов. 

         _<signal.h>_ должен определять следующие макросы, которые 
        используется для обозначения сигналов, которые возникают в системе. Сигналы 
        определенные здесь, начинаются с букв SIG, за которыми следует заглавная буква 
        письмо. Макросы должны расширяться до положительной целочисленной константы 
        выражения с типом **int** и различными значениями. Значение 0 
        зарезервирован для использования в качестве нулевого сигнала (см. _kill_ ()). Дополнительный 
        в системе могут возникать сигналы, определяемые реализацией. 

        Стандарт ISO C требует только имена сигналов SIGABRT, 
        SIGFPE, SIGILL, SIGINT, SIGSEGV и SIGTERM должны быть определены. Ан 
        реализация не должна генерировать ни один из этих шести сигналов, кроме 
        в результате явного использования интерфейсов, генерирующих сигналы, 
        такие как _поднять_ (), _убить_ (), общий терминальный интерфейс (см. 
        _Раздел 11.1.9_ , _Специальные символы_ ), и _kill_ утилита 
        не указано иное (см., например, том System Interfaces 
        POSIX.1-2017, _раздел 2.8.3.3_ , _защита памяти_ ). 

        Следующие сигналы должны поддерживаться во всех реализациях 
        (действия по умолчанию описаны ниже в таблице):

```



| Сигнал     умолчанию  Действие по  Описание                    |     | 
| -------------------------------------------------------------- | --- |
| SIGABRT Сигнал прерывания процесса.                            |     |
| SIGALRM T Будильник.                                           |     |
| SIGBUS Доступ к неопределенной части                           |     |
| объект памяти.                                                 |     |
| SIGCHLD I Дочерний процесс завершен, остановлен,               |     |
| или продолжение.                                               |     |
| SIGCONT C Продолжить выполнение, если оно остановлено.         |     |
| SIGFPE A Ошибочная арифметическая операция.                    |     |
| SIGHUP T Отбой.                                                |     |
| SIGILL A Недопустимая инструкция.                              |     |
| SIGINT T Сигнал прерывания терминала.                          |     |
| SIGKILL T Kill (не может быть пойман или проигнорирован).      |     |
| SIGPIPE T Пишите в трубу так, чтобы никто не читал.            |     |
| SIGQUIT Сигнал выхода терминала.                               |     |
| SIGSEGV Недопустимая ссылка на память.                         |     |
| SIGSTOP S Остановить выполнение (не может быть перехвачено или |     |
| игнорируется).                                                 |     |
| SIGTERM T Сигнал завершения.                                   |     |
| SIGTSTP S Сигнал остановки терминала.                          |     |
| SIGTTIN S Фоновый процесс пытается прочитать.                  |     |
| SIGTTOU S Фоновый процесс пытается выполнить запись.           |     |
| SIGUSR1 T Пользовательский сигнал 1.                           |     |
| SIGUSR2 T Пользовательский сигнал 2.                           |     |
| SIGPOLL T Опрашиваемое событие.                                |     |
| SIGPROF T Таймер профилирования истек.                         |     |
| SIGSYS Неверный системный вызов.                               |     |
| SIGTRAP Ловушка трассировки/точки останова.                    |     |
| SIGURG I Высокоскоростные данные доступны    разъем.                   |     |
| SIGVTALRM T Срок действия виртуального таймера истек.          |     |
| SIGXCPU Превышен предел времени процессора.                    |     |
| SIGXFSZ Превышен предельный размер файла.                      |     |

 Действия по умолчанию следующие: 
```

        T Аварийное завершение процесса. Процесс завершается со всеми 
               последствия **_** exit (), за исключением того, что статус доступен для ожидания () и 
               waitpid () указывает на ненормальное завершение по указанному сигналу. 

        Аварийное завершение процесса. 
               Кроме того, определяемые реализацией аварийные действия завершения, такие как создание 
               основного **.** файла, может произойти 

        Я игнорирую сигнал. 

        S Остановить процесс. 

        C Продолжить процесс, если он остановлен; в противном случае игнорируйте сигнал. 

        Заголовок должен содержать объявление **struct **  **sigaction** , включая по крайней мере 
        следующие участники: 

               **void ** **(*sa_handler)(int)** Указатель на функцию перехвата сигнала или один из макросов 
                                        SIG_IGN или SIG_DFL. 
               **sigset_t ** **sa_mask** Набор сигналов, которые будут заблокированы во время исполнения сигнала 
                                        функция обработки. 
               **int **      **sa_flags** Специальные флаги. 
               **недействительным ** **(*sa_sigaction) (целое, ** **siginfo_t ** ***, ** **пустота ** ***)** Указатель на функцию захвата сигнала. 

        , занимаемая sa_handler и sa_sigaction , может перекрываться, и соответствующий 
        приложение не должно использовать оба одновременно. 

        Следующее должно быть объявлено как константы: 

        SA_NOCLDSTOP 
               Не генерировать SIGCHLD, когда дети останавливаются 
               или остановились дети продолжают. 

        SIG_BLOCK 
               Результирующий набор представляет собой объединение текущего набора и набора сигналов, на который указывает 
               аргументов набор . 

        SIG_UNBLOCK 
               Результирующее множество является пересечением текущего множества и дополнения 
               аргументов набор . 

        SIG_SETMASK 
               Результирующий набор является набором сигналов, на который указывает набор . 

        SA_ONSTACK 
               Вызывает доставку сигнала в альтернативный стек. 

        SA_RESETHAND 
               Приводит к установке расположения сигналов в SIG_DFL при входе в обработчики сигналов. 

        SA_RESTART 
               Делает некоторые функции перезапускаемыми. 

        SA_SIGINFO 
               Вызывает передачу дополнительной информации обработчикам сигналов во время получения 
               сигнал. 

        SA_NOCLDWAIT 
               Заставляет реализации не создавать зомби-процессы после смерти ребенка. 

        SA_NODEFER 
               Заставляет сигнал не блокироваться автоматически при входе в обработчик сигнала. 

        SS_ONSTACK 
               Процесс выполняется на альтернативном стеке сигналов. 

        SS_DISABLE 
               Альтернативный стек сигналов отключен. 

        МИНСИГСТКСЗ 
               Минимальный размер стека для обработчика сигнала. 

        СИГСТКСЗ 
               Размер по умолчанию в байтах для альтернативного стека сигналов. 

         **ucontext_t** должна быть определена через **typedef** , как описано в <ucontext.h> . 

        Тип **mcontext_t** должен быть определен через **typedef** , как описано в <ucontext.h> . 

        Заголовок <signal.h> должен определять **stack_t** как структуру, включающую как минимум 
        следующие члены: 

               **void **     ***ss_sp** База стека или указатель. 
               **size_t **    **ss_size** Размер стека. 
               **int **       **ss_flags** Флаги. 

        Заголовок <signal.h> должен определять **sigstack** , которая включает как минимум 
        следующие участники: 

               **int **       **ss_onstack** Ненулевое значение, когда используется стек сигналов. 
               **void **     ***ss_sp** Указатель стека сигналов. 

        Заголовок <signal.h> должен определять **siginfo_t** как структуру, которая включает в себя 
        как минимум следующие члены: 

               **int **           **si_signo Номер** сигнала. 

               **int **           **si_errno** Если не ноль, errno , связанное с 
                                       этот сигнал, как определено в **<errno.h>.** 

              **int **           **si_code** Код сигнала. 

               **pid_t **         **si_pid Идентификатор** отправляющего процесса. 
               **uid_t **         **si_uid Идентификатор** реального пользователя отправляющего процесса. 
               **void **         ***si_addr** Адрес ошибочной инструкции. 
               **int **           **si_status** Выходное значение или сигнал. 
               **long **          **si_band** Событие диапазона для SIGPOLL. 

               **union ** **sigval **  **si_value** Значение сигнала. 

        Макросы, указанные в **Код** столбце 
        значения si_code , которые являются специфическими или неспецифическими для сигнала причинами, по которым сигнал 
        был сгенерирован. 

                    **Сигнал **    **Код **            **Причина** SIGILL ILL_ILLOPC Недопустимый код операции. 
                              ILL_ILLOPN Недопустимый операнд. 
                              ILL_ILLADR Недопустимый режим адресации. 

                              ILL_ILLTRP Недопустимая ловушка. 
                              ILL_PRVOPC Привилегированный код операции. 
                              ILL_PRVREG Привилегированный регистр. 
                              ILL_COPROC Ошибка сопроцессора. 
                              ILL_BADSTK Внутренняя ошибка стека. 
                    SIGFPE FPE_INTDIV Целочисленное деление на ноль. 
                              FPE_INTOVF Целочисленное переполнение. 
                              FPE_FLTDIV Деление числа с плавающей запятой на ноль. 
                              FPE_FLTOVF Переполнение с плавающей запятой. 
                              FPE_FLTUND Потеря значимости с плавающей запятой. 
                              FPE_FLTRES Неточный результат с плавающей запятой. 
                              FPE_FLTINV Недопустимая операция с плавающей запятой. 
                              Индекс FPE_FLTSUB вне допустимого диапазона. 
                    SIGSEGV SEGV_MAPERR Адрес не сопоставлен с объектом. 
                              SEGV_ACCERR Недопустимые разрешения для сопоставленного объекта. 
                    SIGBUS BUS_ADRALN Неверное выравнивание адреса. 
                              BUS_ADRERR Несуществующий физический адрес. 
                              BUS_OBJERR Аппаратная ошибка объекта. 
                    SIGTRAP TRAP_BRKPT Точка останова процесса. 
                              TRAP_TRACE Ловушка трассировки процесса. 
                    SIGCHLD CLD_EXITED Ребенок вышел. 
                              CLD_KILLED Ребенок аварийно завершил работу и сделал 
                                              не создавать **основной** файл. 
                              CLD_DUMPED Ребенок аварийно завершил работу и 
                                              создал **основной** файл. 
                              CLD_TRAPPED Прослеженный дочерний элемент попал в ловушку. 
                              CLD_STOPPED Ребенок остановлен. 
                              CLD_CONTINUED Остановленный дочерний процесс продолжается. 
                    SIGPOLL POLL_IN Доступен ввод данных. 
                              Доступны выходные буферы POLL_OUT. 
                              POLL_MSG Доступно входное сообщение. 
                              POLL_ERR Ошибка ввода-вывода. 
                              POLL_PRI Доступен ввод с высоким приоритетом. 
                              POLL_HUP Устройство отключено. 
                    Любой сигнал SI_USER, отправленный функцией kill (). 
                              SI_QUEUE Сигнал, отправленный sigqueue (). 
                              SI_TIMER Сигнал, генерируемый по истечении 
                                              таймер установлен таймер_установить время (). 
                              SI_ASYNCIO Сигнал, генерируемый завершением 
                                              асинхронный запрос ввода-вывода. 
                              SI_MESGQ Сигнал, генерируемый при поступлении сообщения 
                                              в пустой очереди сообщений. 

        Реализации могут поддерживать дополнительные si_code , не включенные в этот список, могут 
        генерировать значения, включенные в этот список, при обстоятельствах, отличных от описанных в 
        этот список и может содержать расширения или ограничения, препятствующие тому, чтобы некоторые значения 
        сгенерировано. Реализации не генерируют значения, отличные от описанных в 
        этот список для обстоятельств, описанных в этом списке. 

        Кроме того, должна быть доступна следующая специфичная для сигнала информация: 

                 **сигнала **  **члена **         **Значение** SIGILL **void ** *** ** si_addr  Адрес  ошибочной  инструкции  . 
                SIGFPE 
                SIGSEGV  **void ** *** ** si_addr  Адрес  _  ошибки  память  ссылка на 
                SIGBUS 
                SIGCHLD  **pid_t ** si_pid    дочернего  процесса  . 
                        **int ** si_status   Выходное  значение  или  сигнал. 
                        **uid_t ** si_uid    реального  пользователя  Идентификатор  _  _  процесса  ,  отправившего  сигнал  . 
                SIGPOLL  **long ** si_band    диапазона  Событие  для  POLL_IN,  POLL_OUT  или  POLL_MSG. Для некоторых реализаций значение si_addr может быть неточным. 

        Следующее должно быть объявлено как функции, а также может быть определено как макрос: 

               **недействительным ** **(* bsd_signal (int, ** **недействительным ** **(*) (int))) (int);** 

              **) **    **интервал убить (pid_t, интервал ** **;** 

              **int **    **killpg(pid_t, ** **int);** 

              **int **    **pthread_kill(pthread_t, ** **int);** 
              **int **    **pthread_sigmask(int, ** **const ** **sigset_t ** ***, ** **sigset_t ** ***);** 

              **инт **    **поднять (инт);** 

              **int **    **sigaction(int, ** **const ** **struct ** **sigaction ** ***restrict,** 
                         **struct ** **sigaction ** ***restrict);** 
              **int **    **sigaddset(sigset_t ** ***, ** **int);** 

              **int **    **sigaltstack (const ** **stack_t ** ***restrict, ** **stack_t ** ***restrict);** 

              **int **    **sigdelset(sigset_t ** ***, ** **int);** 
              **int **    **sigemptyset(sigset_t ** ***);** 
              **int **    **sigfillset(sigset_t ** ***);** 

              **инт **    **вздох (инт);** 
              **инт **    **сигигнор (инт);** 
              **int **    **siginterrupt(int, ** **int);** 

              **int **    **sigismember (const ** **sigset_t ** ***, ** **int);** 

              **недействительным ** **(* сигнал (int, ** **недействительным ** **(*) (int))) (int);** 

              **сигпауза **    **(целое);** 

              **int **    **sigpending (sigset_t ** ***);** 
              **int **    **sigprocmask(int, ** **const ** **sigset_t ** ***restrict, ** **sigset_t ** ***ограничивать);** 

              **int **    **sigqueue (pid_t, ** **int, ** **const ** **union ** **sigval);** 

              **инт **    **сигрелсе(инт);** 
              **недействительным ** **(*sigset (int, ** **недействительным ** **(*) (int))) (int);** 

              **int **    **sigsuspend (const ** **sigset_t ** ***);** 

              **int **    **sigtimedwait(const ** **sigset_t ** ***restrict, ** **siginfo_t ** ***restrict,** 
                         **const ** **struct ** **timespec ** ***restrict);** 

              **int **    **sigwait(const ** **sigset_t ** ***restrict, ** **int ** ***restrict);** 

              **int **    **sigwaitinfo(const ** **sigset_t ** ***restrict, ** **siginfo_t ** ***restrict);** Включение <signal.h> может сделать видимыми все символы из <time.h> .


```


# Библиотечные функции

Ниже приведены функции, определенные в заголовке signal.h —

[ void (* signal (int sig, void (* func) (int))) (int)](https://www.tutorialspoint.com/c_standard_library/c_function_signal.htm)
     Эта функция устанавливает функцию для обработки сигнала, т.е. обработчик сигнала.



[int raise (int sig)](https://www.tutorialspoint.com/c_standard_library/c_function_raise.htm)
     сигнала **sig** генерацию Аргумент sig совместим с макросами SIG.



# Разбор 

В [стандартной библиотеке C](https://en.wikipedia.org/wiki/C_Standard_Library) обработка **сигналов** определяет, как программа обрабатывает различные [сигналы](https://en.wikipedia.org/wiki/Signal_(computing)) во время своего выполнения. Сигнал может сообщать о каком-то исключительном поведении внутри программы ( _например, о_ [_делении на ноль_](https://en.wikipedia.org/wiki/Division_by_zero) ) или сигнал может сообщать о каком-то асинхронном событии вне программы ( _например, о том, что кто-то_ [_нажимает интерактивную клавишу внимания_](https://en.wikipedia.org/wiki/SIGINT_(POSIX)) _на клавиатуре_ ).
  

**signal.h** — [заголовочный файл](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BE%D1%87%D0%BD%D1%8B%D0%B9_%D1%84%D0%B0%D0%B9%D0%BB), определенный в [, для указания того, как программа обрабатывает](https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%B0%D1%8F_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B0_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_%D0%A1%D0%B8) [сигналы](https://ru.wikipedia.org/wiki/%D0%A1%D0%B8%D0%B3%D0%BD%D0%B0%D0%BB%D1%8B_(UNIX)) во время её выполнения. Сигнал может быть как синхронным с помощью вызова `raise()`, так и асинхронным.

Сигнал — это прерывание, сгенерированное программным обеспечением, которое ОС отправляет процессу из-за того, что пользователь нажимает ctrl-c или другой процесс что-то сообщает этому процессу.  
Существует фиксированный набор сигналов, которые могут быть отправлены процессу. сигнал идентифицируется целыми числами.  
Номера сигналов имеют символические имена. Например **SIGCHLD** — это номер сигнала, отправляемого родительскому процессу при завершении дочернего процесса.

Каждая реализация определяет какой сигнал что генерирует и определяет их генерацию.

Эта часть библиотеки используется для перехвата сигналов — назначения обработчика определённого сигнала.

Обработчик сигнала может вызывать только следующие функции: `_exit()`, `_Exit()`, `abort()`, `raise()` (только если обработчик не вызван функциями abort или raise). Вызов прочих библиотечных функций приводит к неопределённому поведению, хотя отдельными реализациями такие вызовы могут быть разрешены, например в posix есть список **async-signal-safe** функций.

Заголовок **signal.h** определяет тип переменной **sig_atomic_t** , два вызова функций и несколько макросов для обработки различных сигналов, сообщаемых во время выполнения программы.


**Примеры:**

#define SIGHUP 1 /* Завершение процесса */ 
#define SIGINT 2 /* Прервать процесс */ 
 #define SIGQUIT 3 /* Завершить процесс */ 
 #define SIGILL 4 /* Недопустимая инструкция.  */ 
 #define SIGTRAP 5 /* Ловушка трассировки.  */ 
 #define SIGABRT 6 /* Прервать.  */
 

**Структуры ОС для сигналов**

-   Для каждого процесса операционная система поддерживает 2 целых числа с битами, соответствующими номерам сигналов.
-   Два целых числа отслеживают: **ожидающие сигналы и заблокированные сигналы**
-   С помощью 32-битных целых чисел можно представить до 32 различных сигналов.

**Пример:**
В приведенном ниже примере сигнал SIGINT (= 2) заблокирован, и никаких ожидающих сигналов нет.

![[Pasted image 20220916042453.png]]



Сигнал отправляется процессу, устанавливающему соответствующий бит в целом числе ожидающих сигналов для процесса. Каждый раз, когда ОС выбирает процесс для запуска на процессоре, проверяются ожидающие и заблокированные целые числа. Если ожидающих сигналов нет, процесс перезапускается в обычном режиме и продолжает выполнение со следующей инструкции.

Если 1 или более сигналов ожидают обработки, но каждый из них заблокирован, процесс также перезапускается в обычном режиме, но сигналы по-прежнему помечаются как ожидающие обработки. Если 1 или более сигналов ожидают и НЕ заблокированы, ОС выполняет подпрограммы в коде процесса для обработки сигналов.

## Обработчики сигналов по умолчанию

Существует несколько процедур обработки сигналов по умолчанию. Каждый сигнал связан с одной из этих процедур обработчика по умолчанию. Различные подпрограммы обработчика по умолчанию обычно имеют одно из следующих действий:

-   Ign: игнорировать сигнал; то есть ничего не делать, просто вернуться
-   Срок: прекратить процесс
-   Продолжение: разблокировать остановленный процесс
-   Остановить: заблокировать процесс

>
// CPP program to illustrate`
>
`// default Signal Handler`
>
`#include<stdio.h>`
`#include<signal.h>`
>
`int` `main()`
>
`{`
>
    `signal(SIGINT, handle_sigint);`
    `while` `(1)`
    `{`
>
        `printf(“hello world\n”);`
        `sleep(1);`
>
    `}`
>
    `return` `0;`
>
`}`

Вывод: вывести hello world бесконечное число раз. Если пользователь нажимает ctrl-c для завершения процесса из-за **SIGINT** и его обработчика по умолчанию для завершения процесса.

**Output:**

hello world   
hello world         
hello world         
terminated



## Пользовательские обработчики сигналов

Процесс может заменить обработчик сигналов по умолчанию почти для всех сигналов (но не SIGKILL) собственной пользовательской функцией-обработчиком.  
Функция обработчика сигнала может иметь любое имя, но должна иметь тип возвращаемого значения void и иметь один параметр типа int.  
**Пример:** вы можете выбрать имя sigchld_handler для обработчика сигнала **SIGCHLD** (завершение дочернего процесса). Тогда объявление будет таким:

**недействительным sigchld_handler (int sig);** 

Когда обработчик сигнала выполняется, параметр, передаваемый ему, является номером сигнала. Программист может использовать одну и ту же функцию обработчика сигналов для обработки нескольких сигналов. В этом случае обработчик должен будет проверить параметр, чтобы увидеть, какой сигнал был отправлен. С другой стороны, если функция обработчика сигнала обрабатывает только один сигнал, нет необходимости заморачиваться с параметром, поскольку он всегда будет номером этого сигнала.

>
`// CPP program to illustrate`
`// User-defined Signal Handler`
>
`#include<stdio.h>`
`#include<signal.h>`
>
`// Handler for SIGINT, caused by`
`// Ctrl-C at keyboard`
>
`void` `handle_sigint(int` `sig)`
>
`{`
>
    `printf("Caught signal %d\n", sig);`
`}`
>
`int` `main()`
`{`
>
    `signal(SIGINT, handle_sigint);`
    `while` `(1) ;`
>
    `return` `0;`
>
`}`

**Output:**

^CCaught signal 2  // when user presses ctrl-c
^CCaught signal 2

## Отправка сигналов через kill()

Мы можем отправить сигнал процессу, используя kill().
>
**int kill(pid_t pid, int signal);**
**pid:** id of destination process
**signal:** the type of signal to send
**Return value:** 0 if signal was sent successfully

**Example:**
>
pid_t iPid = getpid(); /* Process gets its id.*/
kill(iPid, SIGINT);  /* Process sends itself a  **SIGINT** signal   
(commits suicide?)(because of **SIGINT** 
signal default handler is terminate the process) */

## Разбор wiki

В [стандартной библиотеке C](https://en.wikipedia.org/wiki/C_Standard_Library "Стандартная библиотека C") обработка **сигналов** определяет, как программа обрабатывает различные [сигналы](https://en.wikipedia.org/wiki/Signal_(computing) "Сигнал (вычисления)") во время своего выполнения. Сигнал может сообщать о каком-то исключительном поведении внутри программы ( _например, о [делении на ноль](https://en.wikipedia.org/wiki/Division_by_zero "Деление на ноль")_ ) или сигнал может сообщать о каком-то асинхронном событии вне программы ( _например, о том, что кто-то [нажимает интерактивную клавишу внимания](https://en.wikipedia.org/wiki/SIGINT_(POSIX) "ПОДПИСКА (POSIX)") на клавиатуре_ ).

Стандарт C определяет только 6 сигналов. Все они определены в `signal.h`заголовок ( `csignal`заголовок в [С++](https://en.wikipedia.org/wiki/C%2B%2B "С++") ): [[1]](https://en.wikipedia.org/wiki/C_signal_handling#cite_note-c99-1)

-   `SIGABRT`– «отмена», аварийное завершение.
-   `SIGFPE`– [**исключение** плавающей **с** _ **запятой** _](https://en.wikipedia.org/wiki/Floating_point_exception "Исключение с плавающей запятой") .
-   `SIGILL`– «незаконная», недействительная инструкция.
-   `SIGINT`– «прерывание», интерактивный запрос внимания, отправленный в программу.
-   `SIGSEGV`– « [**нарушение** сегментации **неверный** доступ](https://en.wikipedia.org/wiki/Segmentation_violation "Нарушение сегментации") к памяти.
-   `SIGTERM`– «termination», запрос на завершение отправлен в программу.

Дополнительные сигналы могут быть указаны в `signal.h`заголовок реализацией. Например, Unix и [Unix-подобные](https://en.wikipedia.org/wiki/Unix-like "Unix-подобный") операционные системы (например, [Linux](https://en.wikipedia.org/wiki/Linux "линукс") ) определяют более 15 дополнительных сигналов; см [сигнал Unix](https://en.wikipedia.org/wiki/Unix_signal "Unix-сигнал") . [[2]](https://en.wikipedia.org/wiki/C_signal_handling#cite_note-sus-2)

### Отладка

-   `SIGTRAP`в целях отладки. Он зависит от платформы и может использоваться в [Unix](https://en.wikipedia.org/wiki/Unix "Юникс") подобных операционных системах.

### Обращение

Сигнал может быть сгенерирован вызовом `raise()`или же `kill()`системные вызовы. `raise()`посылает сигнал текущему процессу, `kill()`посылает сигнал определенному процессу.

Обработчик сигнала — это [функция](https://en.wikipedia.org/wiki/Function_(computer_science) "Функция (информатика)") , которая вызывается целевой средой при появлении соответствующего сигнала. Целевая среда приостанавливает выполнение программы до тех пор, пока обработчик сигнала не вернется или не вызовет `longjmp()`.

Обработчики сигналов могут быть установлены с помощью `signal()`или же `sigaction()`. Поведение `signal()`менялся несколько раз на протяжении истории, и его использование не рекомендуется. [[3]](https://en.wikipedia.org/wiki/C_signal_handling#cite_note-3) Он переносим только при использовании для установки расположения сигнала на SIG_DFL или SIG_IGN. Обработчики сигналов могут быть указаны для всех сигналов, кроме двух ( [SIGKILL](https://en.wikipedia.org/wiki/SIGKILL "СИГКИЛЛ") и [SIGSTOP](https://en.wikipedia.org/wiki/SIGSTOP "SIGSTOP") не могут быть перехвачены, заблокированы или проигнорированы).

Если сигнал сообщает об ошибке в программе (и сигнал не является асинхронным), обработчик сигнала может завершить работу, вызвав `abort()`, `exit()`, или же `longjmp()`.

### Функции


| Функция | Описание                                                                              |
| ------- | ------------------------------------------------------------------------------------- |
| raise   | искусственно посылает сигнал вызывающему процессу                                     |
| kill    | искусственно посылает сигнал указанному процессу                                      |
| signal  | устанавливает действие, предпринимаемое, когда программа получает определенный сигнал |

**Example usage**

>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
>
static void catch_function(int signo) {
    puts("Interactive attention signal caught.");
}
>
int main(void) {
    // Set above function as signal handler for the SIGINT signal:
    if (signal(SIGINT, catch_function) == SIG_ERR) {
        fputs("An error occurred while setting a signal handler.\n", stderr);
        return EXIT_FAILURE;
    }
    puts("Raising the interactive attention signal.");
    if (raise(SIGINT) != 0) {
        fputs("Error raising the signal.\n", stderr);
        return EXIT_FAILURE;
    }
    puts("Exiting.");
    return EXIT_SUCCESS;
    // exiting after raising signal
}