# POSIX
  

Давайте попытаемся выяснить, что описывает стандарт POSIX.

POSIX - это семейство [стандартов](https://en.wikipedia.org/wiki/Standardization) , определенных [IEEE Computer Society](https://en.wikipedia.org/wiki/IEEE_Computer_Society) для обеспечения совместимости между [операционными системами](https://en.wikipedia.org/wiki/Operating_system) как системного, так и пользовательского уровня [интерфейсы прикладного программирования](https://en.wikipedia.org/wiki/Application_programming_interface) (API) [оболочки](https://en.wikipedia.org/wiki/Unix_shell) и служебные интерфейсы для обеспечения совместимости (переносимости) программного обеспечения с вариантами [Unix](https://en.wikipedia.org/wiki/Unix) и других операционных систем. POSIX также является [товарным знаком](https://en.wikipedia.org/wiki/Trademark) IEEE. [[1]](https://en.wikipedia.org/wiki/POSIX#cite_note-FAQ-1) POSIX предназначен для использования как разработчиками приложений, так и разработчиками систем.

Стандарты предназначены для того, чтобы мой компьютер мог взаимодействовать с вашим. Благодаря им, на двух похожих компьютерах веб-страницы или трансляция видео в реальном времени будут выглядеть одинаково.

Однако стандартны предназначены для более масштабных задач, нежели простой обмен какими-либо данными между пользователями. Некоторые стандарты определяют особую модель, благодаря которой открываются возможности, значительно превосходящие по своему значению совместимость файлов или сетей. Стандарт POSIX относится к их числу.

POSIX (portable operating system interface — переносимый интерфейс [операционных](https://ru.wikipedia.org/wiki/%D0%9E%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0) [систем](https://ru.wikipedia.org/wiki/%D0%9E%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0), произносится как «позикс») — набор стандартов, описывающих интерфейсы между [операционной системой](https://ru.wikipedia.org/wiki/%D0%9E%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0) и [прикладной программой](https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B8%D0%BA%D0%BB%D0%B0%D0%B4%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%BE%D0%B5_%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D0%B5) (системный [API](https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9)), библиотеку языка C и набор приложений и их интерфейсов. Стандарт создан для обеспечения совместимости различных [UNIX](https://ru.wikipedia.org/wiki/UNIX)-подобных операционных систем и переносимости прикладных программ на уровне [исходного кода](https://ru.wikipedia.org/wiki/%D0%98%D1%81%D1%85%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BE%D0%B4), но может быть использован и для не-Unix систем.

  
**Все еще не поняли? Окей**

**Posix -** это интерфейс портативных операционных систем. Но что это значит? Во-первых, нужно обозначить область действия понятия «портативность», в этом конкретном случае, и определиться с понятием «интерфейс». Чтобы выяснить это, необходимо отталкиваться от того, что оба понятия неразрывно связаны.

«Портативность», в контексте стандарта POSIX, относится к исходному коду (не к бинарникам, которые из этих самых исходников собираются). Теперь выясним, что такое «интерфейс». В программировании, «интерфейс»— это взаимодействие вашего кода с остальным кодом. Интерфейс ждет от вашего кода предоставления определенной информации. Ваш код, в свою очередь, предполагает получение определенной информации от интерфейса. Хороший пример— функция fopen() в языке Си. Она ожидает информации из двух частей: путь к файлу и режим, в котором он будет открыт. С помощью этих данных, операционная система возвращает другой вид информации, который называется «дескриптор файла». Дескриптор файла может быть использован для чтения файла или записи в файл. Это и есть интерфейс. Из всего этого следует, что POSIX-совместимый код может быть скомпилирован под любую POSIX-совместимую операционную систему без серьезных изменений, а значит, он будет портативным.

Список некоторых интерфейсов, относящихся к стандарту POSIX:

-   snaf()
    
-   printf()
    
-   fprintf()
    
-   memset()
    
-   free()
    
-   [_fdopendir_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fdopendir.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fdopendir.html)
    

-   [_fdopen_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fdopen.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fdopen.html)
    

-   [_feclearexcept_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/feclearexcept.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/feclearexcept.html)
    

-   [_fegetenv_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fegetenv.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fegetenv.html)
    

-   [_fegetexceptflag_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fegetexceptflag.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fegetexceptflag.html)
    

-   [_fegetround_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fegetround.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fegetround.html)
    

-   [_feholdexcept_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/feholdexcept.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/feholdexcept.html)
    

-   [_feof_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/feof.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/feof.html)
    

-   [_feraiseexcept_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/feraiseexcept.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/feraiseexcept.html)
    

-   [_ferror_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/ferror.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/ferror.html)
    

-   [_fesetenv_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fesetenv.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fesetenv.html)
    

-   [_fesetexceptflag_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fesetexceptflag.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fesetexceptflag.html)
    

-   [_fesetround_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fesetround.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fesetround.html)
    

-   [_fetestexcept_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fetestexcept.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fetestexcept.html)
    

-   [_feupdateenv_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/feupdateenv.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/feupdateenv.html)
    

-   [_fexecve_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fexecve.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fexecve.html)
    

-   [_fflush_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fflush.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fflush.html)
    

-   [_ffs_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/ffs.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/ffs.html)
    

-   [_fgetc_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fgetc.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fgetc.html)
    

-   [_fgetpos_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fgetpos.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fgetpos.html)
    

-   [_fgets_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fgets.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fgets.html)
    

-   [_fgetwc_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fgetwc.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fgetwc.html)
    

-   [_fgetws_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fgetws.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fgetws.html)
    

-   [_fileno_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fileno.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fileno.html)
    

-   [_flockfile_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/flockfile.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/flockfile.html)
    

-   [_floorf_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/floorf.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/floorf.html)
    

-   [_floor_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/floor.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/floor.html)
    

-   [_floorl_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/floorl.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/floorl.html)
    

-   [_fmaf_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fmaf.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fmaf.html)
    

-   [_fma_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fma.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fma.html)
    

-   [_fmal_](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fmal.html)[()](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fmal.html)
    

Это всего 1% стандартов, Список интерфейсов, относящихся к стандарту POSIX, находится тут — [https://pubs.opengroup.org/onlinepubs/9699919799/idx/functions.html](https://pubs.opengroup.org/onlinepubs/9699919799/idx/functions.html). Однако, даже несмотря на его огромную длину, вполне возможно, что он неполон. POSIX не ограничивается системными вызовами, он также определяет стандарты для оболочек операционных систем (шеллов, иначе — интерфейсов командной строки), системных утилит, вроде «awk» или «echo», системных библиотек и многого другого.

Стандарт POSIX появился в виде проекта Ричарда Столлмана в 1985 году и в дальнейшем был оформлен как IEEE Std 1003.-1998. Как видно из названия, 1998 год был годом официальной публикации. С тех пор было выпущено большое количество дополнений и расширений к POSIX, который постепенно превращается в целое семейство стандартов, формально известное как IEEE 1003, признанное в качестве международного, с обозначением SO/IEC 9945, попросту называемое стандарт семейства POSIX.

Операционной системе вовсе необязательно быть POSIX-совместимой или уж тем более иметь сертификат POSIX, однако это позволяет разработчикам создавать приложения, инструменты и платформы, не переписывая код раз за разом, а лишь дополнять и подключаться к уже готовому. Также совсем не обязательно писать POSIX-совместимый код, однако это значительно улучшает переносимость проектов между операционными системами. Это значит, что умение писать код, который совместим со стандартом POSIX, является ценным само по себе, и, безусловно, очень полезно для карьеры. Крупные проекты, такие как Gnome или KDE, придерживаются стандарта POSIX, что гарантирует их работу на разных операционных системах. Подсистема POSIX реализована даже в последних выпусках Windows. Linux, как известно, поддерживает большинство системных вызовов, относящихся к стандарту POSIX, также как и крупное расширение к нему, называемое «Стандартная база Linux», которая предназначена для объединения дистрибутивов Linux в плане поддержки исходных кодов и бинарных данных.

  
  

**Вывод****: 

POSIX (Portable Operating System Interface) — это набор стандартных [операционной системы](https://whatis.techtarget.com/definition/operating-system-OS) , основанный на [Unix](https://www.techtarget.com/searchdatacenter/definition/Unix) . Потребность в [стандартизации](https://searchsqlserver.techtarget.com/definition/record-standardization) возникла, потому что предприятия, использующие компьютеры, хотели иметь возможность разрабатывать программы, которые можно было бы перемещать между компьютерными системами разных производителей без необходимости перекодирования. Unix был выбран в качестве основы для стандартного системного интерфейса отчасти потому, что он был «независим от производителя». Однако существовало несколько основных версий Unix, поэтому возникла необходимость разработать систему с общим знаменателем.

Неформально каждый стандарт в наборе POSIX определяется десятичной дробью после POSIX. Таким образом, POSIX.1 является стандартом интерфейса прикладной программы на [C.](https://www.techtarget.com/searchwindowsserver/definition/C) языке POSIX.2 — это стандартная [оболочка](https://www.techtarget.com/searchdatacenter/definition/shell) и [утилит](https://whatis.techtarget.com/definition/utility) (то есть командный интерфейс пользователя с операционной системой). Это два основных интерфейса, но [потоками](https://whatis.techtarget.com/definition/thread) были разработаны или разрабатываются дополнительные интерфейсы, такие как POSIX.4 для управления Интерфейсы POSIX были разработаны под эгидой Института инженеров по электротехнике и электронике ( [IEEE](https://whatis.techtarget.com/definition/IEEE-Institute-of-Electrical-and-Electronics-Engineers) ).

Интерфейсы POSIX.1 и POSIX.2 включены в несколько более крупный интерфейс, известный как Руководство по программированию X/Open (также известный как «Единая спецификация UNIX» и «UNIX 03»). Open Group, группа по отраслевым стандартам, владеет товарным знаком UNIX и, таким образом, может «маркировать» операционные системы, соответствующие интерфейсу, как системы «UNIX». IBM OS/390 является примером операционной системы, включающей фирменный интерфейс UNIX. (Обратите внимание, что товарным знаком является «UNIX»; общим термином для этих операционных систем является «Unix».)