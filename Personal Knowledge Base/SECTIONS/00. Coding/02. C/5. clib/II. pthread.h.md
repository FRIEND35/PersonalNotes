# Описание

> _<pthread.h>_ заголовок определяет следующие символы:
> 
> ```
> 
> PTHREAD_CANCEL_ASYNCHRONOUS
> PTHREAD_CANCEL_ENABLE
> PTHREAD_CANCEL_DEFERRED
> PTHREAD_CANCEL_DISABLE
> PTHREAD_CANCELED
> PTHREAD_COND_INITIALIZER
> PTHREAD_CREATE_DETACHED
> PTHREAD_CREATE_JOINABLE
> PTHREAD_EXPLICIT_SCHED
> PTHREAD_INHERIT_SCHED
> PTHREAD_MUTEX_DEFAULT
> PTHREAD_MUTEX_ERRORCHECK
> PTHREAD_MUTEX_NORMAL
> PTHREAD_MUTEX_INITIALIZER
> PTHREAD_MUTEX_RECURSIVE
> PTHREAD_ONCE_INIT
> PTHREAD_PRIO_INHERIT
> PTHREAD_PRIO_NONE
> PTHREAD_PRIO_PROTECT
> PTHREAD_PROCESS_SHARED
> PTHREAD_PROCESS_PRIVATE
> PTHREAD_RWLOCK_INITIALIZER
> PTHREAD_SCOPE_PROCESS
> PTHREAD_SCOPE_SYSTEM
> ```
> 
> **pthread_attr_t** , **pthread_cond_t** , **pthread_condattr_t** , **pthread_key_t** , **pthread_mutex_t** , **pthread_mutexattr_t** , **pthread_once_t** , **pthread_rwlock_t** , **pthread_rwlockattr_t** а также **pthread_t** типы определяются, как описано в _[<sys/типы.h>](https://pubs.opengroup.org/onlinepubs/7908799/xsh/systypes.h.html)_ .
> 
> Следующие функции объявлены как функции, а также могут быть объявлены как макросы. Прототипы функций должны быть предоставлены для использования с ISO C. компилятор.
> 
> ```
> 
> int   pthread_attr_destroy(pthread_attr_t *);
> int   pthread_attr_getdetachstate(const pthread_attr_t *, int *);
> int   pthread_attr_getguardsize(const pthread_attr_t *, size_t *);
> int   pthread_attr_getinheritsched(const pthread_attr_t *, int *);
> int   pthread_attr_getschedparam(const pthread_attr_t *,
>           struct sched_param *);
> int   pthread_attr_getschedpolicy(const pthread_attr_t *, int *);
> int   pthread_attr_getscope(const pthread_attr_t *, int *);
> int   pthread_attr_getstackaddr(const pthread_attr_t *, void **);
> int   pthread_attr_init(pthread_attr_t *);
> int   pthread_attr_setdetachstate(pthread_attr_t *, int);
> int   pthread_attr_setguardsize(pthread_attr_t *, size_t);
> int   pthread_attr_setinheritsched(pthread_attr_t *, int);
> int   pthread_attr_setschedparam(pthread_attr_t *,
>           const struct sched_param *);
> int   pthread_attr_setschedpolicy(pthread_attr_t *, int);
> int   pthread_attr_setscope(pthread_attr_t *, int);
> int   pthread_attr_setstackaddr(pthread_attr_t *, void *);
> int   pthread_attr_setstacksize(pthread_attr_t *, size_t);
> int   pthread_cancel(pthread_t);
> void  pthread_cleanup_push(void*), void *);
> void  pthread_cleanup_pop(int);
> int   pthread_cond_broadcast(pthread_cond_t *);
> int   pthread_cond_destroy(pthread_cond_t *);
> int   pthread_cond_init(pthread_cond_t *, const pthread_condattr_t *);
> int   pthread_cond_signal(pthread_cond_t *);
> int   pthread_cond_timedwait(pthread_cond_t *, 
>           pthread_mutex_t *, const struct timespec *);
> int   pthread_cond_wait(pthread_cond_t *, pthread_mutex_t *);
> int   pthread_condattr_destroy(pthread_condattr_t *);
> int   pthread_condattr_getpshared(const pthread_condattr_t *, int *);
> int   pthread_condattr_init(pthread_condattr_t *);
> int   pthread_condattr_setpshared(pthread_condattr_t *, int);
> int   pthread_create(pthread_t *, const pthread_attr_t *,
>           void *(*)(void *), void *);
> int   pthread_detach(pthread_t);
> int   pthread_equal(pthread_t, pthread_t);
> void  pthread_exit(void *);
> int   pthread_getconcurrency(void);
> int   pthread_getschedparam(pthread_t, int *, struct sched_param *);
> void *pthread_getspecific(pthread_key_t);
> int   pthread_join(pthread_t, void **);
> int   pthread_key_create(pthread_key_t *, void (*)(void *));
> int   pthread_key_delete(pthread_key_t);
> int   pthread_mutex_destroy(pthread_mutex_t *);
> int   pthread_mutex_getprioceiling(const pthread_mutex_t *, int *);
> int   pthread_mutex_init(pthread_mutex_t *, const pthread_mutexattr_t *);
> int   pthread_mutex_lock(pthread_mutex_t *);
> int   pthread_mutex_setprioceiling(pthread_mutex_t *, int, int *);
> int   pthread_mutex_trylock(pthread_mutex_t *);
> int   pthread_mutex_unlock(pthread_mutex_t *);
> int   pthread_mutexattr_destroy(pthread_mutexattr_t *);
> int   pthread_mutexattr_getprioceiling(const pthread_mutexattr_t *,
>           int *);
> int   pthread_mutexattr_getprotocol(const pthread_mutexattr_t *, int *);
> int   pthread_mutexattr_getpshared(const pthread_mutexattr_t *, int *);
> int   pthread_mutexattr_gettype(const pthread_mutexattr_t *, int *);
> int   pthread_mutexattr_init(pthread_mutexattr_t *);
> int   pthread_mutexattr_setprioceiling(pthread_mutexattr_t *, int);
> int   pthread_mutexattr_setprotocol(pthread_mutexattr_t *, int);
> int   pthread_mutexattr_setpshared(pthread_mutexattr_t *, int);
> int   pthread_mutexattr_settype(pthread_mutexattr_t *, int);
> int   pthread_once(pthread_once_t *, void (*)(void));
> int   pthread_rwlock_destroy(pthread_rwlock_t *);
> int   pthread_rwlock_init(pthread_rwlock_t *,
>           const pthread_rwlockattr_t *);
> int   pthread_rwlock_rdlock(pthread_rwlock_t *);
> int   pthread_rwlock_tryrdlock(pthread_rwlock_t *);
> int   pthread_rwlock_trywrlock(pthread_rwlock_t *);
> int   pthread_rwlock_unlock(pthread_rwlock_t *);
> int   pthread_rwlock_wrlock(pthread_rwlock_t *);
> int   pthread_rwlockattr_destroy(pthread_rwlockattr_t *);
> int   pthread_rwlockattr_getpshared(const pthread_rwlockattr_t *,
>           int *);
> int   pthread_rwlockattr_init(pthread_rwlockattr_t *);
> int   pthread_rwlockattr_setpshared(pthread_rwlockattr_t *, int);
> pthread_t
>       pthread_self(void);
> int   pthread_setcancelstate(int, int *);
> int   pthread_setcanceltype(int, int *);
> int   pthread_setconcurrency(int);
> int   pthread_setschedparam(pthread_t, int ,
>           const struct sched_param *);
> int   pthread_setspecific(pthread_key_t, const void *);
> void  pthread_testcancel(void);
> ```
> 
> Включение _<pthread.h>_ заголовок сделает видимыми символы, определенные в заголовках _[<расписание.h>](https://pubs.opengroup.org/onlinepubs/7908799/xsh/sched.h.html)_ а также _[<время.ч>](https://pubs.opengroup.org/onlinepubs/7908799/xsh/time.h.html)_ .

####  ИСПОЛЬЗОВАНИЕ ПРИЛОЖЕНИЯ

> Запрос на интерпретацию был подан в IEEE PASC относительно требования к видимости символов в этом заголовке.


# Разбор 

Многозадачность свойственна устройствам, средам выполнения и операционным системам и несет в себе возможность параллельно и одновременно обрабатывать несколько поставленных задач. Задачи не связаны между собой и могут обрабатываться отдельно друг от друга.

  
  

Поток является отдельной ветвью кода одной программы, которая может выполняться параллельно с другими ветвями кода этой же программы.

Потоки/процессы — это механизм, с помощью которого вы можете запускать несколько сегментов кода одновременно, кажется, что потоки выполняются одновременно; ядро планирует их асинхронно, время от времени прерывая каждый поток, чтобы дать другим возможность выполниться.

Современные операционные системы и микропроцессоры уже давно поддерживает многозадачность и вместе с тем, каждая из этих задач может выполняться в несколько потоков. Это дает ощутимый прирост производительности вычислений и позволяет лучше масштабировать пользовательские приложения и сервера, но за это приходится платить цену — усложняется разработка программы и ее отладка.
  
  

## Общие сведения

Множественные нити исполнения в одном процессе называют _потоками_ и это базовая единица загрузки ЦПУ, состоящая из идентификатора потока, счетчика, регистров и [[ZE. Стек и куча | стека]]. Потоки внутри одного процесса делят секции кода, данных, а также различные ресурсы: описатели открытых файлов, учетные данные процесса сигналы, значения umask, nice, таймеры и прочее.


![[Pasted image 20220905050352.png]]



У всех исполняемых процессов есть как минимум один поток исполнения. Некоторые процессы этим и ограничиваются в тех случаях, когда дополнительные нити исполнения не дают прироста производительности, но только усложняют программу. Однако таких программ с каждым днем становится относительно меньше.

Потоки — это популярный способ улучшить приложение за счет параллелизма. Например, в браузере несколько вкладок могут быть разными потоками. MS Word использует несколько потоков, один поток для форматирования текста, другой поток для обработки входных данных и т. д.  
Потоки работают быстрее процессов по следующим причинам:

  
1) Создание потока намного быстрее.  
2) Переключение контекста между потоками происходит намного быстрее.  
3) Темы могут быть легко завершены  
4) Связь между потоками быстрее.


**POSIX Threads** — стандарт [POSIX](https://ru.wikipedia.org/wiki/POSIX)-реализации [потоков (нитей) выполнения](https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D1%82%D0%BE%D0%BA_%D0%B2%D1%8B%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F). Стандарт _POSIX.1c, Threads extensions (_[_IEEE_](https://ru.wikipedia.org/wiki/IEEE) _Std 1003.1c-1995)_ определяет [API](https://ru.wikipedia.org/wiki/API) для управления потоками, их синхронизации и планирования.

  
  

## Основные функции стандарта

Pthreads определяет набор типов и функций на [языке программирования Си](https://ru.wikipedia.org/wiki/%D0%A1%D0%B8_(%D1%8F%D0%B7%D1%8B%D0%BA_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)). [Заголовочный файл](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BE%D1%87%D0%BD%D1%8B%D0%B9_%D1%84%D0%B0%D0%B9%D0%BB) — pthread.h.

-   Типы данных:
    
    -   pthread_t: [дескриптор](https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2%D1%8B%D0%B9_%D0%B4%D0%B5%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D1%80) потока (идентификатор потока);
        
    -   pthread_attr_t: перечень атрибутов потока;
        
    -   pthread_barrier_t: барьер;
        
    -   pthread_barrierattr_t: атрибуты барьера;
        
    -   pthread_cond_t: [условная переменная](https://ru.wikipedia.org/wiki/%D0%A3%D1%81%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0%D1%8F_%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F);
        
    -   pthread_condattr_t: атрибуты условной переменной;
        
    -   pthread_key_t: данные, специфичные для потока;
        
    -   pthread_mutex_t: [мьютекс](https://ru.wikipedia.org/wiki/%D0%9C%D1%8C%D1%8E%D1%82%D0%B5%D0%BA%D1%81);
        
    -   pthread_mutexattr_t: атрибуты мьютекса;
        
    -   pthread_rwlock_t: мьютекс с возможностью эксклюзивной блокировки;
        
    -   pthread_rwlockattr_t: атрибуты этого мьютекса;
        
    -   pthread_spinlock_t: [спинлок](https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D0%BD%D0%BB%D0%BE%D0%BA);
        
    -   Функции управления потоками:
        

-   pthread_create(): создание потока.
    

-   pthread_exit(): завершение потока (должна вызываться функцией потока при завершении).
    

-   pthread_cancel(): отмена потока.
    

-   pthread_join(): подключиться к другому потоку и ожидать его завершения; поток, к которому необходимо подключиться, должен быть создан с возможностью подключения (PTHREAD_CREATE_JOINABLE).
    

-   pthread_detach(): отключиться от потока, сделав его при этом отдельным (PTHREAD_CREATE_DETACHED).
    

-   pthread_attr_init(): инициализировать структуру атрибутов потока.
    

-   pthread_attr_setdetachstate(): указывает параметр "отделимости" потока (detach state), который говорит о возможности подключения к нему (при помощи pthread_join) других потоков (значение PTHREAD_CREATE_JOINABLE) для ожидания окончания или о запрете подключения (значение PTHREAD_CREATE_DETACHED); ресурсы отдельного потока (PTHREAD_CREATE_DETACHED) при завершении автоматически освобождаются и возвращаются системе.
    

-   pthread_attr_destroy(): освободить память от структуры атрибутов потока (уничтожить дескриптор).
    

### Простая программа на C для демонстрации использования основных функций pthread.
Обратите внимание, что приведенная ниже программа может компилироваться только компиляторами C с библиотекой pthread.

>
**#include <stdio.h>**
**#include <stdlib.h>**
**#include <unistd.h>  //Header file for sleep(). man 3 sleep for details.**
**#include <pthread.h>**
>
**// A normal C function that is executed as a thread** 
**// when its name is specified in pthread_create()**
>
**void** ***myThreadFun(void** ***vargp)**
>
**{**
>
    **sleep(1);**
>
    **printf("Printing GeeksQuiz from Thread \n");**
>
    **return** **NULL;**
>
**}**
>
**int** **main()**
>
**{**
>
    **pthread_t thread_id;**
    **printf("Before Thread\n");**
    **pthread_create(&thread_id, NULL, myThreadFun, NULL);**
    **pthread_join(thread_id, NULL);**
    **printf("After Thread\n");**
    **exit(0);**
>
**}**

В main() мы объявляем переменную с именем thread_id, которая имеет тип pthread_t, представляющий собой целое число, используемое для идентификации потока в системе. После объявления thread_id мы вызываем функцию pthread_create() для создания потока.  
pthread_create() принимает 4 аргумента.  

- Первый аргумент — это указатель на thread_id, который устанавливается этой функцией.  
- Второй аргумент определяет атрибуты. Если значение равно NULL, то должны использоваться атрибуты по умолчанию.  
- Третий аргумент — это имя функции, которая должна быть выполнена для создаваемого потока.  
- Четвертый аргумент используется для передачи аргументов функции myThreadFun.  

Функция pthread_join() для потоков аналогична функции wait() для процессов. Вызов pthread_join блокирует вызывающий поток до тех пор, пока не завершится поток с идентификатором, равным первому аргументу.

  
  

**Как скомпилировать вышеуказанную программу?**

  
Чтобы подключить библиотеку Pthread к программе, нужно передать компоновщику опцию -lpthread. То есть чтобы скомпилировать многопоточную программу с помощью gcc, нам нужно скомпоновать ее с библиотекой pthreads.
  

Ниже приведена команда, используемая для компиляции программы.

gfg@ubuntu:~/$ gcc multithread.c -lpthread
gfg@ubuntu:~/$ ./a.out
Before Thread
Printing GeeksQuiz from Thread
After Thread
gfg@ubuntu:~/$  
  

### Пример 2
  
>
**#include <stdio.h>
#include <pthread.h>
>
void *text_print(){**
>
  **printf("Hello from precess 1\n");**
>
**}**
>
**void *text_print2(){**
>
  **printf("Hello from process 2\n");**
>
**}**
>
**int main(){**
>
  **pthread_t thread1, thread2;**
  **thread1 = pthread_create(&thread1,NULL,text_print,NULL);**
  **thread2 = pthread_create(&thread2,NULL,text_print2,NULL);**
  **pthread_join(thread1,NULL);**
  **pthread_join(thread2,NULL);**
  **printf("This is main process!");**
  >
  **return 0;** 
**}**

  
  
Результать выполнении кода указанной выще каждый раз будет разным, это потому что если 2 потока созданы последовательно то и отрабатывать начнет раньше тот, который был создан первым. Там нету блокировок никаких.

Хочешь добиться какой-то синхронизации в действиях, нужно иметь знания про мьютексы семафоры и прочую поебень.

  
  

### Пример 3:

>
**#include <stdio.h>**
**#include <stdlib.h>**
**#include <assert.h>**
**#include <pthread.h>**
**#include <unistd.h>**
>
**#define NUM_THREADS 5**
>
**void *perform_work(void *arguments){**
  **int index = *((int *)arguments);**
  **int sleep_time = 1 + rand() % NUM_THREADS;**
  **printf("THREAD %d: Started.\n", index);**
  **printf("THREAD %d: Will be sleeping for %d seconds.\n", index, sleep_time);**
  **sleep(sleep_time);**
  **printf("THREAD %d: Ended.\n", index);**
  **return NULL;**
**}**
>
**int main(void) {**
  **pthread_t threads[NUM_THREADS];**
  **int thread_args[NUM_THREADS];**
  **int i;**
  **int result_code;**
  >
  **//create all threads one by one**
  **for (i = 0; i < NUM_THREADS; i++) {**
    **printf("IN MAIN: Creating thread %d.\n", i);**
    **thread_args[i] = i;**
    **result_code = pthread_create(&threads[i], NULL, perform_work,   &thread_args[i]);**
    **assert(!result_code);**
  **}**
>
  **printf("IN MAIN: All threads are created.\n");**
>
  **//wait for each thread to complete**
  **for (i = 0; i < NUM_THREADS; i++) {**
    **result_code = pthread_join(threads[i], NULL);**
    **assert(!result_code);**
    **printf("IN MAIN: Thread %d has ended.\n", i);**
  **}**
>
  **printf("MAIN program has ended.\n");**
  **return 0;**
**}**


**Что такое нить?**

Поток — это отдельный поток последовательности внутри процесса. Поскольку потоки обладают некоторыми свойствами процессов, их иногда называют _облегченными процессами_ .

**В чем разница между процессом и потоком?**  

Потоки не независимы друг от друга, в отличие от процессов. В результате потоки делятся с другими потоками своим разделом кода, разделом данных и ресурсами ОС, такими как открытые файлы и сигналы. Но, как и процессы, поток имеет свой собственный программный счетчик (ПК), набор регистров и пространство [[ZE. Стек и куча | стека]].

**Почему многопоточность?** Потоки — это популярный способ улучшить приложение за счет параллелизма. Например, в браузере несколько вкладок могут быть разными потоками. MS Word использует несколько потоков, один поток для форматирования текста, другой поток для обработки входных данных и т. д.

Потоки работают быстрее процессов по следующим причинам:

1) Создание потока намного быстрее.

2) Переключение контекста между потоками происходит намного быстрее.

3) Темы могут быть легко завершены

4) Связь между потоками быстрее.

Подробнее см. [http://www.personal.kent.edu/~rmuhamma/OpSystems/Myos/threads.htm](http://www.personal.kent.edu/%7Ermuhamma/OpSystems/Myos/threads.htm) .

**Можем ли мы писать многопоточные программы на C?**  

В отличие от Java, многопоточность не поддерживается стандартом языка. [POSIX Threads (или Pthreads)](http://en.wikipedia.org/wiki/POSIX_Threads) — это стандарт POSIX для потоков. Реализация pthread доступна с компилятором gcc.

**Простая программа на C для демонстрации использования основных функций pthread.**  

Обратите внимание, что приведенная ниже программа может компилироваться только компиляторами C с библиотекой pthread.

>
`#include <stdio.h>`
`#include <stdlib.h>`
`#include <unistd.h>  //Header file for sleep(). man 3 sleep for details.`
`#include <pthread.h>`
>
`// A normal C function that is executed as a thread`
`// when its name is specified in pthread_create()`
>
`void` `*myThreadFun(``void` `*vargp)`
`{`
>
    `sleep(1);`
    `printf``("Printing GeeksQuiz from Thread \n");`
    `return` `NULL;`
`}`
`int` `main()`
`{`
>
    `pthread_t thread_id;`
    `printf``("Before Thread\n");`
    `pthread_create(&thread_id, NULL, myThreadFun, NULL);`
    `pthread_join(thread_id, NULL);`
    `printf``("After Thread\n");`
    `exit``(0);`
`}`

В main() мы объявляем переменную с именем thread_id, которая имеет тип pthread_t, представляющий собой целое число, используемое для идентификации потока в системе. После объявления thread_id мы вызываем функцию pthread_create() для создания потока.

pthread_create() принимает 4 аргумента.

Первый аргумент — это указатель на thread_id, который устанавливается этой функцией.

Второй аргумент определяет атрибуты. Если значение равно NULL, то должны использоваться атрибуты по умолчанию.

Третий аргумент — это имя функции, которая должна быть выполнена для создаваемого потока.

Четвертый аргумент используется для передачи аргументов функции myThreadFun.

Функция pthread_join() для потоков аналогична функции wait() для процессов. Вызов pthread_join блокирует вызывающий поток до тех пор, пока не завершится поток с идентификатором, равным первому аргументу.

**Как скомпилировать вышеуказанную программу?**  

Чтобы скомпилировать многопоточную программу с помощью gcc, нам нужно скомпоновать ее с библиотекой pthreads. Ниже приведена команда, используемая для компиляции программы.

gfg@ubuntu:~/$ gcc multithread.c -lpthread
 gfg@ubuntu:~/$ ./a.out
 Перед потоком
 Печать GeeksQuiz из темы 
 После темы
 gfg@ubuntu:~/$ 

**Программа AC для отображения нескольких потоков с глобальными и статическими переменными**  

Как упоминалось выше, все потоки совместно используют сегмент данных. Глобальные и статические переменные хранятся в сегменте данных. Поэтому они являются общими для всех потоков. Следующий пример программы демонстрирует то же самое.
>
`#include <stdio.h>`
`#include <stdlib.h>`
`#include <unistd.h>`
`#include <pthread.h>`
>
`// Let us create a global variable to change it in threads`
>
`int` `g = 0;`
>
`// The function to be executed by all threads`
>
`void` `*myThreadFun(``void` `*vargp)`
>
`{`
>
    `// Store the value argument passed to this thread`
>
    `int` `*myid = (``int` `*)vargp;`
>
    `// Let us create a static variable to observe its changes`
>
    `static` `int` `s = 0;`
>
    `// Change static and global variables`
>
    `++s; ++g;`
>
    `// Print the argument, static and global variables`
>
    `printf``("Thread ID: %d, Static: %d, Global: %d\n", *myid, ++s, ++g);`
>
`}`
>
`int` `main()`
>
`{`
>
    `int` `i;`
>
    `pthread_t tid;`
>
    `// Let us create three threads`
>
    `for` `(i = 0; i < 3; i++)`
>
        `pthread_create(&tid, NULL, myThreadFun, (``void` `*)&tid);`
>
    `pthread_exit(NULL);`
>
    `return` `0;`
>
`}`

 gfg@ubuntu:~/$ gcc multithread.c -lpthread
 gfg@ubuntu:~/$ ./a.out
 Идентификатор потока: 3, статический: 2, глобальный: 2
 Идентификатор потока: 3, статический: 4, глобальный: 4
 Идентификатор потока: 3, статический: 6, глобальный: 6
 gfg@ubuntu:~/$ 

Обратите внимание, что выше приведен простой пример, показывающий, как работают потоки. Доступ к глобальной переменной в потоке обычно является плохой идеей. Что, если поток 2 имеет приоритет над потоком 1, и поток 1 должен изменить переменную. На практике, если требуется доступ к глобальной переменной несколькими потоками, то доступ к ним следует осуществлять с помощью мьютекса.