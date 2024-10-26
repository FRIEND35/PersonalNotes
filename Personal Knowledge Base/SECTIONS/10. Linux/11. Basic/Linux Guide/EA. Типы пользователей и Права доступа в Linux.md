В операционной системе Linux есть много отличных функций безопасности, но она из самых важных - это система прав доступа к файлам. Linux, как последователь идеологии ядра Linux в отличие от Windows, изначально проектировался как многопользовательская система, поэтому права доступа к файлам в linux продуманы очень хорошо.

И это очень важно, потому что локальный доступ к файлам для всех программ и всех пользователей позволил бы вирусам без проблем уничтожить систему. Но новым пользователям могут показаться очень сложными новые права на файлы в linux, которые очень сильно отличаются от того, что мы привыкли видеть в Windows. В этой статье мы попытаемся разобраться в том как работают права файлов в linux, а также как их изменять и устанавливать.

По замыслу создателей, [**Linux**](https://ravesli.com/chto-takoe-linux-ego-struktura-i-preimushhestva/ "Что такое Linux? Его преимущества")-системы — это многопользовательские операционные системы, т.е. позволяющие нескольким пользователям работать с одной системой, не мешая друг другу. Но пользователи, совместно использующие доступ к файлам, рискуют раскрыть секретную информацию или даже потерять данные, если другие пользователи получат доступ к их файлам или каталогам. Чтобы решить эту проблему, в Linux добавили механизмы владения и прав доступа к файлам (или каталогам), чтобы обозначить, какие полномочия каждый пользователь имеет над определенным файлом (или каталогом).



Теперь представим такую ситуацию: пусть у нас есть два пользователя А и Б, требуется сделать так, чтобы пользователь А не мог повлиять на файл, содержащий жизненно важную информацию/данные пользователя Б. Возникает вопрос: «Как Linux различает данные категории пользователей?». Например, вы не хотите, чтобы ваш коллега, который работает на вашем компьютере с Linux, просматривал ваши изображения. Вот тут-то на сцену и выходят права доступа, определяющие поведение пользователей.


# Права доступа/Разрешения

Каждый файл и каталог в Linux имеет следующие **три типы разрешений** для всех трех вышеописанных категорий пользователей:

   - **Чтение/Просмотр** (**_R_**_ead_) — дает право открывать и читать файл. Разрешение на чтение каталога дает возможность просматривать его содержимое. Инными словами, разрешает получать содержимое файла, но на запись нет. Для каталога позволяет получить список файлов и каталогов, расположенных в нем;

   - **Запись/Изменение** _(_**_W_**_rite)_ — дает право изменять содержимое файла. Разрешение на запись в каталог дает право добавлять, удалять и переименовывать файлы, хранящиеся в каталоге. Рассмотрим сценарий, в котором у вас есть разрешение на запись в файл, но нет разрешения на запись в каталог, где хранится файл. Вы сможете изменить содержимое файла, но вы не сможете переименовать, переместить или удалить файл из каталога. Другими словами, разрешает записывать новые данные в файл или изменять существующие, а также позволяет создавать и изменять файлы и каталоги;

   - **Выполнение** (_e**X**ecute_) — в Linux вы не сможете запустить программу, если не задано разрешение на _выполнение_, но вы все равно сможете видеть/изменять программный код (при условии, что установлены разрешения на чтение и запись), но не запускать его. Простым языком, вы не можете выполнить программу, если у нее нет флага выполнения. Этот атрибут устанавливается для всех программ и скриптов, именно с помощью него система может понять, что этот файл нужно запускать как программу.


Но все эти права были бы бессмысленными, если бы применялись сразу для всех пользователей. Поэтому каждый файл имеет три категории пользователей, для которых можно устанавливать различные сочетания прав доступа:


# Типы пользователей в Linux

Каждый файл и каталог в Linux имеет **три категории пользователей**:

   - **Владелец** — пользователь, создавший файл/каталог. Простыми словами, набор прав для владельца файла, пользователя, который его создал или сейчас установлен его владельцем. Обычно владелец имеет все права, чтение, запись и выполнение.

   - **Группа** — все пользователи, принадлежащие к некоторой заданной группе, будут иметь одинаковые разрешения группы на доступ к файлу. Предположим, у вас есть проект, в котором несколько человек требуют доступа к файлу. Вместо того, чтобы вручную назначать права доступа каждому пользователю, вы можете добавить их всех в одну группу и назначить права доступа группы к файлу таким образом, чтобы только члены данной группы (и никто другой) могли читать или изменять файлы. Даже если вы единственный пользователь системы, вы все равно будете частью многих групп. Другими словами, любая группа пользователей, существующая в системе и привязанная к файлу. Но это может быть только одна группа и обычно это группа владельца, хотя для файла можно назначить и другую группу.

   - **Остальные/Другие** (все остальные пользователи) — любой другой пользователь, имеющий доступ к файлу. Он не является владельцем файла, и не принадлежит к группе, которая могла бы владеть файлом. Простым языком, все пользователи, кроме владельца и пользователей, входящих в группу файла.

Другими словами, _Владелец_ — это один пользователь, _Группа_ — это совокупность пользователей, а _Остальные_ — совокупность из всех остальных пользователей системы.

Именно с помощью этих наборов полномочий устанавливаются права файлов в linux. Каждый пользователь может получить полный доступ только к файлам, владельцем которых он является или к тем, доступ к которым ему разрешен. Только пользователь Root может работать со всеми файлами независимо от их набора их полномочий.

Но со временем такой системы стало не хватать и было добавлено еще несколько флагов, которые позволяют делать файлы не изменяемыми или же выполнять от имени суперпользователя, их мы рассмотрим ниже:

## Специальные права доступа к файлам в Linux

Для того, чтобы позволить обычным пользователям выполнять программы от имени суперпользователя без знания его пароля была придумана такая вещь, как SUID и SGID биты. Рассмотрим эти полномочия подробнее.

- **SUID** - если этот бит установлен, то при выполнении программы, id пользователя, от которого она запущена заменяется на id владельца файла. Фактически, это позволяет обычным пользователям запускать программы от имени суперпользователя;

- **SGID** - этот флаг работает аналогичным образом, только разница в том, что пользователь считается членом группы, с которой связан файл, а не групп, к которым он действительно принадлежит. Если SGID флаг установлен на каталог, все файлы, созданные в нем, будут связаны с группой каталога, а не пользователя. Такое поведение используется для организации общих папок;

-  **Sticky-bit** - этот бит тоже используется для создания общих папок. Если он установлен, то пользователи могут только создавать, читать и выполнять файлы, но не могут удалять файлы, принадлежащие другим пользователям.

## Пример на практике

Рассмотрим следующий пример:

![[Pasted image 20221018091417.png]]

Здесь владелец (_diego_) файла _Адреса.txt_ (который я заранее создал в папке `_/home/diego/Документы_`) имеет доступ к его _«Просмотру и Изменению»_, в то время как другие члены его группы (её название совпадает с именем владельца — _diego_), а также все остальные пользователи, не входящие в эту группу, имеют доступ _«Только просмотр»_. Поэтому они могут открыть файл, но не могут вносить в него изменения.

Чтобы изменить права доступа к файлу, пользователь может открыть выпадающее меню и для каждой категории пользователей выбрать нужное разрешение. Кроме того, вы можете сделать файл _Исполняемым_, позволяя ему работать как программа, установив флажок `"Является выполняемым"`.

Конечно, вы можете посмотреть права доступа к файлам в Linux с помощью файлового менеджера. Все они поддерживают эту функцию, но так вы получите неполную информацию. Для максимально подробной информации обо всех флагах, в том числе специальных, нужно использовать команду ls с параметром -l. Все файлы из каталога будут выведены в виде списка, и там будут показаны все атрибуты и биты.

Чтобы узнать права на файл linux выполните такую команду, в папке где находится этот файл:

>`ls -l`

**_Примечание:_** Команда `ls` используется для вывода содержимого каталогов и информации о файлах. Ключ `–l` используется для вывода детальной информации о правах доступа, владельце, размере файла и пр.

Если применить команду `ls -l` к нашему файлу _Адреса.__txt_, то мы будем наблюдать такой вывод:

![[Pasted image 20221018091441.png]]

За права файлов в linux тут отвечают черточки. Первая это тип файла, который рассмотрен в отдельной статье. Дальше же идут группы прав сначала для владельца, для группы и для всех остальных. Всего девять черточек на права и одна на тип.

Рассмотрим подробнее, что значат условные значения флагов прав:

-   **---** - нет прав, совсем;
-   **--x** - разрешено только выполнение файла, как программы но не изменение и не чтение;
-   **-w-** - разрешена только запись и изменение файла;
-   **-wx** - разрешено изменение и выполнение, но в случае с каталогом, вы не можете посмотреть его содержимое;
-   **r--** - права только на чтение;
-   **r-x** - только чтение и выполнение, без права на запись;
-   **rw-** - права на чтение и запись, но без выполнения;
-   **rwx** - все права;
-   **--s** - установлен SUID или SGID бит, первый отображается в поле для владельца, второй для группы;
-   **--t** - установлен sticky-bit, а значит пользователи не могут удалить этот файл.


Выходные данные содержат следующую информацию:

![[Pasted image 20221018091454.png]]

Рассмотрим детально:

   - **Тип** — обозначает тип объекта. Это может быть обычный файл (`-`), каталог (`d`) или ссылка (`l`).

   - **Разрешения (права доступа)** — в этом поле отображается набор разрешений для файла, о которых мы поговорим ниже.

   - **Жесткая ссылка** — отображает количество ссылок, имеющихся у файла. По умолчанию устанавливается значение `1`.

   - **Владелец** — имя пользователя, который владеет файлом. Часто (но не всегда) совпадает с именем его создателя.

   - **Группа** — группа, имеющая доступ к файлу. Одновременно владеть файлом может только одна группа.

   - **Размер** — размер файла в байтах.

   - **Дата модификации** — дата и время последнего изменения файла.

   - **Имя файла**.

Информация о правах доступа к файлу сгруппирована в строку символов, перед которой стоит `-`. При этом каждая буква задает определенное разрешение, а именно:

   - `r` (_**r**ead_) — разрешение на _чтение/просмотр_ файла;

   - `w` (_**w**rite_) — разрешение на _запись/изменение_ файла;

   - `x` (_e**x**ecute_) — разрешение на _выполнение_ файла;

   - `–` — нет набора разрешений.

Пользователи, имеющие разрешение на _Чтение_, могут видеть содержимое файла (или файлов в каталоге), однако они не могут изменить его (или добавить/удалить файлы в каталоге). С другой стороны, те, у кого есть права на _Запись_, могут редактировать (добавлять и удалять) файлы. Наконец, возможность _Выполнения_ означает, что пользователь может запустить файл. Эта опция в основном используется для запуска скриптов.

Разрешения всегда идут именно в таком порядке, то есть `rwx`. А далее, они устанавливаются для всех трех категорий пользователей в порядке _Владелец, Группа_ и _Остальные/Другие_:

![[Pasted image 20221018091513.png]]

Итак, если вы вооружитесь вышеприведенной картинкой и посмотрите на вывод команды `ls –l`, то сможете сказать следующие вещи о правах доступа к файлу _Адреса.txt_:

>`-rw-r--r-- 1 diego diego 2 фев 17 21:15 /home/diego/Документы/Адреса.txt`

Что мы видим?

   - Владелец _diego_ имеет права на чтение и запись в файл.

   - Группа _diego_ имеет права только на чтение.

   - Остальным пользователям (всем, кто имеет доступ к системе) также доступно только чтение файла. Вам не нужно знать кто этот _другой_ пользователь, потому что к _другому_ относятся все остальные пользователи.

Теперь попробуем применить ту же самую команду `ls -l`, но к другому файлу:

>`diego@debian:~$ ls -l /bin/ping   -rwxr-xr-x 1 root root 77432 фев 2 20:49 /bin/ping`

Что мы видим?

  - Владельцем файла является пользователь _root_, который имеет права доступа на чтение, изменение и выполнение файла (`rwx`).

  - Все члены группы _root_ имеют права на чтение и выполнение файла (`r-x`).

   - Остальные пользователи тоже имеют права на чтение и выполнение файла (`r-x`).

Замечу, что один пользователь может быть членом нескольких групп, но только основная группа пользователя может быть назначена файлу. Основную группу пользователя можно найти с помощью команды `id`, например, `id -gn <имя_пользователя>`. Оставьте `имя_пользователя` пустым, если вы хотите получить информацию о своей собственной основной группе.

Теперь, когда вы знаете, как узнать права доступа к файлу, давайте посмотрим, каким образом можно сменить их и владельца файла.  


## Изменение прав доступа. Команда chmod

Представим, что вы не хотите, чтобы ваш коллега видел ваши личные изображения. Это может быть достигнуто путем изменения прав доступа к файлам с помощью команды `chmod` (сокр. от _«**ch**ange **mod**e»_). Используя эту команду, мы можем установить права доступа (_Чтение, Запись, Выполнение_) к файлу/каталогу для _Владельца_, _Группы_ и всех _Остальных_ пользователей.

Синтаксис команды `chmod` следующий:

>`chmod [разрешения] [имя файла]`

Существует два способа использования команды `chmod`: символьный и числовой.  

### Использование команды chmod в символьном режиме

Чтобы задать параметры разрешений для каждой отдельной категории пользователей, применяются следующие символы:

   - `u` — владелец;

   - `g` — группа;

   - `o` — остальные пользователи;

   - `a` — для всех трех категорий (_Владелец_ + _Группа_ + _Остальные_).

Действие может быть одно из двух, либо добавить - знак **"+"**, либо убрать - знак - **"-"**. Что касается самих прав доступа, то они аналогичны выводу утилиты ls: **r** - чтение, **w** - запись, **x** - выполнение, **s** - suid/sgid, в зависимости от категории, для которой вы его устанавливаете, **t** - устанавливает sticky-bit. 

А также используются следующие математические символы:

   - `+` — добавление разрешений;

   - `–` — удаление разрешений;

   - `=` — переопределение существующих разрешений новым значением.

Теперь, когда вы знаете, как это работает, давайте попробуем использовать команду `chmod` в символьном режиме и установим новые разрешения для ранее упомянутого файла _Адреса.__txt_ следующим образом:

   - чтение, запись и выполнение для _Владельца;_

   - чтение и запись для членов _Группы;_

   - чтение для _Остальных_ пользователей.

Например, всем пользователям полный доступ к файлу test5:

`chmod ugo+rwx test5`

Или заберем все права у группы и остальных пользователей:

`chmod go-rwx test5`

Дадим группе право на чтение и выполнение:

`chmod g+rx test5`

Остальным пользователям только чтение:

`chmod o+r test5`

Для файла test6 установим SUID:

`chmod u+s test6`

А для test7 - SGID:

`chmod g+s test7`


>`chmod u=rwx,g=rw,o=r /home/diego/Документы/Адреса.txt`

В результате мы получаем:

>`diego@debian:~$ chmod u=rwx,g=rw,o=r /home/diego/Документы/Адреса.txt   diego@debian:~$ ls -la /home/diego/Документы/Адреса.txt   -rwxrw-r-- 1 diego diego 2 фев 17 21:15 /home/diego/Документы/Адреса.txt`

Как видите, права доступа к файлу изменились с `-rw-r--r--` на `-rwxrw-r--`, что нам и требовалось.

А если мы теперь хотим убрать разрешение на чтение файла для пользователей, не входящих в нашу группу и не являющихся владельцем файла, то достаточно выполнить следующее:

>`chmod o-r /home/diego/Документы/Адреса.txt`

Результат:

>`diego@debian:~$ chmod o-r /home/diego/Документы/Адреса.txt   diego@debian:~$ ls -la /home/diego/Документы/Адреса.txt   -rwxrw---- 1 diego diego 2 фев 17 21:15 /home/diego/Документы/Адреса.txt`

Права доступа к файлу изменились с `-rwxrw-r--` на `-rwxrw----`.

Подумав, мы решаем дать полные права (за исключением права на выполнение) абсолютно всем пользователям системы, и выполняем команду:

>`diego@debian:~$ chmod a+rw-x /home/diego/Документы/Адреса.txt`

Результат:

`diego@debian:~$ chmod a+rw-x /home/diego/Документы/Адреса.txt   diego@debian:~$ ls -la /home/diego/Документы/Адреса.txt   -rw-rw-rw- 1 diego diego 2 фев 17 21:15 /home/diego/Документы/Адреса.txt`

Права доступа к файлу изменились с `-rwxrw----` на `-rw-rw-rw-`. Все пользователи могут читать и изменять наш файл, но ни у кого нет права на его выполнение.  

### Использование команды chmod в числовом режиме

Другой способ указать права доступа к файлу — применить команду `chmod` в числовом режиме. В этом режиме каждое разрешение файла представлено некоторым числом (в восьмеричной системе счисления):

   - `r` (_чтение/просмотр_) = **4**

   - `w` (_запись/изменение_) = **2**

   - `x` (_выполнение_) = **1**

   - `–` (не задано) = **0**

Допускается объединение данных числовых значений, и таким образом одно число может использоваться для представления всего набора разрешений. В следующей таблице приведены цифры для всех типов разрешений:

| Число     | Тип разрешения                | Символ |
| --------- | ----------------------------- | ------ |
| 0         | Нет разрешения (никаких прав) | −−−    |
| 1         | Выполнение                    | −−x    |
| 2         | Запись                        | −w−    |
| 3 (2+1)   | Запись + Выполнение           | −wx    |
| 4         | Чтение                        | r−−    |
| 5 (4+1)   | Чтение + Выполнение           | r−x    |
| 6 (4+2)   | Чтение + Запись               | rw−    |
| 7 (4+2+1) | Чтение + Запись + Выполнение  | rwx    |
Поскольку вы должны определить разрешения для каждой категории пользователей (_Владелец, Группа, Остальные_), команда будет включать в себя три числа (каждое из которых представляет собой сумму привилегий).

В качестве примера, давайте посмотрим на наш файл _Адреса.txt_, права которого, я напомню, мы сконфигурировали (в символьном режиме) с помощью команды:

>`chmod u=rwx,g=rw,o=r /home/diego/Документы/Адреса.txt`

Те же параметры разрешений, но уже в числовом формате, можно определить следующим образом:

>`chmod 764 /home/diego/Документы/Адреса.txt`

Теперь поменяем разрешения файла так, чтобы _Владелец_ мог читать и писать, _Группа_ — только читать, а у _Остальных_ — вообще не было прав на доступ. Судя по вышеприведенной таблице, для _Владельца_ числовое представление прав доступа соответствует числу `6` (`rw-`), для _Группы_ — числу `4` (`r--`), а для _Остальных_ — `0` (`---`). В совокупности должно получиться `640` (`rw-r-----`):

`diego@debian:~$ chmod 640 /home/diego/Документы/Адреса.txt`

Результат:

>`diego@debian:~$ chmod 640 /home/diego/Документы/Адреса.txt   diego@debian:~$ ls -la /home/diego/Документы/Адреса.txt   -rw-r----- 1 diego diego 2 фев 17 21:15 /home/diego/Документы/Адреса.txt`

Как видите, права изменились с `-rwxrwr--` на `-rw-r-----`, этого мы и хотели.  

## Смена владельца и группы

Помимо изменения прав доступа к файлам, вы можете столкнуться с ситуацией необходимости изменения владельца файла или даже всей группы. Выполнение любой из этих задач требует от вас наличие привилегий суперпользователя (_root_). Для этого я буду применять утилиту `sudo`.

Чтобы изменить владельца файла, необходимо применить команду `chown` (сокр. от _«**ch**ange **own**er»_), синтаксис которой довольно прост:

`chown [имя_пользователя] [имя_файла]`

Если вы хотите сменить не только владельца, но также и группу для файла или каталога, то синтаксис будет следующим:

`chown [имя_пользователь]:[группа] [имя_файла]`

Если вы просто хотите изменить группу, а владельца оставить прежним, то синтаксис примет вид:

`chown :[группа] [имя_файла]`

Или же используйте команду `chgrp` (сокр. от _«**ch**ange **gr**ou**p**«_), специально применяемую для изменения владельца группы файла или каталога:

`chgrp [группа] [имя_файла]`

В качестве тренировки давайте сменим владельца и группу файла _Адреса.__txt_ на пользователя _root_ и группу _root_ (при этом вам могут понадобиться права суперпользователя):

`diego@debian:~$ sudo chown root:root /home/diego/Документы/Адреса.txt   [sudo] пароль для diego:   diego@debian:~$ ls -la /home/diego/Документы/Адреса.txt   -rw-r----- 1 root root 2 фев 17 21:15 /home/diego/Документы/Адреса.txt   diego@debian:~$`

Как вы можете видеть, владелец и группа файла сменились с `diego:diego` на `root:root`.

Заметьте, что мне пришлось использовать `sudo` с `chown`. Это потому, что здесь задействован пользователь _root_, и чтобы иметь с ним дело, вам нужны права суперпользователя.  

## Есть ли приоритет в правах доступа к файлам?

  

Представим ситуацию, когда владелец не имеет никаких разрешений на доступ к файлу, группа имеет разрешение на чтение, в то время как другие пользователи имеют разрешения на чтение и запись.

`----r--rw- 1 diego coolgroup 2 фев 17 21:15 /home/diego/Документы/Адреса.txt`

Теперь, если пользователь _diego_ попытается прочитать файл с помощью команды `cat` или `less`, сможет ли он это сделать? Ответ — нет, потому что у него нет разрешения на чтение.

Но как же так? Ведь пользователь _diego_ является частью группы _coolgroup_, а группа имеет доступ на чтение. И даже все другие пользователи имеет разрешение на чтение и запись! Это должно означать, что каждый (включая пользователя _diego_) может читать и изменять файл, не так ли? Неправильно!

В Linux-системах приоритет считывания прав доступа отдается сначала _Владельцу_, затем _Группе_, а уже после _Остальным_. Система определяет, кто инициировал процесс (`cat` или `less` в нашем примере). Если пользователь, инициировавший процесс, также является _Владельцем_ файла, то считываются биты разрешений для _Владельца_.

Если процесс инициировал не _Владелец_ файла, то система проверяет _Группу_. Если пользователь, инициировавший процесс, находится в той же _Группе_, что и _Группа_-владелец файла, то считываются биты разрешений для _Группы_.

Если же инициировавший процесс пользователь не является _Владельцем_ файла и не входит в соответствующую _Группу_, то для него устанавливаются биты разрешений как для _Остальных_ пользователей.  

## Подсказки

   - Файл `_/etc/group_` содержит все группы, определенные в системе.

   - Вы можете использовать команду `groups`, чтобы найти все группы, членом которых вы являетесь:

![[Pasted image 20221018091621.png]]

- Вы можете использовать команду `newgrp` для работы в качестве члена группы отличной от вашей заданной по умолчанию группы:

![[Pasted image 20221018091647.png]]

 - Две группы не могут владеть одним и тем же файлом.

 - В Linux нет вложенных групп. Одна группа не может быть подгруппой другой.

 -  `x` — _выполнение_ каталога означает разрешение «войти» в каталог и получить возможный доступ к его подкаталогам.

## Подводя итоги

   - Linux-системы являются многопользовательскими системами, в которых применяются права доступа к файлам и каталогам.

   -  В Linux-системах различают три категории пользователей, а именно: _Владелец_, _Группа_ и _Остальные/Другие._

   -  Права доступа к файлам подразделяются на права _Чтения/Просмотра_, _Записи/Изменения_ и _Выполнения_, обозначаемые буквами `r`, `w` и `x`.

   -  Права доступа к файлу могут быть изменены командой `chmod`, которая поддерживает как числовой, так и символьный режимы задания прав доступа.

   - Команда `chown` может изменить владельца файла/каталога.

   - Команда `chgrp` может изменить группу, владеющую файлом.


Вот и все, теперь вы знаете не только что такое права доступа к файлам в Linux, но и как их посмотреть, и даже как их изменить. Это очень важная тема, в которой действительно стоит разобраться новичкам, чтобы использовать свою систему более полноценно. Если у вас остались вопросы, спрашивайте в комментариях!