
https://www.itzgeek.com/how-tos/linux/centos-how-tos/monitor-centos-7-rhel-7-using-nagios-4-0-7.html
https://www.howtoforge.com/how-to-install-and-configure-nagios-on-centos-8/ 

Nagios (Nagios Core) — это бесплатная программа с открытым исходным кодом, которую можно использовать для мониторинга серверов на базе Linux\Windows. В этом руководстве мы установим и настроим Nagios на CentOS 7 VPS.

# Установка
## Установка APACHE

Чтобы Nagios работал на сервере, нам потребуется APACHE или любой другой веб-сервер. Если на вашем сервере уже установлен рабочий веб-сервер, вы можете пропустить это и перейти к следующему шагу.

Чтобы установить Apache на сервер CentOS, выполните следующую команду:

```
yum install httpd
```

Также необходимо запускать Apache при загрузке системы, для этого выполните следующие команды:

```
systemctl enable httpd.service
```

## Установка зависимостей

Следующие пакеты также требуются для работы Nagios. Выполните команду чтобы установить их:

```
yum install gcc glibc glibc-common wget gd gd-devel perl postfix
```

## Загрузка и установка Nagios

Для начала перейдём в каталог tmp и загрузим архив:

```
cd /tmp
wget -O nagioscore.tar.gz https://github.com/NagiosEnterprises/nagioscore/archive/nagios-4.4.2.tar.gz
```

Более свежие релизы можно найти по ссылке: [https://github.com/NagiosEnterprises/nagioscore/releases](https://github.com/NagiosEnterprises/nagioscore/releases)

После загрузки извлекаем архив и переходим в папку и настраиваем код для компиляции:

```
tar xzf nagioscore.tar.gz
cd /tmp/nagioscore-nagios-4.4.2
./configure
```

После завершения настройки компилируем Nagios, выполнив следующую команду:

```
make all
```

Нам так же потребуется создать пользователя nagios и группу, а после добавить пользователя apache в группу nagios:

```
make install-groups-users
usermod -a -G nagios apache
```

Теперь можно установить Nagios командой:

```
make install
```

Далее, выполним команды установки для управления службой Nagios, для создания конфигурационных файлов Nagios и Apache:

```
make install-daemoninit
make install-config
make install-commandmode
make install-webconf
```

После выполнения нужно перезапустить Apache:

```
systemctl restart httpd
```


## Создание учётной записи nagiosadmin

Чтобы иметь возможность войти в Nagios — необходимо создать учетную запись пользователя Apache.  
Для этого выполняем команду, чтобы создать пользователя с именем nagiosadmin и назначить ему пароль:

```
htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin
```

На данном этапе основная установка Nagios завершена. Но для правильной работы Nagios нужно установить плагины Nagios, как описано в следующем шаге.

## Установка плагинов

### Установка плагина NRPE

Чтобы использовать **NRPE**, вам нужно будет выполнить некоторые настройки как на узле **Nagios** **Monitoring**, так и на удаленном **Linux**-хосте, на котором установлен **NRPE**. Мы покажем каждую часть установки отдельно.

Мы предполагаем, что вы устанавливаете **NRPE** на хост, который поддерживает **TCP**-wrappers и демон **Xinted**, установленные на нём. Сегодня в большинстве современных дистрибутивов **Linux** эти два демона предустановленные по умолчанию. Если нет, мы будем устанавливать их позже во время установки, когда это потребуется.
##### Установка на удаленном Linux-хост

Пожалуйста, используйте приведенные ниже инструкции для установки плагинов **Nagios** и демона **NRPE** на удаленном хосте **Linux**.

Для начала установим пакеты для корректной работы плагинов. Перед установкой нам необходимо установить необходимые библиотеки, такие как gcc, glibc, glibc-common и GD, а также библиотеки разработчика:

```
yum install gcc glibc glibc-common make gettext automake autoconf wget openssl-devel net-snmp net-snmp-utils epel-release perl-Net-SNMP
```

Или же:

```
yum install -y gcc glibc glibc-common gd gd-devel make net-snmp openssl-devel
```

Чтобы загрузить и извлечь последнюю версию подключаемых модулей Nagios в tmp каталог на вашем сервере, выполните следующие команды:

```
cd / tmp 
wget --no-check-certificate -O nagios-plugins.tar.gz https://github.com/nagios-plugins/nagios-plugins/archive/release-2.2.1.tar.gz 
tar zxf nagios -plugins.tar.gz
```

После извлечения архива нужно выполнить следующие команды для компиляции и установки модулей:

```
cd /tmp/nagios-plugins-release-2.2.1/ 
./tools/setup 
./configure 
make 
make install
```


## Доступ к Nagios

После всех установок просто запускаем службу Nagios:

```
systemctl start nagios
```

Чтобы получить доступ к Nagios, откройте свой браузер, перейдите [http://IP_SERVER/nagios](http://ip_server/nagios) и войдите в систему, введите имя пользователя nagiosadmin и пароль к нему, который устанавливали раньше.

![[Pasted image 20231203172641.png]]

## Добавить другие хосты

Мы так же можем добавить другие наши сервера для мониторинга в Nagios.  
Для этого переходим в папку конфигураций Nagios:

```
cd /usr/local/nagios/etc/
```

Редактируем конфиг nagios.cfg, добавив строку:

```
cfg_dir=/usr/local/nagios/etc/servers
```

> **/usr/local/nagios/etc/servers** — это путь, где будут храниться конфигурационные файлы наших других серверов.

Создаём папку:

```
mkdir /usr/local/nagios/etc/servers
```

И добавляем конфигурационный файл:

```
nano /usr/local/nagios/etc/servers/host2.cfg
```

В созданный конфиг прописываем следующее:

```
define host{
        use                     linux-server
        host_name               host2
        alias                   host2
        address                 123.123.123.123
        }
define service{
        use                             local-service
        host_name                       host2
        service_description             PING
        check_command                   check_ping!100.0,20%!500.0,60%
        }

define service{
        use                             local-service
        host_name                       host2
        service_description             Root Partition
        check_command                   check_local_disk!20%!10%!/
        }

define service{
        use                             local-service
        host_name                       host2
        service_description             Current Users
        check_command                   check_local_users!20!50
        }
```

Где, **host2** — название хоста.  
**123.123.123.123** — IP сервера.

После всех изменений нужно перезагрузить Nagios командой:

```
service nagios restart
```

Теперь, в веб-интерфейсе появится добавленный хост.

![[Pasted image 20231203172811.png]]

## Программы уведомлений статуса.

Чтобы всё время на заглядывать в веб-интерфейс Nagios — можно воспользоваться программой: Nagstamon — это монитор состояния для рабочего стола. [https://nagstamon.ifw-dresden.de/](https://nagstamon.ifw-dresden.de/)  
Добавьте ваш сервер в настройках программы и при каждой появившейся проблеме Nagstamon будет уведомлять Вас на рабочем столе.

