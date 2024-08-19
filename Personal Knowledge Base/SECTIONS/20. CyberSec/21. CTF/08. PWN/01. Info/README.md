
# Введение 

Проблемы PWN — это тип задач CTF, которые требуют использования двоичного файла, обычно работающего на удаленном сервере. Это можно сделать, воспользовавшись уязвимостью в двоичном файле или используя уязвимость в двоичном файле для получения доступа к системе.

Задания данной категории чаще всего нацелены на эксплуатацию бинарных уязвимостей в исполняемых файлах под различные архитектуры и ОС. По большей части задания затрагивают уязвимости переполнения буфера (куча, стек), форматной строки, UAF, и другие повреждения памяти. Зачастую для задач PWN вам потребуется получить доступ к удаленному серверу, а затем использовать двоичный файл на этом сервере. Это делается путем подключения к серверу с помощью такого инструмента, как netcat, а затем отправки команд на сервер.


**Exploiting** или **Pwn** ("бинарная эксплуатация", "эксплойтинг", "пвн") — это категория задач, в которых, как правило, нужно искать и эксплуатировать уязвимости в скомпилированных приложениях. Чаще всего это уязвимости повреждения памяти (memory corruption).

Эта категория в каком-то смысле противопоставляется категории Web, в которой обычно стоит задача взломать приложение на языке высокого уровня (типа PHP), т.е. всё происходит на уровне интерпретации скрипта, а не на уровне физической памяти. Однако, порой в категорию Pwn включают и приложения на скриптовых языках. Это может быть, к примеру, обход песочницы (jail) на языке Python. Песочницей называют ограниченную среду, в которой разрешены только определённые команды. Целью решения таска обычно является обойти это ограничение и прочитать какую-то конфиденциальную информацию (флаг).

Надо отметить, что в последние годы тематика CTF-соревнований заметно укоренилась именно в области пвна. На топовых соревнованиях задачи зачастую очень сложные, и их решают известные профессионалы, исследователи, разработчики кибероружия. Например, одним из сильнейших пвнеров (и цтферов вообще) является https://en.wikipedia.org/wiki/George_Hotz, активно участвовавший в цтфах в 2013-2014 годах. Сильнейшей командой является команда PPP (Plaid Parliament of Pwning) родом из университета CMU, которая, как нетрудно догадаться, тоже специализируется в пвне.

## Термины 

В контексте CTF (Capture The Flag) термин "pwn" используется для обозначения успешного взлома или эксплуатации уязвимости в программном обеспечении. Это может быть использовано как существительное ("pwnage") или глагол ("to pwn"). "Pwn" в контексте компьютерной безопасности и соревнований Capture The Flag (CTF) означает эксплуатацию уязвимостей в программном обеспечении или операционной системе для получения контроля над системой или выполнения определенных задач. Это термин, происходящий из ошибки в написании слова "own" (владеть) и используется для выражения полного контроля или взлома целевой системы. В соревнованиях CTF, задания типа "pwn" требуют от участников создания и использования специальных программ (эксплойтов), чтобы взломать их цели. Основная цель - найти уязвимости и использовать их в свою пользу, чтобы получить доступ к системе или выполнить определенные действия, определенные правилами соревнования. 

Когда участник CTF говорит, что они "pwned" (взломали) какую-то систему, это означает, что они смогли получить доступ к защищенной информации или выполнить код на удаленной машине, используя уязвимость в программе или сервисе. Успешный "pwn" обычно требует навыков в области эксплойт-разработки, реверс-инжиниринга и знаний о безопасности программного обеспечения.  Таким образом, "pwn" в CTF означает победу или успешное проникновение в систему путем эксплуатации уязвимости. Термин "own" в контексте CTF (Capture The Flag) также используется для обозначения успешного взлома или контроля над системой, устройством или данными. Это может быть использовано как глагол ("to own") или существительное ("ownage").

Когда участник CTF говорит, что они "owned" (взломали) какую-то систему, это означает, что они полностью контролируют эту систему, устройство или данные. Успешный "own" обычно означает, что участник получил полный доступ к системе или данным, а также могут выполнить различные действия на удаленной машине. Таким образом, "own" в CTF также означает победу или успешное проникновение в систему и контроль над ней.

В контексте CTF, "own" в "pwn" означает "взломать" или "компрометировать". Pwn - это категория задач CTF, где вам нужно найти и использовать уязвимости в скомпилированных приложениях, чтобы получить контроль над системой или выполнить другие задачи.

Вот несколько примеров того, что означает "own" в pwn:

- Взломать сервер: Вы можете найти уязвимость в программном обеспечении сервера, чтобы получить доступ к его файлам или выполнить команды на нем.

- Захватить флаг: Во многих задачах pwn вам нужно найти "флаг" - секретный файл или строку текста, спрятанный в приложении.

- Получить root-доступ: Вы можете использовать уязвимость, чтобы повысить свои привилегии до root-пользователя, что даст вам полный контроль над системой.

Pwn - это сложная категория CTF, но она может быть очень интересной и полезной. Она учит вас основам безопасности и эксплуатации уязвимостей, а также навыкам реверс-инжиниринга и программирования.


# Ближе к делу

Наиболее известным и распространённым случаем повреждения памяти является переполнение буфера. Если объяснить в двух словах, переполнение буфера возникает тогда, когда приложение принимает на вход строку и записывает её в некоторую выделенную область памяти (буфер), недостаточно проверяя её длину.

Таким образом, хакер может выйти за границы буфера и переписать какие-то иные участки памяти, в которых могут быть важные данные. Классический способ эксплуатации — это перетирание адреса возврата (return address). Это адрес памяти, на который программа "перепрыгнет" после завершения выполнения текущей функции.

Суть эксплойта в том, что хакер записывает в буфер любой код, который он хочет выполнить, далее выходит за границу буфера и меняет адрес возврата на адрес буфера. Таким образом, после выхода из текущей функции программа перепрыгнет на буфер, и выполнится код, который хакер туда записал.

Обычно в качестве условия задачи даётся бинарник (скомпилированный исполняемый файл программы) и адрес (хост и порт) сервера, на котором этот бинарник висит. Иногда даётся и исходный код приложения. Участнику нужно проанализировать приложение (дизассемблировать, декомпилировать или читать исходный код) и разработать эксплойт, т.е. программу, которая "заставляет" это уязвимое приложение выполнить произвольный код (вызвать шелл). Далее нужно при помощи этого эксплойта заставить сервер организаторов выдать флаг.

В простых случаях сам эксплойт может состоять всего из нескольких байт. Это может быть некоторое количество произвольных байтов для забивания буфера, а затем адрес какой-то функции, которая выдаёт флаг. Если этот адрес перезапишет адрес возврата, программа отдаст флаг.

Иногда даже для относительно непростых задач эксплойт пишется в одну строчку, но найти саму уязвимость и придумать цепочку вызовов для выполнения нужного действия не так легко.

Есть книга Д. Эриксона "Хакинг. Искусство эксплойта" в русском переводе. В ней очень доступно описано введение в эксплуатацию уязвимостей повреждения памяти. Также затронута сетевая безопасность и криптоанализ.

**Простые примеры для понимания:**

- [https://ru.wikipedia.org/wiki/Переполнение_буфера](https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B5%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B1%D1%83%D1%84%D0%B5%D1%80%D0%B0)
- [http://www.thegeekstuff.com/2013/06/buffer-overflow/](http://www.thegeekstuff.com/2013/06/buffer-overflow/)
- [https://www.owasp.org/index.php/Buffer_overflow_attack](https://www.owasp.org/index.php/Buffer_overflow_attack)
- [http://www-inst.eecs.berkeley.edu/~cs161/fa08/papers/stack_smashing.pdf](http://www-inst.eecs.berkeley.edu/~cs161/fa08/papers/stack_smashing.pdf)
- [https://sploitfun.wordpress.com/2015/06/26/linux-x86-exploit-development-tutorial-series/](https://sploitfun.wordpress.com/2015/06/26/linux-x86-exploit-development-tutorial-series/)

**Хорошие ресурсы для тренировки навыков этой категории:**

- [http://io.smashthestack.org/](http://io.smashthestack.org/)
- [https://exploit.education/](https://exploit.education/)
- [http://overthewire.org/wargames/](http://overthewire.org/wargames/)
- [https://ropemporium.com/](https://ropemporium.com/)
- [https://github.com/xairy/easy-linux-pwn](https://github.com/xairy/easy-linux-pwn)
- [https://github.com/shellphish/how2heap](https://github.com/shellphish/how2heap)
- [https://www.root-me.org/en/Challenges/App-System/](https://www.root-me.org/en/Challenges/App-System/)
- [https://github.com/atxsinn3r/VulnCases](https://github.com/atxsinn3r/VulnCases)
- [https://pwnable.tw/](https://pwnable.tw/)
- [https://pwnable.kr/](https://pwnable.kr/)
- [https://pwnable.xyz/](https://pwnable.xyz/)



[**Social Engineering**](https://tglink.ru/Social_engineering_club) - Канал посвященный психологии, социальной инженерии, профайлингу, НЛП, Хакингу, Анонимности и безопасности в сети интернет, Даркнету и все что с ним связано. Добро пожаловать ;-)

[**S.E.Book**](https://tglink.ru/S_E_Book) - Литература социального инженера.  
  
[**@Social_Engineering_bot**](https://tglink.ru/Social_engineering_club/556) - Бот обратной связи.



1. [Создаём Evil архив | WinRAR Path Traversal](https://telegra.ph/Sozdayom-Evil-arhiv-08-18)
2. [НЛП. Как противостоять манипуляциям?](https://telegra.ph/NLP-Kak-protivostoyat-manipulyaciyam-08-17)
3. [Эксплуатируем CVE 2019-8646.](https://t.me/Social_engineering_club/616)
4. [Shodan. HP iLO RCE.](https://telegra.ph/Shodan-HP-iLO-RCE-08-15)
5. [Получаем доступ к андроиду через зараженный APK.](https://telegra.ph/Poluchaem-dostup-k-androidu-cherez-zarazhennyj-APK-08-11)
6. [Подмена буфера обмена.](https://telegra.ph/Podmena-bufera-obmena-08-10)