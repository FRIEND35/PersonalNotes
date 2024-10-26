
## Установить sqlmap

SQLmap — это инструмент для тестирования на проникновение с открытым исходным кодом, который автоматизирует процесс обнаружения и эксплуатации уязвимостей SQL-инъекций и захвата серверов баз данных. Это один из самых популярных и мощных инструментов, когда дело касается эксплуатации уязвимости SQL-инъекций, которая сама по себе является наиболее распространенной уязвимостью безопасности веб-приложений. В этом руководстве мы узнаем, как установить и использовать sqlmap на Kali Linux.

Чтобы установить sqlmap в Kali Linux, откройте окно терминала и введите следующую команду:

```
sudo apt-get install sqlmap
```

После завершения установки вы можете проверить ее, введя следующую команду:

```
sqlmap --version
```

Это отобразит версию sqlmap, установленную в вашей системе. Вы также можете использовать опцию `--help`для просмотра доступных опций и команд.

Теперь, когда sqlmap установлен, вы можете начать использовать его для обнаружения и эксплуатации уязвимостей SQL-инъекций. Чтобы узнать больше о том, как использовать sqlmap, вы можете обратиться к официальной документации [здесь](https://github.com/sqlmapproject/sqlmap/wiki/Usage) .

## Определите цель

Первый шаг в использовании sqlmap для атак SQL-инъекций — идентификация цели. Это можно сделать с помощью различных инструментов, таких как [Nmap](https://www.nmap.org/) , [Metasploit](https://www.metasploit.com/) и [Wireshark](https://www.wireshark.org/) . После идентификации цели следующим шагом будет поиск уязвимых параметров. Для этого можно использовать опцию `-u`в sqlmap для указания целевого URL. Например, если целевой URL — `http://example.com/index.php?id=1`, то команда будет следующей:

sqlmap -u http://example.com/index.php?id=1
Копировать

Это просканирует целевой URL на наличие уязвимых параметров. Если таковые будут найдены, sqlmap отобразит их в выводе. После того, как уязвимые параметры будут идентифицированы, следующим шагом будет запуск sqlmap для эксплуатации уязвимости.

## Найдите уязвимые параметры

Чтобы найти уязвимые параметры, вам нужно определить целевой веб-сайт и его параметры. Для этого вы можете использовать `sqlmap`инструмент командной строки. Этот инструмент просканирует целевой веб-сайт на наличие уязвимых параметров, которые могут быть использованы. Чтобы использовать `sqlmap`, вам нужно указать целевой URL и параметры, которые вы хотите просканировать. Например, если вы хотите просканировать целевой веб-сайт на наличие уязвимых параметров, вы можете использовать следующую команду:

sqlmap -u http://example.com/ --data "param1=value1¶m2=value2"
Копировать

Эта команда просканирует целевой веб-сайт на наличие уязвимых параметров, которые могут быть использованы. После завершения сканирования вам будет представлен список уязвимых параметров, которые могут быть использованы. Затем вы можете использовать эти параметры для эксплуатации уязвимости и получения доступа к целевому веб-сайту.

Важно отметить, что вы всегда должны очищать после эксплуатации уязвимости. Это означает, что вы должны удалить любой вредоносный код, который вы внедрили в целевой веб-сайт. Это поможет гарантировать, что веб-сайт останется безопасным и на него не смогут быть совершены дальнейшие атаки.

## Запустить sqlmap

Теперь, когда вы определили цель и уязвимые параметры, пришло время запустить sqlmap. sqlmap — это инструмент для тестирования на проникновение с открытым исходным кодом, который автоматизирует процесс обнаружения и эксплуатации уязвимостей SQL-инъекций и захвата серверов баз данных. Чтобы запустить sqlmap, откройте окно терминала и введите следующую команду:

```
sqlmap -u http://example.com/vulnerable_page.php?id=1 --dbs
```

Эта команда запустит sqlmap для целевого URL и выведет список всех баз данных, доступных на сервере. Вы также можете использовать опцию `--tables`для вывода списка всех таблиц в определенной базе данных. Чтобы воспользоваться уязвимостью, вы можете использовать опцию `--sql-query`для выполнения произвольных SQL-запросов на сервере. Например, чтобы вывести список всех пользователей в базе данных, вы можете использовать следующую команду:

```
sqlmap -u http://example.com/vulnerable_page.php?id=1 --sql-query "SELECT * FROM users"
```

Вы также можете использовать `--os-shell`опцию для получения интерактивной оболочки на сервере. Это позволит вам выполнять системные команды на сервере и получать доступ к конфиденциальной информации. Чтобы получить интерактивную оболочку, используйте следующую команду:

```
sqlmap -u http://example.com/vulnerable_page.php?id=1 --os-shell
```

После того, как вы воспользовались уязвимостью, важно убрать за собой. Это включает удаление любых файлов или баз данных, которые вы создали, а также любого вредоносного кода, который вы внедрили на сервер. Также важно убедиться, что уязвимость была исправлена, чтобы ее нельзя было использовать снова.

## Воспользуйтесь уязвимостью

Теперь, когда вы определили уязвимые параметры, вы можете использовать их с помощью sqlmap. Для этого вам нужно запустить команду sqlmap с уязвимым параметром в качестве аргумента. Например, если уязвимый параметр — «id», вы должны запустить следующую команду:

```
sqlmap -u http://example.com/page.php?id=1
```

Это запустит sqlmap против URL и попытается использовать уязвимость. В случае успеха sqlmap отобразит результаты атаки. Затем вы можете использовать результаты для получения доступа к базе данных или для изменения данных в базе данных. Вы также можете использовать sqlmap для дампа всей базы данных, что может быть полезно для дальнейшего анализа.

Важно отметить, что sqlmap — мощный инструмент, и его следует использовать с осторожностью. При неправильном использовании он может нанести серьезный ущерб целевой системе. Поэтому важно понимать последствия использования sqlmap, прежде чем пытаться эксплуатировать уязвимость.

## Очистка

После того, как вы успешно воспользовались уязвимостью, важно очистить среду. Это включает удаление любых вредоносных файлов, которые были созданы во время атаки, а также восстановление любых изменений, которые были внесены в систему. Для этого вы можете использовать команду `rm`для удаления любых вредоносных файлов, которые были созданы. Вы также можете использовать команду `restorecon`для восстановления контекста безопасности любых файлов, которые были изменены. Наконец, вы можете использовать команду `iptables`для сброса любых правил брандмауэра, которые были изменены во время атаки.

Также важно обеспечить защиту системы от будущих атак. Это можно сделать, исправив все уязвимости, которые были использованы, а также внедрив дополнительные меры безопасности, такие как брандмауэры и системы обнаружения вторжений. Для получения дополнительной информации о защите вашей системы, пожалуйста, обратитесь к Kali [Linux Security Guide](https://www.kali.org/security/) .