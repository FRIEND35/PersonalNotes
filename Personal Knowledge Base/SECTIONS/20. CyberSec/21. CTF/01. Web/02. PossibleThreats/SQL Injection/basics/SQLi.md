## Что такое SQL-инъекция

SQL-инъекция, также известная как SQLI, является распространенным вектором атаки, который использует вредоносный код SQL для манипуляции базой данных бэкэнда с целью доступа к информации, которая не предназначалась для отображения. Эта информация может включать любое количество элементов, включая конфиденциальные данные компании, списки пользователей или личные данные клиентов.

Влияние SQL-инъекции на бизнес может иметь далеко идущие последствия. Успешная атака может привести к несанкционированному просмотру списков пользователей, удалению целых таблиц и, в некоторых случаях, к получению [злоумышленником](https://www.imperva.com/learn/application-security/ethical-hacking/) административных прав на базу данных, что наносит большой ущерб бизнесу.

При расчете потенциальной стоимости SQLi важно учитывать потерю доверия клиентов в случае кражи личной информации, такой как номера телефонов, адреса и данные кредитных карт.

Хотя этот вектор можно использовать для атаки на любую базу данных SQL, наиболее частыми целями являются веб-сайты.

## Что такое SQL-запросы

SQL — это стандартизированный язык, используемый для доступа к базам данных и управления ими с целью создания настраиваемых представлений данных для каждого пользователя. Запросы SQL используются для выполнения команд, таких как извлечение данных, обновление и удаление записей. Различные элементы SQL реализуют эти задачи, например, запросы, использующие оператор SELECT для извлечения данных на основе предоставленных пользователем параметров.

Типичный запрос к базе данных SQL электронного магазина может выглядеть следующим образом:

```sql
SELECT ItemName, ItemDescription FROM Item WHERE ItemNumber = ItemNumber
```

На основе этого веб-приложение формирует строковый запрос, который отправляется в базу данных как единый оператор SQL:

```sql
sql_query = " SELECT ItemName, ItemDescription FROM Item WHERE ItemNumber = " & Request.QueryString("ItemID")
```

Введенные пользователем данные  http://www.estore.com/items/items.asp?itemid=999 затем могут сгенерировать следующий SQL-запрос:

```sql
SELECT ItemName, ItemDescription FROM Item WHERE ItemNumber = 999
```

Как можно понять из синтаксиса, этот запрос возвращает имя и описание для элемента под номером 999.

## Типы SQL-инъекций

SQL-инъекции обычно делятся на три категории: In-band SQLi (классические), Inferential SQLi (слепые) и Out-of-band SQLi. Вы можете классифицировать типы SQL-инъекций на основе методов, которые они используют для доступа к данным бэкэнда, и их потенциального ущерба.

### **In-band SQLi**

Атакующий использует тот же канал связи для запуска своих атак и сбора результатов. Простота и эффективность In-band SQLi делают его одним из самых распространенных типов атак SQLi. Существует два подварианта этого метода:

- **Error-based SQLi** — злоумышленник выполняет действия, которые заставляют базу данных выдавать сообщения об ошибках. Злоумышленник может потенциально использовать данные, предоставленные этими сообщениями об ошибках, для сбора информации о структуре базы данных.
- **SQLi на основе объединения** — эта техника использует преимущество оператора UNION SQL, который объединяет несколько операторов select, сгенерированных базой данных, для получения одного ответа HTTP. Этот ответ может содержать данные, которые могут быть использованы злоумышленником.

### **Blind/Inferential (слепой) SQLi**

Атакующий отправляет полезные данные на сервер и наблюдает за ответом и поведением сервера, чтобы узнать больше о его структуре. Этот метод называется слепым SQLi, поскольку данные не передаются из базы данных веб-сайта атакующему, поэтому атакующий не может видеть информацию об атаке в полосе пропускания.

Слепые SQL-инъекции полагаются на ответ и поведенческие шаблоны сервера, поэтому они обычно выполняются медленнее, но могут быть столь же вредоносными. Слепые SQL-инъекции можно классифицировать следующим образом:

- **Boolean** — злоумышленник отправляет SQL-запрос в базу данных, побуждая приложение вернуть результат. Результат будет зависеть от того, является ли запрос истинным или ложным. В зависимости от результата информация в HTTP-ответе изменится или останется неизменной. Затем злоумышленник может определить, сгенерировало ли сообщение истинный или ложный результат.
- **На основе времени** — злоумышленник отправляет SQL-запрос в базу данных, что заставляет базу данных ждать (в течение определенного периода времени в секундах), прежде чем она сможет отреагировать. Злоумышленник может увидеть по времени, которое требуется базе данных для ответа, является ли запрос истинным или ложным. На основе результата HTTP-ответ будет сгенерирован мгновенно или после периода ожидания. Таким образом, злоумышленник может выяснить, вернуло ли использованное им сообщение истину или ложь, не полагаясь на данные из базы данных.

- Ключевое различие заключается в том, что при слепой SQL-инъекции злоумышленник **угадывает** результаты запроса, в то время как при инференциальной SQL-инъекции злоумышленник **выводит** результаты запроса.
- Blind SQL injection и инферентичная SQL injection отличаются способом, как атакующий может узнать, удалить или изменить информацию в базе данных.

Blind SQL injection:
- Атакующий не получает прямых ответов от базы данных, поэтому ему нужно гадать и проверять каждую часть запроса по порядку.
- Это подобно игре в угадайку, где атакующий должен догадываться о правильности своих запросов.

 Inferential SQL injection:
- Атакующий получает прямые ответы от базы данных, что делает ее более простой и эффективной.
- Это подобно разгадыванию головоломки, где атакующий может получать информацию о базе данных и извлекать данные напрямую.

В обоих случаях, используя SQL injection, злоумышленники могут получить доступ к конфиденциальным данным и повредить работу системы. Для предотвращения таких атак необходимо обеспечить безопасность веб-приложений и базы данных.

### **Out-of-band SQLi**

Атакующий может выполнить эту форму атаки только тогда, когда на сервере базы данных, используемом веб-приложением, включены определенные функции. Эта форма атаки в основном используется как альтернатива внутриполосным и выведенным методам SQLi.

Внеполосный SQLi выполняется, когда злоумышленник не может использовать тот же канал для запуска атаки и сбора информации или когда сервер слишком медленный или нестабильный для выполнения этих действий. Эти методы основаны на способности сервера создавать DNS- или HTTP-запросы для передачи данных злоумышленнику.

## Пример SQL-инъекции

[Злоумышленник, желающий выполнить SQL-инъекцию, манипулирует стандартным SQL-запросом, чтобы использовать уязвимости](https://www.imperva.com/learn/application-security/vulnerability-management/) непроверенного ввода в базе данных. Существует много способов, с помощью которых этот вектор атаки может быть выполнен, некоторые из которых будут показаны здесь, чтобы предоставить вам общее представление о том, как работает SQLI.

Например, вышеупомянутый ввод, который извлекает информацию о конкретном продукте, можно изменить следующим образом:  http://www.estore.com/items/items.asp?itemid=999 или 1=1 .

В результате соответствующий SQL-запрос выглядит следующим образом:

```sql
SELECT ItemName, ItemDescription ИЗ Items, WHERE ItemNumber = 999 ИЛИ 1=1
```

А поскольку утверждение 1 = 1 всегда истинно, запрос возвращает все наименования и описания продуктов в базе данных, даже те, к которым у вас может не быть доступа.

Злоумышленники также могут воспользоваться неправильно отфильтрованными символами для изменения команд SQL, в том числе используя точку с запятой для разделения двух полей.

Например, этот ввод  http://www.estore.com/items/iteams.asp?itemid=999; DROP TABLE Пользователи  сгенерируют следующий SQL-запрос:

```sql
SELECT ItemName, ItemDescription FROM Items 
WHERE ItemNumber = 999; DROP TABLE USERS
```

В результате вся база данных пользователей может быть удалена.

Другой способ манипулирования SQL-запросами — оператор UNION SELECT. Он объединяет два несвязанных запроса SELECT для извлечения данных из разных таблиц базы данных.

Например, ввод  http://www.estore.com/items/items.asp?itemid=999 UNION SELECT имя-пользователя, пароль FROM USERS  создает следующий SQL-запрос:

```sql
SELECT ItemName, ItemDescription FROM Items WHERE ItemID = '999' UNION SELECT Username, Passwords FROM Users;
```

Используя оператор UNION SELECT, этот запрос объединяет запрос имени и описания элемента 999 с другим запросом, который извлекает имена и пароли для каждого пользователя в базе данных.

## SQL-инъекция в сочетании с выполнением команд ОС: атака Accellion

Accellion, производитель File Transfer Appliance (FTA), сетевого устройства, широко используемого в организациях по всему миру и используемого для перемещения больших конфиденциальных файлов. Продукту более 20 лет, и сейчас он подходит к концу.

FTA стала объектом уникальной, очень сложной атаки, сочетающей SQL-инъекцию с выполнением команд операционной системы. Эксперты предполагают, что атака Accellion была осуществлена ​​хакерами, связанными с финансовой [преступной группировкой](https://www.imperva.com/blog/dont-be-a-victim-of-cyber-extortion/) FIN11 и группой вымогателей Clop.

Атака демонстрирует, что SQL-инъекция — это не просто атака, которая затрагивает веб-приложения или веб-сервисы, но также может использоваться для компрометации внутренних систем и [кражи данных](https://www.imperva.com/blog/the-latest-multistage-attacks-demonstrate-the-need-to-secure-the-data-layer/) .

### Кто пострадал от атаки?

Эксплойт Accellion представляет собой [атаку на цепочку поставок](https://www.imperva.com/learn/application-security/supply-chain-attack/) , затрагивающую многочисленные организации, которые развернули устройство FTA. Среди них Резервный банк Новой Зеландии, штат Вашингтон, Австралийская комиссия по ценным бумагам и инвестициям, телекоммуникационный гигант Singtel и производитель программного обеспечения безопасности Qualys, а также многие другие.

### Поток атаки Accelion

Согласно отчету, подготовленному по заказу Accellion, комбинированная атака SQLi и выполнения команд работала следующим образом:

1. Злоумышленники выполнили SQL-инъекцию, чтобы получить доступ к document_root.html, и извлекли ключи шифрования из базы данных Accellion FTA.
2. Злоумышленники использовали ключи для генерации действительных токенов и использовали эти токены для получения доступа к дополнительным файлам.
3. Злоумышленники использовали уязвимость выполнения команд операционной системы в файле sftp_account_edit.php, что позволило им выполнять собственные команды.
4. Злоумышленники создали веб-шелл по адресу сервера /home/seos/courier/oauth.api
5. Используя эту веб-оболочку, они загрузили на диск пользовательский полнофункциональный веб-оболочку, который включал в себя высоконастраиваемый инструментарий для эксфильтрации данных из системы Accellion. Исследователи назвали эту оболочку DEWMODE.
6. Используя DEWMODE, злоумышленники извлекли список доступных файлов из базы данных MySQL в системе Accellion FTA и перечислили файлы и их метаданные на HTML-странице.
7. Злоумышленники выполняли запросы на загрузку файлов, которые содержали запросы к компоненту DEWMODE, с зашифрованными и кодированными параметрами URL.
8. DEWMODE может принимать эти запросы, а затем удалять запросы на загрузку из веб-журналов FTA.

Это повышает значимость атак с использованием SQL-инъекций, показывая, как их можно использовать в качестве шлюза для гораздо более разрушительной атаки на критически важную корпоративную инфраструктуру.

## Предотвращение и смягчение последствий SQLI

Существует несколько эффективных способов предотвращения атак SQLI, а также защиты от них в случае их возникновения.

Первым шагом является проверка входных данных (также известная как санация), то есть написание кода, способного идентифицировать нелегитимный пользовательский ввод.

Хотя проверка ввода всегда должна считаться лучшей практикой, она редко является надежным решением. Реальность такова, что в большинстве случаев просто невозможно отобразить все законные и незаконные вводы — по крайней мере, не вызывая большого количества ложных срабатываний, которые мешают пользовательскому опыту и функциональности приложения.

По этой причине брандмауэр веб-приложений (WAF) обычно используется для фильтрации SQLI, а также других сетевых угроз. Для этого WAF обычно полагается на большой и постоянно обновляемый список тщательно созданных сигнатур, которые позволяют ему хирургически отсеивать вредоносные SQL-запросы. Обычно такой список содержит сигнатуры для устранения определенных векторов атак и регулярно обновляется для введения правил блокировки для недавно обнаруженных уязвимостей.

Современные [межсетевые экраны веб-приложений](https://www.imperva.com/learn/application-security/what-is-web-application-firewall-waf/) также часто интегрируются с другими решениями безопасности. От них [WAF](https://www.imperva.com/products/web-application-firewall-waf/) может получать дополнительную информацию, которая еще больше расширяет его возможности безопасности.

Например, брандмауэр веб-приложений, который сталкивается с подозрительным, но не откровенно вредоносным вводом, может перекрестно проверить его с данными IP, прежде чем принять решение о блокировке запроса. Он блокирует ввод только в том случае, если сам IP имеет плохую репутацию.

[WAF на основе облака](https://www.imperva.com/products/cloud-waf/) Imperva  использует распознавание сигнатур, репутацию IP и другие методы безопасности для выявления и блокировки SQL-инъекций с минимальным количеством ложных срабатываний. Возможности WAF дополняются [IncapRules](https://www.imperva.com/blog/incaprules-optimized-application-security) — пользовательским механизмом правил безопасности, который позволяет детально настраивать параметры безопасности по умолчанию и создавать дополнительные политики безопасности для конкретных случаев.

Наш WAF также использует методы краудсорсинга, которые гарантируют, что новые угрозы, нацеленные на любого пользователя, немедленно распространяются по всей пользовательской базе. Это позволяет быстро реагировать на недавно обнаруженные уязвимости и [угрозы нулевого дня](https://www.imperva.com/learn/application-security/zero-day-exploit/) .