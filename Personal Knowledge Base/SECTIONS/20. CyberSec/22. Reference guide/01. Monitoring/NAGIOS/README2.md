
# Введение

В этом руководстве мы рассмотрим установку Nagios 4, очень популярной системы мониторинга с открытым исходным кодом, на CentOS 7 или RHEL 7. Мы рассмотрим некоторые базовые настройки, чтобы вы могли отслеживать ресурсы хоста через веб-интерфейс. Мы также будем использовать Nagios Remote Plugin Executor (NRPE), который будет установлен в качестве агента на удаленных хостах, для мониторинга их локальных ресурсов.

Nagios полезен для ведения инвентаризации ваших серверов и обеспечения работоспособности критически важных служб. Использование системы мониторинга, такой как Nagios, является важным инструментом для любой среды производственного сервера.

# Предварительные условия

Чтобы следовать этому руководству, у вас должны быть права суперпользователя на сервере CentOS 7, на котором будет работать Nagios. В идеале вы будете использовать пользователя без полномочий root с привилегиями суперпользователя. Если вам нужна помощь в настройке, выполните шаги с 1 по 3 в этом руководстве: [Первоначальная настройка сервера с CentOS 7](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-centos-7) .

Также требуется стек LAMP. Если вам нужно это настроить, следуйте этому руководству: [Как установить стек LAMP в CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-centos-7) .

В этом руководстве предполагается, что на вашем сервере включена частная сеть. Если это не так, просто замените все ссылки на частные IP-адреса общедоступными IP-адресами.

Теперь, когда мы разобрались с предварительными условиями, давайте перейдем к установке Nagios 4.

# Установить Nagios 4

В этом разделе описано, как установить Nagios 4 на ваш сервер мониторинга. Вам нужно заполнить этот раздел только один раз.
## Установить зависимости сборки

Поскольку мы собираем Nagios Core из исходного кода, нам необходимо установить несколько библиотек разработки, которые позволят нам завершить сборку.

Сначала установите необходимые пакеты:

```
sudo yum install gcc glibc glibc-common gd gd-devel make net-snmp openssl-devel xinetd unzip
```

## Создать пользователя и группу Nagios

Мы должны создать пользователя и группу, которые будут запускать процесс Nagios. Создайте пользователя «nagios» и группу «nagcmd», затем добавьте пользователя в группу с помощью следующих команд:

```
sudo useradd nagios
sudo groupadd nagcmd
sudo usermod -a -G nagcmd nagios
```

Давайте теперь установим Nagios.

## Установите ядро ​​Nagios

Загрузите исходный код последней стабильной версии Nagios Core. Перейдите на [страницу загрузок Nagios](http://www.nagios.org/download/core-stay-informed) и нажмите ссылку **«Пропустить загрузку»** под формой. Скопируйте адрес ссылки на последнюю стабильную версию, чтобы загрузить ее на свой сервер Nagios.

На момент написания этой статьи последней стабильной версией была Nagios 4.1.1. Загрузите его в свой домашний каталог с помощью Curl:

```
cd ~
curl -L -O https://assets.nagios.com/downloads/nagioscore/releases/nagios-4.1.1.tar.gz
```

Распакуйте архив Nagios с помощью этой команды:

```
tar xvf nagios-*.tar.gz
```

Затем перейдите в извлеченный каталог:

```
cd nagios-*
```

Прежде чем собирать Nagios, мы должны настроить его с помощью этой команды:

```
./configure --with-command-group=nagcmd 
```

Теперь скомпилируйте Nagios с помощью этой команды:

```
make all
```

Теперь мы можем запустить эти команды make для установки Nagios, сценариев инициализации и примеров файлов конфигурации:

```
sudo make install
sudo make install-commandmode
sudo make install-init
sudo make install-config
sudo make install-webconf
```

Чтобы выдавать внешние команды через веб-интерфейс Nagios, мы должны добавить пользователя веб-сервера `apache`в `nagcmd`группу:

```
sudo usermod -G nagcmd apache
```

Копировать

## Установите плагины Nagios

Последний выпуск плагинов Nagios можно найти здесь: [Загрузка плагинов Nagios](http://nagios-plugins.org/download/?C=M;O=D) . Скопируйте адрес ссылки для последней версии и скопируйте адрес ссылки, чтобы вы могли загрузить ее на свой сервер Nagios.

На момент написания этой статьи последней версией являются плагины Nagios 2.1.1. Загрузите его в свой домашний каталог с помощью Curl:

```
cd ~
curl -L -O http://nagios-plugins.org/download/nagios-plugins-2.1.1.tar.gz
```

Извлеките архив плагинов Nagios с помощью этой команды:

```
tar xvf nagios-plugins-*.tar.gz
```

Затем перейдите в извлеченный каталог:

```
cd nagios-plugins-*
```

Прежде чем создавать плагины Nagios, мы должны его настроить. Используйте эту команду:

```
./configure --with-nagios-user=nagios --with-nagios-group=nagios --with-openssl
```

Теперь скомпилируйте плагины Nagios с помощью этой команды:

```
make
```

Затем установите его с помощью этой команды:

```
sudo make install
```

## Установить nrpe

Плагин **NRPE** (Nagios Remote Plugin Executor) позволяет отслеживать любые удаленные службы **Linux**/**Unix** или сетевые устройства. Это дополнение **NRPE** позволяет **Nagios** отслеживать любые локальные ресурсы, такие как загрузка процессора, swap, использование памяти, пользователей онлайн и т.д. на удаленных машинах **Linux**.

**Примечание**. Для добавления **NRPE** необходимо, чтобы **плагины** **Nagios** были установлены на удаленном компьютере **Linux**. Без них демон **NRPE** не будет работать и ничего не будет отслеживать.

Чтобы использовать **NRPE**, вам нужно будет выполнить некоторые настройки как на узле **Nagios** **Monitoring**, так и на удаленном **Linux**-хосте, на котором установлен **NRPE**. Мы покажем каждую часть установки отдельно.

Мы предполагаем, что вы устанавливаете **NRPE** на хост, который поддерживает **TCP**-wrappers и демон **Xinted**, установленные на нём. Сегодня в большинстве современных дистрибутивов **Linux** эти два демона предустановленные по умолчанию. Если нет, мы будем устанавливать их позже во время установки, когда это потребуется.

Найдите исходный код последней стабильной версии NRPE на [странице загрузок NRPE](http://sourceforge.net/projects/nagios/files/nrpe-2.x/) . Загрузите последнюю версию на свой сервер Nagios.

На момент написания этой статьи последняя версия — 2.15. Загрузите его в свой домашний каталог с помощью Curl:

```
cd ~
curl -L -O http://downloads.sourceforge.net/project/nagios/nrpe-2.x/nrpe-2.15/nrpe-2.15.tar.gz
```

Копировать

Распакуйте архив NRPE с помощью этой команды:

```
tar xvf nrpe-*.tar.gz
```

Копировать

Затем перейдите в извлеченный каталог:

```
cd nrpe-*
```

Копировать

Настройте NRPE с помощью этих команд:

```
./configure --enable-command-args --with-nagios-user=nagios --with-nagios-group=nagios --with-ssl=/usr/bin/openssl --with-ssl-lib=/usr/lib/x86_64-linux-gnu
```

Копировать

Теперь соберите и установите NRPE и его сценарий запуска xinetd с помощью следующих команд:

```
make all
sudo make install
sudo make install-xinetd
sudo make install-daemon-config
```

Копировать

Откройте скрипт запуска xinetd в редакторе:

```
sudo vi /etc/xinetd.d/nrpe
```

Копировать

Измените `only_from`строку, добавив в конец частный IP-адрес вашего сервера Nagios (замените фактический IP-адрес вашего сервера):

```
only_from = 127.0.0.1 10.132.224.168
```

Сохранить и выйти. Только серверу Nagios будет разрешено взаимодействовать с NRPE.

Перезапустите службу xinetd, чтобы запустить NRPE:

```
sudo service xinetd restart
```

Копировать

Теперь, когда Nagios 4 установлен, нам нужно его настроить.

## Настроить Nagios

Теперь давайте выполним первоначальную настройку Nagios. Вам нужно выполнить этот раздел только один раз на вашем сервере Nagios.
### Организация конфигурации Nagios

Откройте основной файл конфигурации Nagios в вашем любимом текстовом редакторе. Мы будем использовать vi для редактирования файла:

```
sudo vi /usr/local/nagios/etc/nagios.cfg
```

Теперь найдите раскомментируйте эту строку, удалив `#`:

```
#cfg_dir=/usr/local/nagios/etc/servers
```

Сохранить и выйти.

Теперь создайте каталог, в котором будет храниться файл конфигурации для каждого сервера, который вы будете отслеживать:

```
sudo mkdir /usr/local/nagios/etc/servers
```

### Настройка контактов Nagios

Откройте конфигурацию контактов Nagios в вашем любимом текстовом редакторе. Мы будем использовать vi для редактирования файла:

```
sudo vi /usr/local/nagios/etc/objects/contacts.cfg
```

Найдите директиву электронной почты и замените ее значение (выделенную часть) на свой адрес электронной почты:

```
email                           nagios@localhost        ; <<***** CHANGE THIS TO YOUR EMAIL ADDRESS ******
```

Сохранить и выйти.
### Настройте команду check_nrpe

Давайте добавим новую команду в нашу конфигурацию Nagios:

```
sudo vi /usr/local/nagios/etc/objects/commands.cfg
```

Копировать

Добавьте в конец файла следующее:

```
define command{
        command_name check_nrpe
        command_line $USER1$/check_nrpe -H $HOSTADDRESS$ -c $ARG1$
}
```

Сохранить и выйти. Это позволит вам использовать эту `check_nrpe`команду в определениях служб Nagios.

### Настроить Apache

Используйте htpasswd, чтобы создать пользователя-администратора с именем «nagiosadmin», который сможет получить доступ к веб-интерфейсу Nagios:

```
sudo htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin
```

Введите пароль в командной строке. Запомните этот логин, поскольку он понадобится вам для доступа к веб-интерфейсу Nagios.

**Примечание.** Если вы создаете пользователя без имени «nagiosadmin», вам потребуется отредактировать `/usr/local/nagios/etc/cgi.cfg`и изменить все ссылки «nagiosadmin» на созданного вами пользователя.

Nagios готов к запуску. Давайте сделаем это и перезапустим Apache:

```
sudo systemctl daemon-reload
sudo systemctl start nagios.service
sudo systemctl restart httpd.service
```

Чтобы включить запуск Nagios при загрузке сервера, выполните следующую команду:

```
sudo chkconfig nagios on
```

#### Необязательно: Ограничить доступ по IP-адресу.

Если вы хотите ограничить IP-адреса, которые могут получить доступ к веб-интерфейсу Nagios, вам нужно отредактировать файл конфигурации Apache:

```
sudo vi /etc/httpd/conf.d/nagios.conf
```

Найдите и прокомментируйте следующие две строки, добавив `#`перед ними символы:

```
Order allow,deny
Allow from all
```

Затем раскомментируйте следующие строки, удалив `#`символы, и добавьте IP-адреса или диапазоны (разделенные пробелами), которые вы хотите разрешить в строке `Allow from`:

```
#  Order deny,allow
#  Deny from all
#  Allow from 127.0.0.1
```

Поскольку эти строки появятся в файле конфигурации дважды, вам придется выполнить эти шаги еще раз.

Сохранить и выйти.

Теперь запустите Nagios и перезапустите Apache, чтобы изменения вступили в силу:

```
sudo systemctl restart nagios.service
sudo systemctl restart httpd.service
```

Nagios теперь запущен, давайте попробуем войти в систему.

## Доступ к веб-интерфейсу Nagios

Откройте свой любимый веб-браузер и перейдите на свой сервер Nagios (замените выделенную часть IP-адресом или именем хоста):

```
http://nagios_server_public_ip/nagios
```

Поскольку мы настроили Apache для использования htpasswd, вам необходимо ввести учетные данные для входа, которые вы создали ранее. В качестве имени пользователя мы использовали «nagiosadmin»:

![[Pasted image 20231203173845.png]]

После аутентификации вы увидите домашнюю страницу Nagios по умолчанию. Нажмите ссылку **«Хосты»** на левой панели навигации, чтобы увидеть, какие хосты отслеживает Nagios:

![[Pasted image 20231203173903.png]]

## Мониторинг хоста CentOS 7 с помощью NRPE

В этом разделе мы покажем вам, как добавить новый хост в Nagios, чтобы его можно было отслеживать. Повторите этот раздел для каждого сервера CentOS или RHEL, который вы хотите отслеживать.

**Примечание.** Если вы хотите отслеживать сервер Ubuntu или Debian, следуйте инструкциям по этой ссылке: [Мониторинг хоста Ubuntu с помощью NRPE](https://www.digitalocean.com/community/tutorials/how-to-install-nagios-4-and-monitor-your-servers-on-ubuntu-14-04#monitor-an-ubuntu-host-with-nrpe) .

На сервере, который вы хотите отслеживать, установите репозиторий EPEL:

```
sudo yum install epel-release
```

Теперь установите плагины Nagios и NRPE:

```
sudo yum install nrpe nagios-plugins-all
```

Теперь давайте обновим файл конфигурации NRPE. Откройте его в своем любимом редакторе (мы используем vi):

```
sudo vi /etc/nagios/nrpe.cfg
```

Найдите `allowed_hosts`директиву и добавьте частный IP-адрес вашего сервера Nagios в список, разделенный запятыми (замените его вместо выделенного примера):

```
allowed_hosts=127.0.0.1,10.132.224.168
```

Сохранить и выйти. Это настроит NRPE на прием запросов от вашего сервера Nagios через его частный IP-адрес.

Перезапустите NRPE, чтобы изменения вступили в силу:

```
sudo systemctl start nrpe.service
sudo systemctl enable nrpe.service
```

После завершения установки и настройки NRPE на хостах, которые вы хотите отслеживать, вам нужно будет добавить эти хосты в конфигурацию вашего сервера Nagios, прежде чем он начнет их отслеживать.

### Добавьте хост в конфигурацию Nagios

На сервере Nagios создайте новый файл конфигурации для каждого из удаленных хостов, которые вы хотите отслеживать в формате `/usr/local/nagios/etc/servers/`. Замените выделенное слово «yourhost» на имя вашего хоста:

```
sudo vi /usr/local/nagios/etc/servers/yourhost.cfg
```

Добавьте следующее определение хоста, заменив `host_name`значение именем удаленного хоста («web-1» в примере), значение `alias`описанием хоста и значение `address`частным IP-адресом удаленного хоста:

```
define host {
        use                             linux-server
        host_name                       yourhost
        alias                           My first Apache server
        address                         10.132.234.52
        max_check_attempts              5
        check_period                    24x7
        notification_interval           30
        notification_period             24x7
}
```

Используя приведенный выше файл конфигурации, Nagios будет отслеживать только то, включен ли хост или нет. Если вам этого достаточно, сохраните и выйдите, а затем перезапустите Nagios. Если вы хотите отслеживать определенные службы, добавьте любой из этих сервисных блоков для служб, которые вы хотите отслеживать. Обратите внимание, что значение check_command определяет, что будет отслеживаться, включая пороговые значения состояния. Вот несколько примеров, которые вы можете добавить в файл конфигурации вашего хоста:

Пинг:

```
define service {
        use                             generic-service
        host_name                       yourhost
        service_description             PING
        check_command                   check_ping!100.0,20%!500.0,60%
}
```

SSH (notifications_enabled, установленный в 0, отключает уведомления для службы):

```
define service {
        use                             generic-service
        host_name                       yourhost
        service_description             SSH
        check_command                   check_ssh
        notifications_enabled           0
}
```

Если вы не уверены, что это `use generic-service`значит, то это просто наследование значений шаблона службы под названием «generic-service», определенного по умолчанию.

Теперь сохранитесь и выйдите. Перезагрузите конфигурацию Nagios, чтобы изменения вступили в силу:

```
sudo systemctl reload nagios.service
```

Как только вы закончите настройку Nagios для мониторинга всех ваших удаленных хостов, все должно быть настроено. Обязательно зайдите в веб-интерфейс Nagios и посетите страницу **«Службы»** , чтобы просмотреть все отслеживаемые вами хосты и службы:

![[Pasted image 20231203173922.png]]

# Заключение

Теперь, когда вы отслеживаете свои хосты и некоторые их службы, возможно, вам захочется потратить некоторое время на то, чтобы выяснить, какие службы для вас важны, и начать их мониторинг. Вы также можете настроить уведомления, чтобы, например, вы получали электронное письмо, когда загрузка вашего диска достигает критического порога или когда ваш основной веб-сайт не работает, чтобы вы могли решить ситуацию быстро или до того, как проблема возникнет.

Удачи!