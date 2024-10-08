
# Описание

**string.h** — [заголовочный файл](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BE%D1%87%D0%BD%D1%8B%D0%B9_%D1%84%D0%B0%D0%B9%D0%BB) [стандартной библиотеки языка Си](https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%B0%D1%8F_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B0_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_%D0%A1%D0%B8), содержащий функции для работы со [строками](https://ru.wikipedia.org/wiki/%D0%9D%D1%83%D0%BB%D1%8C-%D1%82%D0%B5%D1%80%D0%BC%D0%B8%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B0) и различными функциями работы с памятью. Эта библиотека определяет несколько функций для обработки Cи-строк и массивов. В таблице кратко описаны функции, макросы и типы данных этого заголовочного файла. Простыми словами, библиотека string.h предоставляет функции для работы со строками (zero-terminated strings) в си, а также несколько функций для работы с массивами, которые сильно упрощают жизнь.

**string.h** — это заголовок в стандартной библиотеке C для языка программирования C, который содержит макроопределения, константы и объявления функций и типов, используемых не только для обработки строк, но и различных функций обработки памяти; Таким образом, это имя является неправильным.

Язык [C](https://en.wikipedia.org/wiki/C_(programming_language) "С (язык программирования)") набор функций, реализующих операции над [строками](https://en.wikipedia.org/wiki/String_(computer_science) "Строка (информатика)") (строками символов и строками байтов) [стандартной библиотеке](https://en.wikipedia.org/wiki/C_standard_library "Стандартная библиотека C") . Поддерживаются различные операции, такие как копирование, [конкатенация](https://en.wikipedia.org/wiki/Concatenation "Конкатенация") , [токенизация](https://en.wikipedia.org/wiki/Tokenization_(lexical_analysis) "Токенизация (лексический анализ)") и поиск. Для символьных строк в стандартной библиотеке используется соглашение о том, что строки [заканчиваются нулем](https://en.wikipedia.org/wiki/Null-terminated_string "Строка с завершающим нулем") : строка из n символов представляется как [массив](https://en.wikipedia.org/wiki/Array_(data_structure) "Массив (структура данных)") из _n_ + 1 элементов, последним из которых является `NUL`символ (с числовым значением 0).

Единственная поддержка строк в самом языке программирования заключается в том, что компилятор переводит [строковые константы](https://en.wikipedia.org/wiki/String_literal "Строковый литерал") в кавычках в строки с завершающим нулем. 
Функции, объявленные в `string.h`чрезвычайно популярны, поскольку как часть [стандартной библиотеки C](https://www.prowaretech.com/wiki/C_standard_library "Стандартная библиотека C") они гарантированно работают на любой платформе, поддерживающей C. Однако с этими функциями существуют некоторые проблемы безопасности, такие как [переполнение буфера](https://www.prowaretech.com/wiki/Buffer_overflow "Переполнение буфера") , что заставляет программистов предпочитать более безопасные и, возможно, менее переносимые варианты.

Кроме этого, строковые функции работают только с набором символов ASCII или его совместимыми расширениями, такими как ISO-8859-1; многобайтовые кодировки такие как UTF-8 будут работать, с отличием, что «длина» строки будет определяться как число байтов, а не число символов Юникода, которым они соответствуют. Несовместимые с ASCII строки обычно обрабатываются кодом описанным в wchar.h.
  

Большинство функций string.h не производят никакого выделения памяти и контроля границ; эта обязанность целиком возлагается на программиста.

Если максимально просто то `<string.h>` Заголовочный файл объявляет набор функций для работы со строками. 


Заголовок **string.h** определяет один тип переменной, один макрос и различные функции для работы с массивами символов.

## Библиотечные переменные

Ниже приведен тип переменной, определенный в заголовке string.h —

- **size_t**  - Это целочисленный тип без знака, который является результатом **sizeof** .


## Библиотечные макросы

Ниже приведен макрос, определенный в заголовке string.h —

- **NULL** - Этот макрос является значением константы нулевого указателя.

## Функции string.h

Ниже приведены функции, определенные в заголовке string.h:

Имя 	                                                                                                        Заметки

- void *memcpy(void *dest, const void *src, size_t n);  копирует n байт между двумя областями памяти, которые не должны перекрываться
- void *memccpy(void *dest, const void *src, int c, size_t n);	копирует до n байтов между двумя областями памяти, которые не должны перекрываться, останавливаясь при обнаружении байта c
- void *memmove(void *dest, const void *src, size_t n); 	копирует n байт между двумя областями памяти; в отличие от memcpyобласти могут пересекаться
- void *memchr(const void *s, int c, size_t n); 	возвращает указатель на первое вхождение c в первых n байтах s или NULL, если не найден
- int memcmp(const void *s1, const void *s2, size_t n); 	сравнивает первые n символов двух областей памяти
- void *memset(void *, int, size_t); 	перезаписывает область памяти шаблоном байтов
- char *strcat(char *dest, const char *src); 	добавляет строку src к dest
- char *strncat(char *, const char *, size_t); 	добавляет не более n символов строки src к dest
- char *strchr(const char *, int); 	находит символ в строке, ища с начала
- char *strrchr(const char *, int); 	находит символ в строке, ища с конца
- int strcmp(const char *, const char *); 	сравнивает две строки численно
- int strncmp(const char *, const char *, size_t); 	численно сравнивает до первых n байтов двух строк
- int strcoll(const char *, const char *); 	текущей локали , порядок сортировки
- char *strcpy(char *, const char *); 	копирует строку из одного места в другое
- char *strncpy(char *, const char *, size_t); 	копирует до n байтов строки из одного места в другое
- char *strerror(int); 	возвращает строковое представление errno (не потокобезопасное)
- int *strerror_r(int, char *, size_t); 	возвращает строковое представление errno (потокобезопасное; некоторые различия в семантике между GNU и XSI / POSIX )
- size_t strlen(const char *); 	находит длину строки C
- size_t strspn(const char *s, const char *accept); 	определяет длину максимальной начальной подстроки s, полностью состоящей из символов в accept
- size_t strcspn(const char *s, const char *reject); 	определяет длину максимальной начальной подстроки s, полностью состоящей из символов, не находящихся в отклонении
- char *strpbrk(const char *s, const char *accept); 	находит первое вхождение любого символа в accept в s
- char *strstr(const char *haystack, const char *needle); 	находит первое вхождение иглы в стоге сена
- char *strtok(char *, const char *); 	разбирает строку на последовательность токенов; не потокобезопасный
- char *strtok_r(char *, const char *, char **); 	потокобезопасная версия strtok
- size_t strxfrm(char *dest, const char *src, size_t n); 	преобразует src в форму сопоставления, так что числовой порядок сортировки преобразованной строки эквивалентен порядку сопоставления src. 

### Wiki:

strcpy[11] 	    wcscpy[12] 	    Копирует одну строку в другую
strncpy[13] 	wcsncpy[14]     	Записывает ровно n байт, копируя из источника или добавляя нули
strcat[15] 	    wcscat[16] 	        Добавляет одну строку к другой
strncat[17] 	    wcsncat[18] 	    Добавляет не более n байтов из одной строки в другую
strxfrm[19] 	wcsxfrm[20] 	    Преобразует строку в соответствии с текущей локалью
strlen[21] 	    wcslen[22] 	    Возвращает длину строки
strcmp[23] 	wcscmp[24] 	    Сравнивает две строки ( трехстороннее сравнение )
strncmp[25] 	wcsncmp[26] 	Сравнивает определенное количество байтов в двух строках
strcoll[27] 	    wcscoll[28] 	    Сравнивает две строки в соответствии с текущей локалью
strchr[29] 	    wcschr[30] 	    Находит первое вхождение байта в строку
strrchr[31] 	    wcsrchr[32] 	    Находит последнее вхождение байта в строку
strspn[33] 	    wcsspn[34] 	    Возвращает количество начальных байтов в строке, которые находятся во второй строке.
strcspn[35] 	wcscspn[36] 	    Возвращает количество начальных байтов в строке, которых нет во второй строке.
strpbrk[37] 	wcspbrk[38] 	    Находит в строке первое вхождение байта в наборе
strstr[39] 	    wcsstr[40] 	        Находит первое вхождение подстроки в строку
strtok[41] 	    wcstok[42] 	    Разбивает строку на токены
strerror[43]  	                            Возвращает строку, содержащую сообщение, полученное из кода ошибки
memset[44] 	wmemset[45] 	Заполняет буфер повторяющимся байтом
memcpy[46] 	wmemcpy[47] 	Копирует один буфер в другой
memmove[48] 	wmemmove[49] 	Копирует один буфер в другой, возможно, перекрывающийся буфер
memcmp[50] 	wmemcmp[51] 	        Сравнивает два буфера (трехстороннее сравнение)
memchr[52] 	wmemchr[53] 	        Находит первое вхождение байта в буфер

#### Многобайтовые функции

Имя 	Описание

mblen[54] 	        Возвращает количество байтов в следующем многобайтовом символе
mbtowc[55] 	    Преобразует следующий многобайтовый символ в расширенный символ
wctomb[56] 	    Преобразует расширенный символ в его многобайтовое представление
mbstowcs[57] 	Преобразует многобайтовую строку в широкую строку
wcstombs[58] 	Преобразует широкую строку в многобайтовую строку
btowc[59]           Преобразует однобайтовый символ в широкий символ, если это возможно
wctob[60] 	        Преобразует широкий символ в однобайтовый символ, если это возможно
mbsinit[61] 	    Проверяет, представляет ли объект состояния начальное состояние
mbrlen[62] 	    Возвращает количество байтов в следующем многобайтовом символе в заданном состоянии
mbrtowc[63] 	    Преобразует следующий многобайтовый символ в широкий символ, учитывая состояние
wcrtomb[64] 	    Преобразует расширенный символ в его многобайтовое представление с заданным состоянием
mbsrtowcs[65] 	Преобразует многобайтовую строку в широкую строку с заданным состоянием
wcsrtombs[66] 	Преобразует широкую строку в многобайтовую строку с заданным состоянием 

Все  функции (**многобайтовые функции**) принимают указатель на mbstate_t объект, который вызывающая сторона должна поддерживать. Первоначально это было предназначено для отслеживания состояний переключения в мб кодировки, а современные типа UTF-8 в этом не нуждаются. Однако эти функции были разработаны исходя из предположения, что Туалет кодирование не является кодированием [переменной ширины](https://en.wikipedia.org/wiki/Variable-width_encoding "Кодирование переменной ширины") и поэтому предназначено для работы только с одним wchar_t за раз, передавая его по значению, а не используя указатель на строку. Поскольку UTF-16 является кодировкой переменной ширины, mbstate_t был повторно использован для отслеживания суррогатных пар в широком кодировании, хотя вызывающая сторона по-прежнему должна обнаруживать и вызывать mbtowc дважды для одного символа. 


#### Числовые преобразования

| Байт                    | Широкий                 | Описание                                                                                                |
| ----------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------- |
|                         |                         |                                                                                                         |
|                         |                         |                                                                                                         |
| atof[70]                | —                       | преобразует строку в значение с плавающей запятой («atof» означает «ASCII в число с плавающей запятой») |
| atoi, atol, atoll       |                         | преобразует строку в целое число ( C99 ) («atoi» означает «ASCII в целое число»)                        |
| strtof, strtod, strtold | wcstof, wcstod, wcstold | преобразует строку в значение с плавающей запятой                                                       |
| strtold, strtoll        | wcstold, wcstoll        | преобразует строку в целое число со знаком                                                              |
| strtol, strtoll         | wcstol, wcstoll         | преобразует строку в целое число со знаком                                                              |
| strtoul, strtoull       | wcstoul, wcstoull       | преобразует строку в беззнаковое целое                                                                  |


#### Популярные расширения


| Имя            | Платформа    | Описание                                                                                                                                           |
| -------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| bzero[83] [84] | POSIX , БСД  | Заполняет буфер нулевыми байтами, устарело memset                                                                                                  |
| memccpy[85]    | СВИД , POSIX | копирует заданное количество байтов между двумя областями памяти, которые не должны перекрываться, останавливаясь при обнаружении заданного байта. |
| mempcpy[86]    | ГНУ          | вариант memcpyвозврат указателя на байт, следующий за последним записанным байтом                                                                  |
| strcasecmp[87] | POSIX, БСД   | нечувствительные к регистру версии strcmp                                                                                                          |
| strcat_s[88]   | Окна         | вариант strcatкоторый проверяет размер буфера назначения перед копированием                                                                        |
| strcpy_s[89]   | Окна         | вариант strcpyкоторый проверяет размер буфера назначения перед копированием                                                                        |
| strdup[90]     | POSIX        | выделяет и дублирует строку                                                                                                                        |
| strerror_r[91] | POSIX 1, GNU | вариант strerrorэто потокобезопасно. Версия GNU несовместима с версией POSIX.                                                                      |
| stricmp[92]    | Окна         | нечувствительные к регистру версии strcmp                                                                                                          |
| strlcpy[93]    | БСД, Солярис | вариант strcpyкоторый усекает результат, чтобы он поместился в буфере назначения [94]                                                              |
| strlcat[93]    | БСД, Солярис | вариант strcatкоторый усекает результат, чтобы он поместился в буфере назначения [94]                                                              |
| strsignal[95]  | POSIX:2008   | возвращает строковое представление кода сигнала . Не потокобезопасный.                                                                             |
| strtok_r[96]   | POSIX        | вариант strtokэто потокобезопасный                                                                                                                 |

## Замены

Несмотря [на установленную необходимость](https://en.wikipedia.org/wiki/C_standard_library#Buffer_overflow_vulnerabilities "Стандартная библиотека C") замены `strcat`[[15]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-strcat-cppreference-16) и `strcpy`[[11]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-strcpy-cppreference-12) с функциями, не допускающими переполнения буфера, общепринятого стандарта не возникло. Отчасти это связано с ошибочным мнением многих программистов на C, что `strncat`а также `strncpy`иметь желаемое поведение; однако ни одна из функций не была предназначена для этого (они были предназначены для манипулирования строковыми буферами фиксированного размера, дополненными нулями, формат данных менее часто используется в современном программном обеспечении), а поведение и аргументы неинтуитивны и часто написаны неправильно даже экспертом. программисты. [[94]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-strl-96)

Наиболее популярной [[a]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-99) являются `strlcat`а также `strlcpy`функции, которые появились в [OpenBSD](https://en.wikipedia.org/wiki/OpenBSD "OpenBSD") 2.4 в декабре 1998 года. [[94]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-strl-96) Эти функции всегда записывают один NUL в буфер назначения, усекая результат при необходимости, и возвращают размер буфера, который был бы необходим, что позволяет обнаружить усечение и обеспечивает размер для создания нового буфера, который не будет усекаться. Их критиковали за то, что они якобы неэффективны, [[97]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-100) поощряют использование струн C (вместо какой-либо более совершенной альтернативной формы струн), [[98]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-libc-alpha-discussion-1-101) [[99]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-102) и скрывают другие потенциальные ошибки. [[100]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-103) [[101]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-104) Следовательно, они не были включены в [библиотеку GNU C](https://en.wikipedia.org/wiki/GNU_C_library "библиотека GNU C") (используемую программным обеспечением в Linux), хотя они реализованы в библиотеках C для OpenBSD, [FreeBSD](https://en.wikipedia.org/wiki/FreeBSD "FreeBSD") , [NetBSD](https://en.wikipedia.org/wiki/NetBSD "NetBSD") , [Solaris](https://en.wikipedia.org/wiki/Solaris_(operating_system) "Солярис (операционная система)") , [OS X](https://en.wikipedia.org/wiki/OS_X "ОС Х") и [QNX](https://en.wikipedia.org/wiki/QNX "QNX") , как а также в альтернативных библиотеках C для Linux [,](https://en.wikipedia.org/wiki/Musl "мусульманин") 2011 [musl](https://en.wikipedia.org/wiki/C_string_handling#cite_note-105) [как](https://en.wikipedia.org/wiki/C_string_handling#cite_note-106) представленный [,](https://en.wikipedia.org/wiki/Specification_and_Description_Language "Язык спецификации и описания") году [в](https://en.wikipedia.org/wiki/GLib "GLib") таких [.](https://en.wikipedia.org/wiki/FFmpeg "FFmpeg") , [rsync](https://en.wikipedia.org/wiki/Rsync "Rsync") и даже внутри [Ядро линукса](https://en.wikipedia.org/wiki/Linux_kernel "ядро Linux") . Доступны реализации этих функций с открытым исходным кодом. [[104]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-107) [[105]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-108)

Иногда `memcpy`[[46]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-memcpy-cppreference-47) или `memmove`[[48]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-memmove-cppreference-49) , так как они могут быть более эффективными, чем `strcpy`так как они повторно не проверяют наличие NUL (на современных процессорах это менее актуально). Поскольку им требуется длина буфера в качестве параметра, правильная установка этого параметра может избежать переполнения буфера.

2004 [жизненного цикла разработки безопасности](https://en.wikipedia.org/wiki/Microsoft_Security_Development_Lifecycle "Жизненный цикл разработки безопасности Майкрософт") года Microsoft представила семейство «безопасных» функций, включая `strcpy_s`а также `strcat_s`(вместе со многими другими). [[106]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-109) Эти функции были стандартизированы с некоторыми незначительными изменениями как часть необязательного [C11 (Приложение K)](https://en.wikipedia.org/wiki/C11_(C_standard_revision) "C11 (стандартная версия C)") , предложенного ISO/IEC WDTR 24731. Эти функции выполняют различные проверки, включая проверку того, не является ли строка слишком длинной для размещения в буфере. Если проверки не пройдены, вызывается указанная пользователем функция «обработчика ограничений времени выполнения», [[107]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-110) которая обычно прерывает выполнение программы. [[108]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-111) [[109]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-112) Некоторые функции выполняют деструктивные операции перед вызовом обработчика ограничений времени выполнения; Например, `strcat_s`устанавливает назначение в пустую строку [[110]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-113) , что может затруднить восстановление после ошибок или их отладку. Эти функции вызвали серьезную критику, поскольку изначально они были реализованы только в Windows, и в то же время [Microsoft Visual C++](https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B "Microsoft визуальный С++") предлагающие программистам использовать эти функции вместо стандартных. Некоторые предполагают, что это попытка Microsoft привязать разработчиков к своей платформе. [[111]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-114) Хотя доступны реализации этих функций с открытым исходным кодом, эти функции отсутствуют в общих библиотеках Unix C. [[112]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-115) Опыт работы с этими функциями показал значительные проблемы с их принятием и ошибки в использовании, поэтому предлагается исключить Приложение K из следующего пересмотра стандарта C. [[113]](https://en.wikipedia.org/wiki/C_string_handling#cite_note-116) Использование `memset_s`также был предложен как способ избежать нежелательных оптимизаций компилятора.


  
  

# Пример использование некоторых функции библиотеки string.h:

  
## strlien() - Это функция возвращает длину строки.

**Синтаксис:**

> size_t strlen ( const char * str )

**size_t** представляет беззнаковый шорт

  
  
**Пример****:

>
**#include <stdio.h>**
**#include <string.h>**
>
**int main(){**
>
**char str1[20] = "BeginnersBook";**
>
**printf("Length of string str1: %d", strlen(str1));**
>
**return 0;**
>
**}**
>

**Вывод****:**

Length of string str1: 13

## strcmp()

****strcmp()**** **-** **Это функция с**равнивает две строки и возвращает целочисленное значение. Если обе строки одинаковы (равны), то эта функция вернет 0, иначе она может вернуть отрицательное или положительное значение на основе сравнения.
 

**Синтаксис****:
  

>**int strcmp ( const char * str1 , const char * str2 )**
  

**Если строка1 < строка2 ИЛИ строка1 является подстрокой строки2** , то результатом будет отрицательное значение. Если строка1 > строка2, то будет возвращено положительное значение.  
**Если string1 == string2** , то вы получите 0 (ноль) при использовании этой функции для сравнения строк.

  

**Пример** **strcmp****:


>
**#include <stdio.h>**
**#include <string.h>**
>
**int main(){**
>
**char s1[20] = "BeginnersBook";**
>
**char s2[20] = "BeginnersBook.COM";**
>
 if (strcmp(s1, s2) ==0)**{**
>
**printf("string 1 and string 2 are equal");**
>
**}else**
>
**{**
>
**printf("string 1 and 2 are different");**
>
**}**
>
**return 0;**
>
**}**
>


**Вывод****:

string 1 and 2 are different

  
  

****strcat()**** **-** **Это функция** объединяет две строки и возвращает объединенную строку.

****Синтаксис********:****

char * strcat ( char * str1 , char * str2 )

**Пример****:

>
**#include <stdio.h>**
**#include <string.h>**
>
**int main(){**
>
**char s1[10] = "Hello";**
**char s2[10] = "World";**
>
**strcat(s1,s2);**
**printf("Output string after concatenation: %s", s1);**
>
**return 0;**
**}**

**Вывод****:**

Output string after concatenation: HelloWorld



## strcpy 

**strcpy()** - Это функция копирует строку str2 в строку str1, включая конечный символ (ограничитель char '\0').

**Пример****:

>
**#include <stdio.h>**
**#include <string.h>**
>
**int main(){**
>
**char s1[30] = "string 1";**
>
**char s2[30] = "string 2 : I’m gonna copied into s1";**
>
**/* this function has copied s2 into s1*/**
>
**strcpy(s1,s2);**
>
**printf("String s1 is: %s", s1);**
>
**return 0;**
>
**}**

**Вывод****:**

String s1 is: string 2: I’m gonna copied into s1

## memcpy  

**memcpy()** - Это функция используется для копирования блока памяти из одного места в другое.

**Синтаксис****:

>void *memcpy(void *dest, const void * src, size_t n)


## Параметры

- **dest** — это указатель на целевой массив, в который должно быть скопировано содержимое, с приведением типа к указателю типа void*.

- **src** — это указатель на источник копируемых данных, приведенный к типу указателя типа void *.

- **n** — это количество копируемых байтов.

  

  
  

**Пример****:

>
**#include <stdio.h>**
**#include <string.h>**
>
**int** **main ()**
>
**{**
>
  **char** **str1[] = "Geeks";** 
  **char** **str2[] = "Quiz";** 
  **puts("str1 before memcpy ");**
  **puts(str1);**
>
  **/* Copies contents of str2 to str1 */**
>
  **memcpy** **(str1, str2, sizeof(str2));**
>
  **puts("\nstr1 after memcpy ");**
  **puts(str1);**
>
  **return** **0;**
**}**
>
  

**Вывод****:**

str1 before memcpy
Geeks  

str1 after memcpy
Quiz
