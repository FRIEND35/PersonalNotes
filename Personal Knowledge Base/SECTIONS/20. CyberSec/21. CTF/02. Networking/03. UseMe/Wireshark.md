Wireshark — это анализатор пакетов с открытым исходным кодом, который используется для **обучения, анализа, разработки программного обеспечения, разработки протоколов связи и устранения неполадок в сети**.  Он используется для отслеживания пакетов, чтобы каждый из них фильтровался в соответствии с нашими конкретными потребностями. Его обычно называют **сниффером, анализатором сетевых протоколов и сетевым анализатором** . Он также используется инженерами сетевой безопасности для изучения проблем безопасности.

Wireshark — это бесплатное приложение, которое используется для перехвата данных туда и обратно. Его часто называют бесплатным компьютерным приложением для анализа пакетов. Он переводит сетевую карту в неселективный режим, т. е. принимает все пакеты, которые она получает.

Wireshark - это анализатор сетевого трафика, который используется для захвата и анализа сетевых пакетов. Перед тем, как переходить к рассмотрению способов анализа трафика, нужно рассмотреть, какие возможности поддерживает программа более подробно, с какими протоколами она может работать и что делать. Вот основные возможности программы:

- Захват пакетов в реальном времени из проводного или любого другого типа сетевых интерфейсов, а также чтение из файла;
- Поддерживаются такие интерфейсы захвата: Ethernet, IEEE 802.11, PPP и локальные виртуальные интерфейсы;
- Пакеты можно отсеивать по множеству параметров с помощью фильтров;
- Все известные протоколы подсвечиваются в списке разными цветами, например TCP, HTTP, FTP, DNS, ICMP и так далее;
- Поддержка захвата трафика VoIP-звонков;
- Поддерживается расшифровка HTTPS-трафика при наличии сертификата;
- Расшифровка WEP-, WPA-трафика беспроводных сетей при наличии ключа и handshake;
- Отображение статистики нагрузки на сеть;
- Просмотр содержимого пакетов для всех сетевых уровней;
- Отображение времени отправки и получения пакетов.

# Использование Wireshark:

Wireshark можно использовать следующими способами:

1. Он используется инженерами сетевой безопасности для изучения проблем безопасности.
2. Это позволяет пользователям наблюдать за всем трафиком, передаваемым по сети.
3. Он используется сетевыми инженерами для устранения неполадок в сети.
4. Это также помогает устранять проблемы с задержкой и вредоносные действия в вашей сети.
5. Он также может анализировать отброшенные пакеты.
6. Это помогает нам узнать, как все устройства, такие как ноутбуки, мобильные телефоны, настольные компьютеры, коммутаторы, маршрутизаторы и т. д., взаимодействуют в локальной сети или в остальном мире.

# Что такое пакет?

Пакет — это единица данных, которая передается по сети между источником и пунктом назначения. Сетевые пакеты небольшие: максимум **1,5 килобайта для пакетов Ethernet и 64 килобайта для пакетов IP** . Пакеты данных в Wireshark можно просматривать онлайн и анализировать в автономном режиме.

# Особенности Wireshark

- Это мультиплатформенное программное обеспечение, то есть оно может работать на Linux, Windows, OS X, FreeBSD, NetBSD и т. д.
- Это стандартный трехпанельный пакетный браузер.
- Он выполняет глубокую проверку сотен протоколов.
- Часто это включает в себя анализ в реальном времени, т. е. из различных типов сетей, таких как Ethernet, петлевая связь и т. д., мы можем считывать живые данные.
- Он имеет параметры сортировки и фильтрации, которые облегчают пользователю просмотр данных.
- Это также полезно при анализе VoIP.
- Он также может захватывать необработанный USB-трафик.
- Для фильтрации вывода можно использовать различные настройки, такие как таймеры и фильтры.
- Он может захватывать пакеты только в сетях, поддерживаемых PCAP (интерфейс прикладного программирования, используемый для захвата сети).
- Wireshark поддерживает множество хорошо документированных форматов файлов захвата, таких как PcapNg и Libpcap. Эти форматы используются для хранения захваченных данных.
- Это программное обеспечение №1 для своей цели. Он имеет бесчисленное множество приложений **, начиная от отслеживания несанкционированного трафика, настроек брандмауэра и т. д** .
# Что такое цветовое кодирование в Wireshark?

Пакеты в Wireshark выделяются **синим** , **черным** и **зеленым цветом** . Эти цвета помогают пользователям идентифицировать типы трафика. Это также называется **раскрашиванием пакетов** . Разновидностями правил раскраски в Wireshark являются **временные правила** и **постоянные правила** .

- Временные правила действуют до тех пор, пока программа не перейдет в активный режим или пока мы не выйдем из программы.
- Постоянные правила цвета доступны до тех пор, пока Wireshark не будет использоваться или пока вы не запустите Wireshark в следующий раз. Действия по применению цветовых фильтров будут обсуждаться позже в этом разделе.

# Анализ сетевого трафика

Для начала анализа выберите сетевой интерфейс, например eth0, и нажмите кнопку **Start.**

![[Pasted image 20240311231411.png]]

После этого откроется следующее окно, уже с потоком пакетов, которые проходят через интерфейс. Это окно тоже разделено на несколько частей:

- **Верхняя часть** - это меню и панели с различными кнопками;
- **Список пакетов** - дальше отображается поток сетевых пакетов, которые вы будете анализировать;
- **Содержимое пакета** - чуть ниже расположено содержимое выбранного пакета, оно разбито по категориям в зависимости от транспортного уровня;
- **Реальное представление** - в самом низу отображается содержимое пакета в реальном виде, а также в виде HEX.

Вы можете кликнуть по любому пакету, чтобы проанализировать его содержимое:

![[Pasted image 20240311231455.png]]

Здесь мы видим пакет запроса к DNS, чтобы получить IP-адрес сайта, в самом запросе отправляется домен, а в пакете ответа мы получаем наш вопрос, а также ответ.

Для более удобного просмотра можно открыть пакет в новом окне, выполнив двойной клик по записи:

![[Pasted image 20240311231514.png]]

# Фильтры Wireshark

Перебирать пакеты вручную, чтобы найти нужные, очень неудобно, особенно при активном потоке. Поэтому для такой задачи лучше использовать фильтры. Для ввода фильтров под меню есть специальная строка. Вы можете нажать **Expression**, чтобы открыть конструктор фильтров, но там их очень много, поэтому мы рассмотрим самые основные:

- **ip.dst** - целевой IP-адрес;
- **ip.src** - IP-адрес отправителя;
- **ip.addr** - IP отправителя или получателя;
- **ip.proto** - протокол;
- **tcp.dstport** - порт назначения;
- **tcp.srcport** - порт отправителя;
- **ip.ttl** - фильтр по ttl, определяет сетевое расстояние;
- **http.request_uri** - запрашиваемый адрес сайта.

Для указания отношения между полем и значением в фильтре можно использовать такие операторы:

- **`==`** - равно;
- **!=** - не равно;
- **<** - меньше;
- **>** - больше;
- **<=** - меньше или равно;
- **>=** - больше или равно;
- **matches** - регулярное выражение;
- **contains** - содержит.

Для объединения нескольких выражений можно применять:

- **&&** - оба выражения должны быть верными для пакета;
- **||** - может быть верным одно из выражений.

Теперь рассмотрим подробнее на примерах несколько фильтров и попытаемся понять все знаки отношений.

Сначала отфильтруем все пакеты, отправленные на 194.67.215.125 (losst.pro). Наберите строку в поле фильтра и нажмите **Apply**. Для удобства фильтры Wireshark можно сохранять с помощью кнопки **Save**:

```
ip.dst == 194.67.215.125
```

![[Pasted image 20240311231620.png]]

А чтобы получить не только отправленные пакеты, но и полученные в ответ от этого узла, можно объединить два условия:

```
ip.dst == 194.67.215.125 || ip.src == 194.67.215.125
```

![[Pasted image 20240311231645.png]]

Дальше отберём пакеты с ttl меньше 10:

```
ip.ttl < 10
```


![[Pasted image 20240311231712.png]]

Также мы можем отобрать переданные большие файлы:

```
http.content_length > 5000
```

Отфильтровав Content-Type, мы можем выбрать все картинки, которые были загружены; выполним анализ трафика Wireshark,  пакеты, которого содержат слово image:

```
http.content_type contains image
```

Чтобы очистить фильтр, вы можете нажать кнопку Clear. Бывает, вы не всегда знаете всю необходимую для фильтрации информацию, а просто хотите изучить сеть. Вы можете добавить любое поле пакета в качестве колонки и посмотреть его содержимое в общем окне для каждого пакета.

Например, я хочу вывести в виде колонки ttl (время жизни) пакета. Для этого откройте информацию о пакете, найдите это поле в разделе IP. Затем вызовите контекстное меню и выберите опцию Apply As Column:

![[Pasted image 20240311231816.png]]

Далее вы увидите нужную колонку после обновления:

![[Pasted image 20240311231833.png]]

Таким же образом можно создать фильтр на основе любого нужного поля. Выберите его и вызовите контекстное меню, затем нажмите Apply as filter или Prepare as filter, затем выбираем Selected, чтобы вывести только выбранные значения, или Not selected, чтобы их убрать:

![[Pasted image 20240311231846.png]]

Указанное поле и его значение будет применено или во втором случае подставлено в поле фильтра:

![[Pasted image 20240311231856.png]]

Таким способом вы можете добавить в фильтр поле любого пакета или колонку. Там тоже есть эта опция в контекстном меню. Для фильтрации протоколов вы можете использовать и более простые условия. Например, выполним анализ трафика Wireshark для протоколов HTTP и DNS:

```
http || dns
```

Еще одна интересная возможность программы - использование Wireshark для отслеживания определённого сеанса между компьютером пользователя и сервером. Для этого откройте контекстное меню для пакета и выберите Follow TCP stream.

![[Pasted image 20240311231924.png]]

Затем откроется окно, в котором вы найдете все данные, переданные между сервером и клиентом:

![[Pasted image 20240311231937.png]]

# Диагностика проблем Wireshark

Возможно, вам интересно, как пользоваться Wireshark 2.0 для обнаружения проблем в сети. Для этого в левом нижнем углу окна есть круглая кнопка, при нажатии на неё открывается окно **Expet Tools**. В нём Wireshark собирает все сообщения об ошибках и неполадках в сети:

![[Pasted image 20240311232119.png]]

Окно разделено на такие вкладки, как Errors, Warnings, Notices, Chats. Программа умеет фильтровать и находить множество проблем с сетью, и тут вы можете их очень быстро увидеть. Здесь тоже поддерживаются фильтры Wireshark.

![[Pasted image 20240311232147.png]]

# Анализ трафика Wireshark

Вы можете очень просто понять, что именно скачивали пользователи и какие файлы они смотрели, если соединение не было зашифровано. Программа очень хорошо справляется с извлечением контента.

Для этого сначала нужно остановить захват трафика с помощью красного квадрата на панели. Затем откройте меню **File** -> **Export Objects** -> **HTTP**:

![[Pasted image 20240311232507.png]]

Далее в открывшемся окне вы увидите все доступные перехваченные объекты. Вам достаточно экспортировать их в файловую систему. Вы можете сохранять как картинки, так и музыку.

![[Pasted image 20240311232518.png]]

Дальше вы можете выполнить анализ сетевого трафика Wireshark или сразу открыть полученный файл другой программой, например плеером.

# Выводы

В этой статье мы рассмотрели, как пользоваться Wireshark 2 для анализа сетевого трафика, а также примеры решения проблем с сетью. Это очень мощная утилита, которая имеет очень много функций. Всю её функциональность невозможно охватить в одной статье, но приведенной здесь базовой информации будет вполне достаточно, чтобы вы могли сами освоить всё необходимое.