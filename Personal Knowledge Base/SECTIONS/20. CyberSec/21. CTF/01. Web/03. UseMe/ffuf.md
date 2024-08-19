### Введение в Ffuf

Если говорить проще, фаззинг можно назвать в некоторой степени «причудливым брутфорсом». Однако вы можете фаззингить то, что вы не можете брутфорсить. Фаззинг — это использование инструментов безопасности для автоматизации ввода данных, которые мы предоставляем, в такие вещи, как веб-сайты или программные приложения. Фаззинг — чрезвычайно эффективный процесс, поскольку компьютеры могут выполнять трудоемкие действия, такие как поиск скрытых файлов/папок, пробовать разные имена пользователей и пароли, гораздо быстрее, чем человек (и готов это делать...)

Плохо построенные приложения часто не могут обрабатывать данные так, как им положено, при интенсивной нагрузке. Более того, данные, которые мы анализируем в приложении, могут быть интерпретированы и выполнены (вместо того, чтобы быть обработанными правильно, т. е. системными командами). Мы можем использовать фаззинг, чтобы заставить приложение вызвать то, что известно как состояние ошибки, когда этим может злоупотребить тестировщик на проникновение или охотник за ошибками.

Ffuf — это мощный и быстрый веб-фаззер, написанный на Go. Это позволяет исследователям безопасности и тестировщикам на проникновение обнаруживать скрытые файлы, каталоги и другие уязвимости веб-приложений, выполняя рекурсивный поиск и поиск методом перебора. Ffuf известен своей скоростью и гибкостью, что делает его отличным инструментом для испытаний CTF.

### Вызов CTF

Давайте углубимся в задачу CTF, которую мы будем решать с помощью Ffuf. Задача заключается в поиске скрытых каталогов и файлов в веб-приложении, размещенном по адресу . Мы будем использовать Ffuf для выполнения фаззинга и обнаружения этих скрытых ресурсов.http://83.136.250.34:53339

### Шаг 1: Обнаружение скрытых каталогов

Чтобы начать задачу, мы выполняем Ffuf со списком слов, содержащим общие имена каталогов и целевой URL-адрес . Команда выглядит следующим образом: http://83.136.250.34:53339/FUZZ

```bash
sudo ffuf -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://83.136.250.34:53339/FUZZ

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.4.1-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://83.136.250.34:53339/FUZZ
 :: Wordlist         : FUZZ: /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________
```

На основе выходных данных Ffuf обнаруживает следующие каталоги:

 - /blog (Статус: 301, Размер: 322)
 - /forum (Статус: 301, Размер: 323)

Каталог, который нам нужно найти на этом шаге: ./forum

### Шаг 2: Фаззинг каталога «/blog»

На втором этапе нам нужно размыть каталог и найти все страницы в нем. Ожидается, что одна из этих страниц будет содержать флаг. Мы снова используем Ffuf для выполнения операции фаззинга со списком слов и целевым URL-адресом . Команда выглядит следующим образом:/bloghttp://83.136.250.34:53339/blog/FUZZ.php

```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://83.136.250.34:53339/blog/FUZZ.php 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.4.1-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://83.136.250.34:53339/blog/FUZZ.php
 :: Wordlist         : FUZZ: /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________
```

Ffuf выполняет операцию фаззинга, отправляя несколько запросов на целевой URL-адрес с разными именами файлов. Он анализирует ответы и предоставляет выходные данные с подробностями, аналогичными предыдущему шагу.

После процесса фаззинга Ffuf обнаруживает следующую страницу:

 - /blog/home.php (Статус: 200, Размер: 1046, Слов: 438, Строк: 58)

Чтобы найти флаг, переходим на обнаруженную страницу: . Флаг показан на этой странице:http://83.136.250.34:53339/blog/home.php

Флаг: HTB{bru73_f0r_c0mm0n_*********}

Шаг 3: Поиск дополнительных файлов/каталогов

На третьем шаге продолжаем поиск дополнительных файлов и каталогов. Один из этих ресурсов должен предоставить нам другой флаг. Нам нужно применить полученные знания и повторить процесс.

После дальнейшего изучения мы находим следующий URL-адрес, содержащий второй флаг:

http://94.237.62.6:51052/forum/flag.php

Флаг: HTB{fuzz1n6_7h3_****}

### Шаг 4: Открытие поддомена магазина сувениров

На последнем этапе мы проводим тест фаззинга поддомена, чтобы обнаружить онлайн-магазин сувениров HackTheBox. Мы используем Ffuf со списком слов поддоменов и целевым URL-адресом . Команда выглядит следующим образом:hackthebox.euhttp://FUZZ.hackthebox.eu/

```bash
ffuf -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://FUZZ.hackthebox.eu/  
  
/'___\ /'___\ /'___\  
/\ \__/ /\ \__/ __ __ /\ \__/  
\ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\  
\ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/  
\ \_\ \ \_\ \ \____/ \ \_\  
\/_/ \/_/ \/___/ \/_/  
  
v1.4.1-dev  
________________________________________________  
  
:: Method : GET  
:: URL : http://FUZZ.hackthebox.eu/  
:: Wordlist : FUZZ: /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt  
:: Follow redirects : false  
:: Calibration : false  
:: Timeout : 10  
:: Threads : 40  
:: Matcher : Response status: 200,204,301,302,307,401,403,405,500  
________________________________________________  
```

- `**store.hackthebox.eu**` (Статус: 200, Размер: ..., Слова: ..., Строки: ...)

Полный домен магазина HackTheBox Swag Shop: .`store.hackthebox.eu`

### Шаг 5: Фаззинг VHost

Первая задача требует, чтобы мы выполнили сканирование фаззинга VHost в домене «academy.htb» и определили любые дополнительные VHosts. Для этого мы используем инструмент со следующей командой:`**ffuf`

```bash
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://94.237.59.206:42671/ -H 'Host: FUZZ.academy.htb' -ms 0  
  
        /'___\  /'___\           /'___\         
       /\ \__/ /\ \__/  __  __  /\ \__/         
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\        
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/        
         \ \_\   \ \_\  \ \____/  \ \_\         
          \/_/    \/_/   \/___/    \/_/         
  
       v2.0.0-dev  
________________________________________________  
  
 :: Method           : GET  
 :: URL              : http://94.237.59.206:42671/  
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt  
 :: Header           : Host: FUZZ.academy.htb  
 :: Follow redirects : false  
 :: Calibration      : false  
 :: Timeout          : 10  
 :: Threads          : 40  
 :: Matcher          : Response size: 0  
________________________________________________  
  
[Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 59ms]  
    * FUZZ: test  
  
[Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 4155ms]  
    * FUZZ: admin  
  
:: Progress: [4989/4989] :: Job [1/1] :: 578 req/sec :: Duration: [0:00:11] :: Errors: 0 ::
```

Результат сканирования показывает существование двух VHosts: '' и ''.`test.academy.htb``admin.academy.htb`

### Шаг 6: Фаззинг параметров

Во второй задаче нам нужно запустить сканирование фаззинга параметров на определенной веб-странице и определить допустимый параметр. С помощью инструмента выполняем следующую команду:`ffuf`

```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://admin.academy.htb:34138/admin/admin.php?FUZZ=key -fs 798  
user
```

Выходные данные сканирования указывают на то, что параметр '' принимается веб-страницей.`**key`

### Шаг 7: Создание списка слов и POST-запрос

Для третьей задачи мы должны создать список слов под названием «», определить принятое значение с помощью фаззингового сканирования и использовать его в запросе «» с «curl» для получения флага. Давайте выполним следующие действия:`ids.txt``POST`

1. Создайте список слов «ids.txt» с нужными значениями.
2. Выполните нечеткое сканирование, используя для определения допустимого значения параметра '':`ffuf``id`

ffuf -w ids.txt:FUZZ -u http://admin.academy.htb:34138/admin/admin.php -X POST -d 'id=73' -H 'Content-Type: application/x-www-form-urlencoded'

Ответ содержит флаг: .`**HTB{p4r4m373r_fuzz1n6_15_****}`

### Оценка навыков — веб-фаззинг

### Шаг 1: Фаззинг поддоменов/VHost и расширений

В четвертой задаче нам поручено запустить сканирование фаззинга поддоменов/VHost на '' и идентифицировать все поддомены. Мы снова нанимаем:`.academy.htb``ffuf`

```bash
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://94.237.55.114:47287/ -H 'Host: FUZZ.academy.htb' -ms 0  
  
        /'___\  /'___\           /'___\         
       /\ \__/ /\ \__/  __  __  /\ \__/         
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\        
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/        
         \ \_\   \ \_\  \ \____/  \ \_\         
          \/_/    \/_/   \/___/    \/_/         
  
       v2.0.0-dev  
________________________________________________  
  
 :: Method           : GET  
 :: URL              : http://94.237.55.114:47287/  
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt  
 :: Header           : Host: FUZZ.academy.htb  
 :: Follow redirects : false  
 :: Calibration      : false  
 :: Timeout          : 10  
 :: Threads          : 40  
 :: Matcher          : Response size: 0  
________________________________________________  
  
[Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 63ms]  
    * FUZZ: test  
  
[Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 61ms]  
    * FUZZ: archive  
  
[Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 67ms]  
    * FUZZ: faculty  
  
:: Progress: [4989/4989] :: Job [1/1] :: 578 req/sec :: Duration: [0:00:09] :: Errors: 0 ::
```

Выходные данные сканирования показывают три поддомена: ',' ',' и '.'`test.academy.htb``archive.academy.htb``faculty.academy.htb`

Перед запуском сканирования фаззинга страниц рекомендуется выполнить сканирование расширения. Цель состоит в том, чтобы определить различные расширения, принимаемые доменами. Мы можем сделать это с помощью следующей команды:

```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://94.237.55.114:47287/indexFUZZ  
  
  
        /'___\  /'___\           /'___\         
       /\ \__/ /\ \__/  __  __  /\ \__/         
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\        
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/        
         \ \_\   \ \_\  \ \____/  \ \_\         
          \/_/    \/_/   \/___/    \/_/         
  
       v2.0.0-dev  
________________________________________________  
  
 :: Method           : GET  
 :: URL              : http://94.237.55.114:47287/indexFUZZ  
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/web-extensions.txt  
 :: Follow redirects : false  
 :: Calibration      : false  
 :: Timeout          : 10  
 :: Threads          : 40  
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500  
________________________________________________  
  
[Status: 200, Size: 985, Words: 423, Lines: 55, Duration: 63ms]  
    * FUZZ: .php  
  
[Status: 403, Size: 281, Words: 20, Lines: 10, Duration: 61ms]  
    * FUZZ: .phps  
  
:: Progress: [40/40] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::The scan output indicates that the extensions ‘.php’ and ‘.phps’ are accepted.
```

```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://faculty:47287/indexFUZZ  
.php7
```

На одной из страниц, которые вы определите, должно быть написано «У вас нет доступа!». Что такое полный URL-адрес страницы?

```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u <http://faculty.academy.htb:47287/FUZZ> -recursion -recursion-depth 1 -e .php -v -t 80  
index.hph7  
courses  
linux-security.php7
```

`http://faculty.academy.htb:47287/courses/linux-security.php7`

### Задача 5: Идентификация параметров и фаззинг

В пятой задаче нам нужно определить параметры, принимаемые конкретной страницей, полученной на предыдущем шаге. Для этого мы выполняем следующую команду:

```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://faculty.academy.htb:PORT/courses/linux-security.php7 -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded'  
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://faculty.academy.htb:30796/courses/linux-security.php7 -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs 774
```

Выходные данные сканирования показывают два параметра: '' и '.'`user``username`

Далее от нас требуется размыть идентифицированные параметры с рабочими значениями, чтобы получить флаг. Мы можем сделать это с помощью следующей команды:

```bash
ffuf -w /opt/useful/SecLists/Usernames/xato-net-10-million-usernames.txt:FUZZ -u http://faculty.academy.htb:30401/courses/linux-security.php7 -X POST -d 'username=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded'  
ffuf -w /opt/useful/SecLists/Usernames/xato-net-10-million-usernames.txt:FUZZ -u http://faculty.academy.htb:30401/courses/linux-security.php7 -X POST -d 'username=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -fs 781
```

Ответ содержит флаг: `HTB{w3b_fuzz1n6_******}`

### Заключение

В этой статье мы рассмотрели процесс решения различных проблем веб-фаззинга, возникающих в соревновании CTF. Мы узнали, как выполнять фаззинг VHost, фаззинг параметров, создание списков слов и сканирование фаззинга для поддоменов, расширений и параметров. Выполнив эти шаги и используя инструмент, мы успешно получили нужные флаги. Веб-фаззинг является важнейшим навыком в области кибербезопасности, позволяющим нам обнаруживать уязвимости и потенциальные векторы атак.`ffuf`

---