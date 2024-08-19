Источники:

- https://kmb.cybber.ru/forensic/main.html
- https://wiki.cyber-mo.ru/forensic/forensic-eto

### Введение

"Форензика"-от латинского «foren»,«речь перед форумом»,выступление перед судом, судебные дебаты. В русский язык пришло из английского. Сам термин «forensics» это сокращенная форма от «forensic science», дословно «судебная наука», то есть наука об исследовании доказательств – криминалистика. Криминалистика которая изучает компьютерные доказательства, по английски будет «computer forensics». В России слово форензика имеет одно значение - компьютерная криминалистика.

**Forensic (Computer forensic)** - прикладная наука о раскрытии инцидентов, связанных с компьютерной информацией, исследовании цифровых доказательств, методах поиска, получения и закрепления таких доказательств. Форензика является подразделом криминалистики, является неотъемлемой частью в сфере ИБ.

Виды инцидентов:

- утечка конфиденциальной информации
- неправомерный доступ к информации
- удаление информации
- компрометация информации
- саботаж
- мошенничество с помощью ИТ систем
- использование активов компании в личных целях
- внешние атаки: DoS, DDoS, фишинг, перехват и подмена трафика
- размещение конфиденциальной/провокационной информации в сети Интернет
- взлом
- вирусные атаки

---
### Forensic в CTF

В CTF _forensic_ является одной из сложных категорий заданий, сравнимой с PWN. Эта категория охватывает довольно обширные категории знаний:

- Программирование
- ОС (Windows, Unix, ~~BolgenOS~~)
- ФС (FAT, NTFS, Ext, etc.)
- Специфика типов файлов (JPEG, ELF, WAV, etc.)
- Сети (как минимум стек протоколов TCP/IP)
- Криптография
- Стеганография
- RE
- OSINT (Open Source INTelligence)

Виды задач, встречающиеся в тасках CTF:

- Восстановление данных (в том числе и удаленных)
- Анализ логов (журналы аудита, лог-файлы программ)
- Анализ сетевого трафика
- Поиск информации из открытых источников

Задачи могут перемежаться между собой, а также быть усложнены другими категориями знаний (криптография, RE, вирусология).

Каких-либо универсальных методов решения тасков категории _forensic_ нет. Никогда не знаешь, что тебе за инцидент попадется и как тебе с ним ~~париться~~ справляться. Можно лишь выработать стратегию решения, например:

- Что за ~~фигню~~ объект мы имеем?
- Какие особенности имеет тип объекта?
- Какие отличия имеет объект от эталонного типа объекта?
- Какие методы решения существуют?

Эту стратегию следует зациклить до тех пор, пока задача не будет решена. Например, в исходных данных мы имеем дамп сетевого трафика. Проанализировав его, мы определили, что там передавались какие-то данные. После успешного (или не очень) извлечения мы получаем новый объект. Мы снова анализируем, что это за объект, какие он имеет особенности, что с ним не так и что с этим дальше делать.

Инструменты для решения задач _forensic_:

- Сетевые утилиты (_Wireshark, Tshark, Scapy_)
- Файловые утилиты (_file, head, hex-редакторы_)
- Утилиты для работы с ФС (_TSK, Foremost, Autopsy_)
- Крипто-утилиты (_Cryptool_)
- Графические редакторы (_GIMP, PS_)
- Аудиоредакторы (_Audacity, AU_)
- Языки программирования (_Python, C, ~~Brainfuck~~_)

---
### Пример задания

Один из тасков на соревнованиях PlaidCTF 2015 - **_Unknown_**.

Из исходных данных - файл непонятного содержания. Первое что приходит в голову - отдать файл утилите _file_ (КЭП рядом). Результат:

```
such@n00b:/tmp$ file unknown_2348c21020c876be4ae7d9eb19f8500a 
unknown_2348c21020c876be4ae7d9eb19f8500a: LaTeX document, ASCII text
 ```

Пробуем открыть редаткором LaTeXа - ничего вразумительного. Посмотрим любым текстовым редактором содержание файла, увидим следующее:

```
\begindata{raster,1}
2 0 65536 65536 0 0 640 400
bits 1 640 400
5a5c0b2f620b86f56c220475ab062
```

Погуглим значение первой строки (Нечто похожее на хедер какого-то файла). Первая же ссылка дает нам вполне вразумительную информацию о файле.

```
Format of ATK raster images

The raster data object writes a standard ATK data stream beginning with a \begindata line and ending with a \enddata line. Between these comes a header and possibly an image body.
 
The first line of the header looks like this:
 
2 0 65536 65536 0 0 484 603
```

Из статьи делаем вывод, что перед нами - растровое изображение какой-то ~~фигни~~ Andrew User Interface System. Расширение файла - **.CMU**.

Далее опять обращаемся к гуглу за тем, что же нам может открыть данный тип изображений, на что получаем ответ - _XnView_. Качаем программу, ставим, переименовываем файл в _unknown.CMU_, открываем, получаем результат - **flag{l0l_CMU_da_b3s}**