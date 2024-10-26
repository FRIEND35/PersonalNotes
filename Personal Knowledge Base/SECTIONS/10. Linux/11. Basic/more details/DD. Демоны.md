
В [Unix](https://www.computerhope.com/jargon/u/unix.htm) и [Linux](https://www.computerhope.com/jargon/l/linux.htm) — **демон** это программа, работающая в [фоновом режиме](https://www.computerhope.com/jargon/b/backgrou.htm) и не требующая вмешательства пользователя. Имя файла программного демона обычно оканчивается на букву **d**.

Например, **httpd** ( [демон протокола передачи гипертекста](https://www.computerhope.com/jargon/h/http.htm) ) работает как фоновый процесс на многих веб-серверах, в том числе созданных [Apache](https://www.computerhope.com/jargon/a/apache.htm) , [CERN](https://www.computerhope.com/jargon/c/cern.htm) и [NCSA](https://www.computerhope.com/jargon/n/ncsa.htm) . Httpd ожидает и отвечает на запросы, сделанные через HTTP, предоставляя веб-страницы и другие файлы по мере необходимости. Если вы используете один из этих веб-серверов и запускаете команду [top](https://www.computerhope.com/unix/top.htm) , вы видите запросы httpd по мере того, как они выполняются на сервере.

В [Microsoft Windows](https://www.computerhope.com/jargon/w/windows.htm) программное обеспечение, работающее как неинтерактивный фоновый процесс, называется [службой](https://www.computerhope.com/jargon/s/service.htm) . Служба Windows выполняет примерно ту же роль, что и демон Linux или Unix.

**Де́мон** (daemon, dæmon, [др.-греч.](https://ru.wikipedia.org/wiki/%D0%94%D1%80%D0%B5%D0%B2%D0%BD%D0%B5%D0%B3%D1%80%D0%B5%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D1%8F%D0%B7%D1%8B%D0%BA "Древнегреческий язык") δαίμων _[дэймон](https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D0%B9%D0%BC%D0%BE%D0%BD_(%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F) "Деймон (значения)")_) — [компьютерная программа](https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%BD%D0%B0%D1%8F_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0 "Компьютерная программа") в [UNIX-подобных системах](https://ru.wikipedia.org/wiki/Unix-%D0%BF%D0%BE%D0%B4%D0%BE%D0%B1%D0%BD%D0%B0%D1%8F_%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0 "Unix-подобная операционная система"), запускаемая самой системой и работающая в [фоновом режиме](https://ru.wikipedia.org/wiki/%D0%A4%D0%BE%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9_%D1%80%D0%B5%D0%B6%D0%B8%D0%BC "Фоновый режим") без прямого взаимодействия с пользователем.

Демоны обычно запускаются во время загрузки системы. Типичные задачи демонов: [серверы](https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D1%80%D0%B2%D0%B5%D1%80_(%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5) "Сервер (приложение)") [сетевых протоколов](https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D1%82%D0%B5%D0%B2%D0%BE%D0%B9_%D0%BF%D1%80%D0%BE%D1%82%D0%BE%D0%BA%D0%BE%D0%BB "Сетевой протокол") ([HTTP](https://ru.wikipedia.org/wiki/HTTP "HTTP"), [FTP](https://ru.wikipedia.org/wiki/File_Transfer_Protocol "File Transfer Protocol"), электронная почта и др.), управление оборудованием, поддержка очередей печати, управление выполнением заданий по расписанию и т. д. В техническом смысле демоном считается [процесс](https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D1%86%D0%B5%D1%81%D1%81_(%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0) "Процесс (информатика)"), который не имеет управляющего терминала. Чаще всего (но не обязательно) предком демона является [init](https://ru.wikipedia.org/wiki/Init "Init") — корневой процесс UNIX. Традиционно названия демон-процессов заканчиваются на букву _d_, чтобы показать, что этот процесс является демоном, и для различия нормальной компьютерной программы и демона.

В операционных системах [Solaris 10](https://ru.wikipedia.org/wiki/Solaris_10 "Solaris 10") и [OpenSolaris](https://ru.wikipedia.org/wiki/OpenSolaris "OpenSolaris") для управления демонами используется специальный механизм — [Service Management Facility](https://ru.wikipedia.org/wiki/Service_Management_Facility "Service Management Facility").

В системах [Windows](https://ru.wikipedia.org/wiki/Windows "Windows") аналогичный класс программ называется [службой](https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B1%D1%8B_Windows "Службы Windows") ([англ.](https://ru.wikipedia.org/wiki/%D0%90%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9_%D1%8F%D0%B7%D1%8B%D0%BA "Английский язык") Services).

Демоны много работают, для того, чтобы вы могли сосредоточится на своем деле. Представьте, что вы пишите статью или книгу. Вы заинтересованны в том, чтобы писать. Удобно, что вам не нужно вручную запускать принтер и сетевые службы, а потом следить за ними весь день для того чтобы убедится, что всё работает нормально.

За это можно благодарить демонов, они делают эту работу за нас. В сегодняшней статье мы рассмотрим что такое демоны в Linux, а также зачем они нужны.



## wiki

Демоны** (англ. _«**daemons»_) — это работающие в фоновом режиме служебные программы (или _процессы_), целью которых является мониторинг определенных подсистем ОС и обеспечение её нормальной работы. Например, демон принтера контролирует возможности печати, демон сети контролирует и поддерживает сетевые коммуникации и т.д.

**_Примечание_**: Windows называет такие процессы «службами», в то время как UNIX-подобные системы [**называют их «демонами»**](https://ravesli.com/daemons-in-linux/ "Что такое демоны (daemons) в Linux?").

Самым известным демоном является [**systemd**](https://ravesli.com/linux-init-systems/ "Системы инициализации Linux. Сравнение SysV и systemd"), который управляет всеми другими процессами операционной системы. Это первый процесс, который выполняется после загрузки ядра Linux. Его задача состоит в том, чтобы управлять другими демонами и запускать их при необходимости во время загрузки или в любое другое время. Он контролирует все службы, доступные в операционной системе, и может включать или выключать их при необходимости.  

Демоны являются аналогом служб (_services_) в [**Windows**](https://ravesli.com/sravnenie-linux-i-windows-v-chem-raznitsa-i-chto-luchshe/ "Сравнение Linux и Windows"): они выполняют определенные действия в заранее определенное время или в ответ на определенные события. Существует множество различных демонов, работающих в [**Linux**](https://ravesli.com/chto-takoe-linux-ego-struktura-i-preimushhestva/ "Что такое Linux? История создания Linux"), каждый из которых создан специально для наблюдения за своей собственной маленькой частью системы. Из-за того, что демоны выполняют основную часть своей работы в фоновом режиме и не находятся под прямым контролем пользователя, бывает трудно определить предназначение того или иного демона.

Так как демон — это процесс, который выполняется в фоновом режиме и обычно находится вне контроля пользователя, то _у него нет управляющего терминала_.

**Процесс** — это запущенная программа. В определенный момент времени процесс может либо выполняться, либо ожидать, либо быть **[«зомби»](https://ravesli.com/processes-v-linux/#toc-2)**.

В Linux существует три типа процессов:

   - **Процессы переднего плана** (или _**«интерактивные процессы»**_) — это те процессы, которые запускаются пользователем в [**терминале**](https://ravesli.com/bash-v-linux/#toc-0).

   - **Фоновые процессы** (или _**«автоматические процессы»**_) — это объединенные в список процессы, не подключенные к терминалу; они не ожидают пользовательского ввода данных.

   - **Демоны** (англ. **_«_****_daemons»_**) — это особый тип фоновых процессов, которые запускаются при старте системы и продолжают работать в виде системных служб; они не _умирают_.

Процессы переднего плана и фоновые процессы _не являются демонами_, хотя их можно запускать в фоновом режиме и выполнять некоторую работу по мониторингу системы. Для данных типов процессов необходимо участие пользователя, который бы их запускал. В то время как демонам для их запуска пользователь не требуется.

Когда завершается загрузка системы, процесс инициализации системы начинает создавать демоны с помощью **метода fork()**, устраняя необходимость в терминале (именно это подразумевается под _«отсутствием управляющего терминала»_).

Я не буду вдаваться в подробности работы метода _fork__()_, отмечу лишь, что, хотя существуют и другие методы, традиционный способ создания дочернего процесса в Linux заключается в создании копии существующего процесса (посредством своеобразного «ответвления»), после чего выполняется системный вызов _exec__()_ для запуска другой программы.

_**Примечание**_: Термин _«fork»_ не был взят с потолка. Он получил свое название от метода fork() из Стандартной библиотеки языка программирования Си. В языке Си данный метод предназначен для создания новых процессов.


## Примеры демонов в Linux

Наиболее распространенный способ идентификации демона в Linux — это поиск [**процесса**](https://ravesli.com/processes-v-linux/ "Изучаем процессы в Linux. Управление процессами"), имя которого заканчивается буквой _d._ Есть много способов увидеть работающих демонов. Их можно отследить в списках процессов через такие команды, как: `ps`, `top`, `htop`, а также `pstree`.

**Команда pstree** показывает процессы, запущенные в настоящее время в нашей системе, и отображает их в виде древовидной диаграммы. Откройте терминал и введите следующую команду:

> pstree

Вывод команды `pstree` — это довольно хорошая иллюстрация того, что происходит с нашей системой. Перед нами появился список всех запущенных процессов, среди которых можно заметить и несколько демонов: _cups**d**_, _dbus-_**_daemon_**, _kdekonnect**d**_, _packagekit**d**_ и некоторые другие.

Вот несколько «популярных» примеров демонов, которые могут работать в вашей системе:

   - _system**d**_ — это системный демон, который (подобно процессу _init_) является родителем (прямым или косвенным) всех других процессов, и имеет [**PID=1**](https://ravesli.com/processes-v-linux/#toc-1).

   - _rsyslog**d**_ — используется для регистрации системных сообщений. Это более новая версия _syslogd_, имеющая несколько дополнительных функций.

   - _udisks**d**_ — обрабатывает такие операции, как: запрос, монтирование, размонтирование, форматирование или отсоединение устройств хранения данных (жесткие диски, USB-флеш-накопители и пр.).

   - _login**d**_ — крошечный демон, который различными способами управляет входами пользователей в систему.

   -  _ssh**d**_ — демон, отвечающий за управление службой SSH. Используется практически на любом сервере, который принимает SSH-соединения.

   - _ftp**d**_ — управляет службой FTP. Протокол FTP (сокр. от англ. _«**F**ile **T**ransfer **P**rotocol»_) является широко используемым протоколом для передачи файлов между компьютерами, где один компьютер действует как клиент, другой — как сервер.

   - _cron**d**_ — демон планировщика заданий, зависящих от времени. С его помощью можно выполнять обновление программного обеспечения, проверку системы и пр.

Пример типы задач демонов:

   - Серверы сетевых протоколов
   - Обработка сетевых запросов
   - Прослушивание портов

И многое другое.



Демоны много работают, поэтому вам не нужно.

Представьте, что вы пишете статью, веб-страницу или книгу. Ваше намерение состоит в том, чтобы сделать именно это — написать. Довольно приятно, что вам не нужно вручную запускать принтер и сетевые службы, а затем весь день следить за их работой, чтобы убедиться, что они работают правильно.

Мы можем поблагодарить за это демонов — они делают эту работу за нас.

![[Pasted image 20221109055801.png]]

## Что такое демон в Linux?

Демон _( обычно_ произносится как: `day-mon`, но иногда произносится как рифмующийся с `diamond`) — это программа с уникальной целью. Это служебные программы, которые тихо работают в фоновом режиме, чтобы контролировать и заботиться об определенных подсистемах, чтобы гарантировать, что операционная система работает правильно. Демон принтера контролирует и заботится о службах печати. Сетевой демон отслеживает и поддерживает сетевые коммуникации и так далее.

Пройдясь по произношению _daemon_ , добавлю, что если вы хотите произносить его как демон, я не буду жаловаться.

Для тех, кто пришел в Linux из мира Windows, демоны известны как _сервисы_ . Для пользователей Mac термин _сервисы_ используется по-другому. Операционная система Mac на самом деле UNIX, поэтому в ней используются демоны. Термин _услуги_ используется, но только для обозначения программного обеспечения, находящегося под `Services`меню.

Демоны выполняют определенные действия в заранее определенное время или в ответ на определенные события. В системе Linux работает множество демонов, каждый из которых специально предназначен для наблюдения за своей маленькой частью системы, и, поскольку они не находятся под непосредственным контролем пользователя, они фактически невидимы, но необходимы. Поскольку демоны выполняют большую часть своей работы в фоновом режиме, они могут казаться немного загадочными, и, возможно, их трудно идентифицировать и определить, что они на самом деле делают.

## Какие демоны работают на вашей машине?

Чтобы идентифицировать демона, найдите процесс, оканчивающийся на букву _d_ . Это общее правило Linux, что имена демонов заканчиваются именно так.

Есть много способов мельком увидеть работающий демон. Их можно увидеть в списках процессов через `ps`, `top`, или же `htop`. Это полезные программы сами по себе — у них есть определенная цель, но чтобы увидеть все демоны, работающие на вашей машине, `pstree`command лучше подойдет для нашего обсуждения.

The `pstree`command — это небольшая удобная утилита, которая показывает процессы, запущенные в настоящее время в вашей системе, и отображает их в виде древовидной диаграммы. Откройте терминал и введите эту команду:

```
pstree
```

Вы увидите полный список всех запущенных процессов. Вы можете не знать, что из себя представляют некоторые из них или что они делают, они перечислены. `pstree`output является довольно хорошей иллюстрацией того, что происходит с вашей машиной. Много всего происходит!

![проверить наличие демона с помощью pstree](https://itsfoss.com/wp-content/uploads/2021/05/daemon_pstree1.png)

демон — запуск pstree завершен

Глядя на снимок экрана, здесь можно увидеть несколько демонов: **udisksd** , **gvfsd** , **systemd** , **logind** и некоторые другие.

Наш список процессов был достаточно длинным, поэтому список не мог уместиться в одном окне терминала, но мы можем прокручивать его с помощью мыши или клавиш курсора:

![демон pstree](https://itsfoss.com/wp-content/uploads/2021/05/daemon_pstree2.png)

демон — верхняя часть pstree

## Порождение демонов

![демоны](https://itsfoss.com/wp-content/uploads/2021/05/demons-800x400.jpg)

Изображение только для репрезентативных целей

Опять же, демон — это процесс, работающий в фоновом режиме и обычно неподконтрольный пользователю. Говорят, что у демона _нет управляющего терминала_ .

Процесс _._ — это работающая программа В конкретный момент времени он может быть запущенным, спящим или зомбированным (процесс, завершивший свою задачу, но ожидающий, пока его родительский процесс примет возвращаемое значение).

В Linux существует три типа процессов: интерактивный, пакетный и демон.

_Интерактивные процессы_ — это те, которые запускаются пользователем в командной строке, называются интерактивными процессами.

_Пакетные процессы_ — это процессы, не связанные с командной строкой и представленные в списке процессов. Думайте об этом как о «группах задач». Это лучше всего в то время, когда использование системы низкое. Резервное копирование системы, например, обычно выполняется ночью, поскольку дневные сотрудники не используют систему. Когда я был штатным системным администратором, я часто запускал по ночам инвентаризацию использования диска, сценарии анализа поведения системы и т. д.

Интерактивные процессы и пакетные задания _не_ являются демонами, хотя они могут работать в фоновом режиме и могут выполнять некоторую работу по мониторингу. Ключевым моментом является то, что эти два типа процессов включают человеческий ввод через своего рода терминальное управление. Демонам не нужен человек, чтобы запустить их.

Мы знаем, что _демон_ — это компьютерная программа, которая работает как фоновый процесс, а не находится под непосредственным контролем интерактивного пользователя. Когда загрузка системы завершена, процесс инициализации системы начинает _порождать_ (создавать) демонов с помощью метода, называемого _разветвлением_ , что устраняет необходимость в терминале (именно это подразумевается под _отсутствием управления терминалом_ ).

Я не буду вдаваться в подробности процесса разветвления, но надеюсь, что смогу быть достаточно кратким, чтобы показать небольшую справочную информацию, чтобы описать, что делается. Хотя существуют и другие методы создания процессов, традиционно в Linux способ создания процесса заключается в создании копии существующего процесса для создания дочернего процесса. Затем выполняется системный вызов exec для запуска другой программы.

Между прочим , термин « _форк_ » не является произвольным. Он получил свое название от языка программирования C. Одна из библиотек, которые использует C, называется стандартной библиотекой, содержащей методы для выполнения операционных служб. Один из этих методов, называемый _fork_ , предназначен для создания новых процессов. Процесс, который инициирует ответвление, считается родительским процессом вновь созданного дочернего процесса.

Процесс, создающий демонов, называется инициализацией (называется `init`) путем разветвления собственного процесса для создания новых. Сделано таким образом, `init`процесс является прямым родительским процессом.

Есть еще один способ вызвать демона, а именно, чтобы другой процесс развил дочерний процесс, а затем _умер_ (термин, часто используемый вместо _exit_ ). Когда родитель умирает, дочерний процесс становится _сиротой_ . Когда дочерний процесс становится сиротой, он усыновляется `init`процесс.

Если вы слышали обсуждения или читали онлайн-материалы о демонах, имеющих «идентификатор родительского процесса 1», вот почему. Некоторые демоны не создаются во время загрузки, а создаются позже другим процессом, который умер, и `init`принял его.

Важно, чтобы вы не перепутали его с _зомби_ . Помните, что зомби — это дочерний процесс, завершивший свою задачу и ожидающий, пока родитель примет статус выхода.

## Примеры демонов Linux

![линукс-демон](https://itsfoss.com/wp-content/uploads/2021/05/linux-daemon-1.png)

Опять же, наиболее распространенный способ определить демона Linux — найти службу, оканчивающуюся на букву _d_ . Вот несколько примеров демонов, которые могут работать в вашей системе. Вы сможете увидеть, что демоны создаются для выполнения определенного набора задач:

`systemd`— основная цель этого демона — унифицировать конфигурацию и поведение службы в дистрибутивах Linux.

`rsyslogd`– используется для регистрации системных сообщений. Это более новая версия `syslogd`наличие ряда дополнительных функций. Он поддерживает ведение журнала как в локальных, так и в удаленных системах.

`udisksd`– обрабатывает такие операции, как запрос, монтирование, размонтирование, форматирование или отсоединение устройств хранения, таких как жесткие диски или флэш-накопители USB.

`logind`— крошечный демон, который различными способами управляет логинами и местами пользователей.

`httpd`– диспетчер службы HTTP. Обычно это выполняется с программным обеспечением веб-сервера, таким как Apache.

`sshd`– Демон, отвечающий за управление сервисом SSH. Это используется практически на любом сервере, который принимает SSH-соединения.

`ftpd`– управляет службой FTP – FTP или протокол передачи файлов – широко используемый протокол для передачи файлов между компьютерами; один действует как клиент, другой действует как сервер.

`crond`– демон планировщика для действий, зависящих от времени, таких как обновления программного обеспечения или проверки системы.

## Каково происхождение слова демон?

Когда я впервые начал писать эту статью, я планировал рассказать только о том, что такое демон, и на этом остановиться. Я работал с UNIX до появления Linux. В то время я представлял демона таким, каким он был: фоновым процессом, выполняющим системные задачи. Меня совершенно не интересовало, как он получил свое название. С дополнительным разговором о других вещах, таких как зомби и сироты, я просто понял, что у создателей операционной системы было извращенное чувство юмора (очень похожее на мое).

Я всегда провожу некоторое исследование каждой статьи, которую пишу, и я был удивлен, узнав, что, по-видимому, многие другие люди действительно хотели знать, как появилось это слово и почему.

Это слово, безусловно, вызвало некоторое любопытство, и, прочитав несколько оживленных обменов мнениями, я признаю, что мне тоже стало любопытно. Выполните поиск по значению или этимологии слова (происхождению слов), и вы найдете несколько ответов.

В интересах внести свой вклад в обсуждение, вот мое мнение по этому поводу.

Самая ранняя форма слова «демон» записывалась как « _даймон_ », форма ангела-хранителя — духи-помощники, которые помогали формировать характер людей, которым они помогали. Сократ утверждал, что у него есть тот, который служил ему ограниченным образом, но правильно. Даймон Сократа только говорил ему, когда держать рот на замке. Сократ описал своего даймона во время судебного процесса в 399 г. до н.э., поэтому вера в даймонов существует уже довольно давно. Иногда даймон пишется как daemon. _Даймон_ и _демон_ здесь означают одно и то же.

В то время как _демон_ — это слуга, _демон_ — это злой персонаж из Библии. Различия в написании являются преднамеренными и, по-видимому, были приняты в 16 веке. Демоны — хорошие парни, а демоны — плохие.

Использование слова «демон» в вычислительной технике началось в 1963 году. [Проект MAC](https://www.britannica.com/topic/Project-Mac) является сокращением от « _Проект по математике и вычислениям_ » и был создан в Массачусетском технологическом институте. Именно здесь слово «демон» [вошло в обиход](https://ei.cs.vt.edu/%7Ehistory/Daemon.html) для обозначения любого системного процесса, который отслеживает другие задачи и выполняет заранее определенные действия в зависимости от их поведения. Слово «демон» было названо в [честь демона Максвелла](https://www.britannica.com/science/Maxwells-demon) .

Демон Максвелла — результат мысленного эксперимента. В 1871 году [Джеймс Клерк Максвелл](https://www.britannica.com/biography/James-Clerk-Maxwell) представил разумное и находчивое существо, способное наблюдать и направлять движение отдельных молекул в определенном направлении. Цель мыслительного упражнения состояла в том, чтобы показать возможность противоречия второму закону термодинамики.

Я видел некоторые комментарии о том, что слово «демон» является аббревиатурой от `Disk And Executive MONitor`. Первоначальные пользователи слова «демон» [никогда не использовали его для этой цели](https://ei.cs.vt.edu/%7Ehistory/Daemon.html) , поэтому идея аббревиатуры, я считаю, неверна.

![beastie](https://itsfoss.com/wp-content/uploads/2021/05/Beastie.jpg)

Наконец, чтобы закончить это на легкой ноте, есть талисман BSD: демон, имеющий вид демона. Демон BSD был назван в честь программных демонов, но получил свое название из-за игры со словом.

Имя демона — _Beastie_ . Я еще не исследовал это полностью (пока), но я нашел один комментарий, в котором говорится, что Beastie происходит от неразборчивости букв, _BSD_ . Попытайся; Я сделал. Произносите буквы так быстро, как только можете, и вы получите звук, очень похожий на _beastie_ .

Beastie часто можно увидеть с трезубцем, который символизирует разветвление процессов демоном.