
Сегодня поговорим о том, как добавить Linux-хост на сервер мониторинга Nagios с помощью NRPE-плагина. В предыдущих статьях мы объяснили, как установить и настроить последнюю версию **[Nagios Core](https://blog.sedicomm.com/2018/10/31/kak-ustanovit-nagios-na-rhel-centos-i-fedora/) 4.2.0** на сервере **CentOS** **7.2**. В этой статье мы покажем вам, как добавить удаленную **Linux**-машину и её функционал хосту **Nagios** **Monitoring** с помощью агента **NRPE**.

Мы надеемся, что у вас уже установлен и работает **Nagios**. Если нет, пожалуйста, используйте следующее руководство по установке, чтобы решить данную проблему:

- [Как установить Nagios 4.3.4 на RHEL, CentOS и Fedora?](https://blog.sedicomm.com/2018/10/31/kak-ustanovit-nagios-na-rhel-centos-i-fedora/)
- [Как добавить Windows Host на сервер мониторинга Nagios?](https://blog.sedicomm.com/2018/10/31/kak-dobavit-windows-host-na-server-monitoringa-nagios/)

После установки вы можете продолжить установку агента **NRPE** на хост **Linux**. Прежде чем продолжить, давайте коротко разберёмся что же такое **NRPE**.

# Что такое NRPE?

Плагин **NRPE** (Nagios Remote Plugin Executor) позволяет отслеживать любые удаленные службы **Linux**/**Unix** или сетевые устройства. Это дополнение **NRPE** позволяет **Nagios** отслеживать любые локальные ресурсы, такие как загрузка процессора, swap, использование памяти, пользователей онлайн и т.д. на удаленных машинах **Linux**.

**Примечание**. Для добавления **NRPE** необходимо, чтобы **плагины** **Nagios** были установлены на удаленном компьютере **Linux**. Без них демон **NRPE** не будет работать и ничего не будет отслеживать.

# Установка плагина NRPE

Чтобы использовать **NRPE**, вам нужно будет выполнить некоторые настройки как на узле **Nagios** **Monitoring**, так и на удаленном **Linux**-хосте, на котором установлен **NRPE**. Мы покажем каждую часть установки отдельно.

Мы предполагаем, что вы устанавливаете **NRPE** на хост, который поддерживает **TCP**-wrappers и демон **Xinted**, установленные на нём. Сегодня в большинстве современных дистрибутивов **Linux** эти два демона предустановленные по умолчанию. Если нет, мы будем устанавливать их позже во время установки, когда это потребуется.

## Установка на удаленном Linux-хост

Пожалуйста, используйте приведенные ниже инструкции для установки плагинов **Nagios** и демона **NRPE** на удаленном хосте **Linux**.
### Шаг 1: Установка необходимых зависимостей

Перед установкой нам необходимо установить необходимые библиотеки, такие как **gcc**, **glibc**, **glibc-common** и **GD**, а также библиотеки разработчика:

```
[root@tecmint]# yum install -y gcc glibc glibc-common gd gd-devel make net-snmp openssl-devel
-------------- On Fedora 22+ Onwards --------------
[root@tecmint]# dnf install -y gcc glibc glibc-common gd gd-devel make net-snmp openssl-devel
```
### Шаг 2. Создание пользователя Nagios

Создайте новую учетную запись пользователя **nagios** и установите пароль:

```
[root][root@tecmint]# useradd nagios  
[root@tecmint]# passwd nagios[/root]
```
### Шаг 3: Установка плагина Nagios

Создайте каталог для установки и его будущих загрузок:

```
[root@tecmint]# cd /root/nagios
```

Теперь загрузите последний пакет **Nagios Plugins 2.1.2** с помощью команды **wget**:

```
[root@tecmint nagios~]# wget https://www.nagios-plugins.org/download/nagios-plugins-2.1.2.tar.gz
```

### Шаг 4: Извлеките плагины Nagios

Выполните следующую команду **tar**, чтобы извлечь исходный код **tarball**:

```
[root@tecmint nagios~]# tar -xvf nagios-plugins-2.1.2.tar.gz
```

После этого в этой папке появится извлеченная новая папка:

```
[root@tecmint nagios ~]# ls -l

total 2640
drwxr-xr-x. 15 root root 4096 Aug 1 21:58 nagios-plugins-2.1.2
-rw-r--r--. 1 root root 2695301 Aug 1 21:58 nagios-plugins-2.1.2.tar.gz
```

### Шаг 5: Скомпилируйте и установите плагины Nagios

Затем скомпилируйте и установите плагины, используя следующие команды:

```
[root@tecmint nagios]# cd nagios-plugins-2.1.2
[root@tecmint nagios-plugins-2.1.2]# ./configure
[root@tecmint nagios-plugins-2.1.2]# make
[root@tecmint nagios-plugins-2.1.2]# make install
```

### Шаг 5: Скомпилируйте и установите плагины Nagios

Затем скомпилируйте и установите плагины, используя следующие команды:

```
[root@tecmint nagios]# cd nagios-plugins-2.1.2
[root@tecmint nagios-plugins-2.1.2]# ./configure
[root@tecmint nagios-plugins-2.1.2]# make
[root@tecmint nagios-plugins-2.1.2]# make install
```

Установите разрешения для каталога плагинов:

```
[root@tecmint nagios-plugins-2.1.2]# chown nagios.nagios /usr/local/nagios
[root@tecmint nagios-plugins-2.1.2]# chown -R nagios.nagios /usr/local/nagios/libexec
```

### Шаг 6: Установите Xinetd

В большинстве систем, демон **Xinetd** установлен по умолчанию. Если по каким-то причинам он у вас не установлен, установите пакет **xinetd**, используя следующую команду **yum**:

```
[root@tecmint nagios-plugins-2.1.2]# yum install xinetd
-------------- On Fedora 22+ Onwards --------------
[root@tecmint nagios-plugins-2.1.2]# dnf install xinetd
```

### Шаг 7: Установите плагин NRPE

Загрузите последние пакеты **NRPE Plugin 3.2** с помощью команды **wget**:

```
[root@tecmint nagios-plugins-2.1.2]# cd /root/nagios
[root@tecmint nagios]# wget https://github.com/NagiosEnterprises/nrpe/releases/download/nrpe-3.2.1/nrpe-3.2.1.tar.gz
```

Распакуйте архив с исходным кодом **NRPE**:

```
[root@tecmint nagios]# tar xzf nrpe-3.2.1.tar.gz
[root@tecmint nrpe-3.2]# cd nrpe-3.2
```

Скомпилируйте и установите аддон **NRPE**:

```
[root@tecmint nrpe-3.2]# ./configure
[root@tecmint nrpe-3.2]# make all
```

Затем установите демон **NRPE**-плагина и пример файла конфигурации демона:

```
[root@tecmint nrpe-3.2]# make install-plugin
[root@tecmint nrpe-3.2]# make install-daemon
[root@tecmint nrpe-3.2]# make install-daemon-config
```

Установите демон **NRPE** в качестве службы для **xinetd**:

```
[root@tecmint nrpe-3.2]# make install-xinetd
```

Или же:

```
[root@tecmint nrpe-3.2]# make install-inetd
```

Теперь откройте файл **/etc/xinetd.d/nrpe** и добавьте локальный хост и **IP**-адрес сервера мониторинга **Nagios**:

```
only_from = 127.0.0.1 localhost <nagios_ip_address>[/bahs]
```

Затем, откройте файл <strong>/etc/services</strong>, добавьте следующую запись для демона <strong>NRPE</strong> в нижней части файла:

```
[bash]nrpe 5666/tcp NRPE
```

Перезагрузите службу **xinetd**:

```
[root@tecmint]# service xinetd restart
```

### Шаг 8: Проверьте локальный демоном NRPE

Выполните следующую команду, чтобы убедиться, что демон **NRPE** правильно работает в **xinetd**:

```
[root@tecmint]# netstat -at | grep nrpe

tcp 0 0 *:nrpe *:* LISTEN
```

Если вы получаете результат, аналогичный приведенному выше, значит, он работает правильно. Если нет, обязательно проверьте следующее:

- Убедитесь, что вы правильно добавили запись **nrpe** в файл **/etc/services**.
- Проверьте, чтобы **only_from** содержал запись для «**nagios_ip_address**» в файле **/etc/xinetd.d/nrpe**.
- Проверьте, что **Xinetd** установлен и запущен.
- Проверьте наличие ошибок в файлах системного журнала примерно **xinetd** или **nrpe**, если проблемы найдены – необходимо их устранить.

Теперь проверьте, правильно ли работает демон **NRPE**. Запустите команду «**check_nrpe**»:

```
[root@tecmint]# /usr/local/nagios/libexec/check_nrpe -H localhost
```

Вы получите следующую строку на экране, она покажет вам, какая версия **NRPE** установлена:

```
NRPE v3.2
```

### Шаг 9: Настройка правил брандмауэра

Убедитесь, что брандмауэр на локальном компьютере позволит доступ к демону **NRPE** с удаленных серверов. Для этого запустите следующую команду **iptables**:
`
```
-------------- On RHEL/CentOS 6/5 and Fedora --------------
[root@tecmint]# iptables -A INPUT -p tcp -m tcp --dport 5666 -j ACCEPT
-------------- On RHEL/CentOS 7 and Fedora 19 Onwards --------------
[root@tecmint]# firewall-cmd --permanent --zone=public --add-port=5666/tcp
```

Выполните следующую команду, чтобы сохранить новое правило **iptables** (чтобы оно сохранилось при перезагрузке системы):

```
-------------- On RHEL/CentOS 6/5 and Fedora --------------
[root@tecmint]# service iptables save
```

### Шаг 10. Настройте команды NRPE.

Установленный по умолчанию файл конфигурации **NRPE** имеет несколько определений команд, которые будут использоваться для мониторинга машины на которой он установлен.

```
[root@tecmint]# vi /usr/local/nagios/etc/nrpe.cfg
```

Ниже приведены определения команд по умолчанию, которые расположены в нижней части файла конфигурации. Пока мы предполагаем, что вы используете эти команды. Вы можете проверить их, используя следующие команды:

```
# /usr/local/nagios/libexec/check_nrpe -H localhost -c check_users

USERS OK - 1 users currently logged in |users=1;5;10;0
```

```
# /usr/local/nagios/libexec/check_nrpe -H localhost -c check_load

OK - load average: 3.90, 4.37, 3.94|load1=3.900;15.000;30.000;0; load5=4.370;10.000;25.000;0; load15=3.940;5.000;20.000;0;
```

```
# /usr/local/nagios/libexec/check_nrpe -H localhost -c check_hda1

DISK OK - free space: /boot 154 MB (84% inode=99%);| /boot=29MB;154;173;0;193
```

```
# /usr/local/nagios/libexec/check_nrpe -H localhost -c check_total_procs

PROCS CRITICAL: 297 processes
```

```
# /usr/local/nagios/libexec/check_nrpe -H localhost -c check_zombie_procs

PROCS OK: 0 processes with STATE = Z
```


Вы можете редактировать и добавлять новые определения команд, редактируя файл конфигурации **NRPE**.

Наконец-то, вы успешно установили и настроили агент **NRPE** на удаленном **Linux**-хост. Теперь пришло время установить компоненты **NRPE** и добавить некоторые службы на ваш сервер мониторинга **Nagios**…

## Устновка NRPE на сервере мониторинга Nagios

Теперь войдите в свой сервер мониторинга **Nagios**. Здесь вам понадобятся выполнить следующие шаги:

- Установить плагин **check_nrpe**.
- Создать определение команды **Nagios** с помощью плагина **check_nrpe**.
- Создать узел **Nagios** и добавить определения служб для мониторинга удаленного хоста **Linux**.

### Шаг 1: Установка плагина NRPE

Перейдите в каталог загрузки **nagios** и загрузите последний плагин **NRPE** с помощью команды **wget**:

```
[root@tecmint]# cd /root/nagios
[root@tecmint]# wget https://github.com/NagiosEnterprises/nrpe/releases/download/nrpe-3.2.1/nrpe-3.2.1.tar.gz
```

Распакуйте архив с исходным кодом **NRPE**:

```
[root@tecmint]# tar xzf nrpe-3.2.1.tar.gz
[root@tecmint]# cd nrpe-3.2
```

Скомпилируйте и установите аддон **NRPE**:

```
[root@tecmint]# ./configure
[root@tecmint]# make all
[root@tecmint]# make install-daemon
```

### Шаг 2: Проверка удаленного демона NRPE

Убедитесь, что плагин **check_nrpe** может взаимодействовать с демоном **NRPE** на удаленном **Linux-хост**. Добавьте **IP**-адрес в приведенную ниже команду с **IP**-адресом удаленного хоста **Linux**:

```
[root@tecmint]# /usr/local/nagios/libexec/check_nrpe -H <remote_linux_ip_address>
```

В ответ вы получите строку, которая покажет вам, какая версия **NRPE** установлена ​​на удаленном хосте, например:

```
NRPE v3.0
```

Если вы получили ошибку тайм-аута плагина, проверьте следующее:

- Убедитесь, что ваш брандмауэр не блокирует связь между удаленным хостом и хостом мониторинга.
- Убедитесь, что демон **NRPE** правильно установлен в **xinetd**.
- Убедитесь, что правила брандмауэра удаленного **Linux-хоста** не блокируют доступ сервера мониторинга для связи с демоном **NRPE**.

## Добавление удаленного Linux-хост к серверу мониторинга Nagios

Чтобы добавить удаленный хост, вам нужно создать два новых файла «**hosts.cfg**» и «**services.cfg**» в разделе «**/usr/local/nagios/etc/**».

```
[root@tecmint]# cd /usr/local/nagios/etc/
[root@tecmint]# touch hosts.cfg
[root@tecmint]# touch services.cfg
```

Теперь добавьте эти два файла в главный файл конфигурации **Nagios**. Откройте файл **nagios.cfg** с помощью любого текстового редактора:

```
[root@tecmint]# vi /usr/local/nagios/etc/nagios.cfg
```

Теперь добавьте два только что созданных файла, как показано ниже:

```
# You can specify individual object config files as shown below:

cfg_file=/usr/local/nagios/etc/hosts.cfg
cfg_file=/usr/local/nagios/etc/services.cfg
```

Затем откройте файл **hostss.cfg** и добавьте имя шаблона хоста по умолчанию, укажите удаленные хосты, как показано ниже.

_Обязательно замените имя хоста, псевдоним и адрес, данными вашего удаленного хост-сервера._

```
[root@tecmint]# vi /usr/local/nagios/etc/hosts.cfg
```

```
## Default Linux Host Template ##
define host{
name linux-box ; Name of this template
use generic-host ; Inherit default values
check_period 24x7
check_interval 5
retry_interval 1
max_check_attempts 10
check_command check-host-alive
notification_period 24x7
notification_interval 30
notification_options d,r
contact_groups admins
register 0 ; DONT REGISTER THIS - ITS A TEMPLATE
}

## Default
define host{
use linux-box ; Inherit default values from a template
host_name tecmint ; The name we're giving to this server
alias CentOS 6 ; A longer name for the server
address 5.175.142.66 ; IP address of Remote Linux host
}
```

Следующий файл **services.cfg** добавляет следующие службы для мониторинга:

```
[root@tecmint]# vi /usr/local/nagios/etc/services.cfg
```

```
define service{
use generic-service
host_name tecmint
service_description CPU Load
check_command check_nrpe!check_load
}

define service{
use generic-service
host_name tecmint
service_description Total Processes
check_command check_nrpe!check_total_procs
}

define service{
use generic-service
host_name tecmint
service_description Current Users
check_command check_nrpe!check_users
}

define service{
use generic-service
host_name tecmint
service_description SSH Monitoring
check_command check_nrpe!check_ssh
}

define service{
use generic-service
host_name tecmint
service_description FTP Monitoring
check_command check_nrpe!check_ftp
}
```

Теперь необходимо создать определение команд **NRPE** в файле **commands.cfg**:

```
[bahs][root@tecmint]# vi /usr/local/nagios/etc/objects/commands.cfg[/bash]
```

Добавьте нижеприведённые определения команд **NRPE** в нижней части файла:

```
###############################################################################
# NRPE CHECK COMMAND
#
# Command to use NRPE to check remote host systems
###############################################################################

define command{
command_name check_nrpe
command_line $USER1$/check_nrpe -H $HOSTADDRESS$ -c $ARG1$
}
```

Наконец, проверьте файлы конфигурации Nagios на наличие ошибок:

```
[root@tecmint]# /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg

Total Warnings: 0
Total Errors: 0
```

Перезагрузите Nagios:

```
[root@tecmint]# /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg

Total Warnings: 0
Total Errors: 0
```

Теперь перейдите в веб-интерфейс Nagios Monitoring через «http://Your-server-IP-address/nagios» или «http://FQDN/nagios» и укажите имя пользователя «nagiosadmin» и пароль. Убедитесь, что удаленный Linux-хост действительно добавлен и его можно контролировать.

![[Pasted image 20231203182806.png]]

Теперь вы знаете, как добавить Linux-хост на сервер мониторинга Nagios с помощью NRPE-плагина.

Пока на этом всё! В одной из следующих статьей я покажу вам, [как добавить Windows Host на сервер мониторинга Nagios](https://blog.sedicomm.com/2018/10/31/kak-dobavit-windows-host-na-server-monitoringa-nagios/).

