Я расскажу о позиционной системе счисления т.к. она используется в языке Assembler. Позиционная (двоичная, восьмеричная, десятичная, шестнадцатеричная) система счисления – такая, в которой значение цифры зависит от ее положения в числе, положения цифр в числе называют порядками или разрядами. Основанием позиционной системы счисления является счет, при достижении которого заполняется следующий порядок числа. Иначе, основание системы счисления равно числу цифр, включая ноль, которыми записываются числа в этой системе.

Ассемблер допускает возможность использования чисел в двоичной, восьмеричной, десятичной или шестнадцатеричной системе. По умолчанию ассемблер считает все числа, встречающиеся в программе, десятичными. Но остальные системы счисления можно указать при помощи тэгов (для MASM32 11 версии): b или y – для двоичных чисел; o или q – для восьмеричных; d или t – для десятичных чисел; h – для шестнадцатеричных чисел. Тэг записывается в конце числа, слитно с числом. Если в числе используются буквенные символы (шестнадцатеричные числа), в начале записывают ноль – по правилам ассемблера обозначения чисел должны начинаться с цифры. Например:

  .data 
      var1 byte 00001111b ; 15 в двоичном представлении 
      var2 byte 00001111y ; 15 в двоичном представлении 
      var3 byte 17o ; 15 в восьмеричном представлении 
      var4 byte 17q ; 15 в восьмеричном представлении 
      var5 byte 15d ; 15 в десятичном представлении 
      var6 byte 15t ; 15 в десятичном представлении 
      var7 byte 0Fh ; 15 в шестнадцатеричном представлении


Важно знать компьютер считает числа задом на перёд. Например - 1, 2, 3, 4, 5, 6, 7, 8, 9 = 1^6, 2^5, 3^4, 4^3, 5^2, 6^1, 7^0.


# Шестнадцатеричная система счисления

Шестнадцатиричная система использует 16 цифр. И поэтому основание в шестнадцатиричной системе равно 16.

  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F
  

Шестнадцатиричные числа являются компактными и легкими для чтения.  
Их легко преобразовать в двоичную систему и наборот. Каждый полубайт (4 бита) можно преобразовать в шестнадцатиричную цифру, пользуясь таблицей:

  ![[Screenshot_20220819_060011.png]]

Принято в конец шестнадцатиричного числа добавлять букву “h”, таким образом можно определить, что 5Fh – это шестнадцатиричное число, которому соответствует десятичное значение 95. Мы также добавляем “0” в начало шестнадцатиричного числа, если оно начинается с буквы (A..F), например 0E120h.

В вычислительной машине все числа хранятся в виде последовательностей из нулей и единиц. Когда мы в текст программы записываем какое-либо число, его перевод в машиночитаемое представление осуществляет ассемблер, и в исполняемый файл это число будет записано в надлежащем (двоичном) виде. Но организовывать вывод из программы числа в понятном уже пользователю формате мы должны сами, значит, тогда мы должны сделать в программе следующее:  

а) перевести число из двоичной системы в десятичную – из машинного представления в человеческое;  

б) заменить полученное десятичное число его символом, то есть соответствующей числу картинкой, поскольку монитор отображает именно картинки, а не числа.

Перевод машинного числа в заданную систему счисления осуществляется последовательным делением этого числа и получающегося результата на основание искомой системы счисления. Остаток от деления заносится в младший разряд, частное снова делится на основание системы счисления, остаток заносится в следующий разряд – и так до достижения в результате деления нуля. Допустим, требуется перевести десятичное число 250 в шестнадцатеричное представление:

  250 / 16 = 15, остаток = A (10), 
  15 / 16 = 0, остаток = F (15), 
  таким образом, 250 (десятичное) = FA (шестнадцатеричное).
  

Максимальной число, которое может быть записано в байт, составляет 255. Если по результатам работы программы необходимо вывести на экран число в десятичном формате из однобайтовой переменной, следует это число делить на 10 не более, чем три раза – в 255 три десятичных порядка. В переменных типа word (два байта) 
максимальное значение составляет 65 535, в переменных типа double word (четыре байта) – 4 294 967 295. Поэтому, числа word для перевода в десятичный формат делим на 10 не более пяти раз, double word -не более десяти раз. 

Если всё сказать коротко, то в 16-ном системе содержится 10 цифры и 6 букв (0,1,2,3,4,5,6,7,8,9,0,A,B,C,D,E,F). ТУТ - A = 10, B = 11, C = 12, D = 13, E = 14, F = 15
Шестнатцатиричная система удобнаяс, и ее используют для адресации у других вещец. В ассемблере шестнадцатиричные цифры заканчиваются букувкой h.Например - 1D7Ch. Или они могут начинаться с 0x. Например - 0x1D7C. Разницы это не имеет (окончания h и начало 0x) обе они говорять об одном и том же
(что число 16-ного формата).

Шестнадцатеричная система счисления состоит из 16 символов: `0-9` и `A-F`. Символы `A-F` используются для представления шестнадцатеричных цифр, соответствующих десятичным значениям с 10 по 15.

Шестнадцатеричные значения в вычислениях используются для сокращения длинных двоичных представлений. По сути, шестнадцатеричная система счисления представляет собой двоичные данные, деля каждый байт пополам и выражая значение каждого полубайта. В следующей таблице приведены десятичные, двоичные и шестнадцатеричные эквиваленты:


| Десятичное представление | Двоичное представление | Шестнадцатеричное представление |
| ------------------------ | ---------------------- | ------------------------------- |
| 0                        | 0                      | 0                               |
| 1                        | 1                      | 1                               |
| 2                        | 10                     | 2                               |
| 3                        | 11                     | 3                               |
| 4                        | 100                    | 4                               |
| 5                        | 101                    | 5                               |
| 6                        | 110                    | 6                               |
| 7                        | 111                    | 7                               |
| 8                        | 1000                   | 8                               |
| 9                        | 1001                   | 9                               |
| 10                       | 1010                   | A                               |
| 11                       | 1011                   | B                               |
| 12                       | 1100                   | C                               |
| 13                       | 1101                   | D                               |
| 14                       | 1110                   | E                               |
| 15                       | 1111                   | F                               |


Для конвертации бинарного числа в его шестнадцатеричный эквивалент разбейте бинарное число на 4 последовательные группы, начиная справа, и запишите эти группы поверх соответствующих цифр шестнадцатеричного числа.

**_Пример:_** Бинарное число 1000 (8) 1100 (C) 1101 (D) 0001 (1) эквивалентно шестнадцатеричному 8CD1.

Чтобы конвертировать шестнадцатеричное число в двоичное, просто запишите каждую шестнадцатеричную цифру в её 4-значный двоичный эквивалент.

**_Пример:_** Шестнадцатеричное число FAD8 эквивалентно двоичному 1111 (F) 1010 (A) 1101 (D) 1000 (8).



# Десятичная систе́ма счисления 

Десятичная систе́ма счисления  —  Это та система счислении которого мы привыкли видить каждый день, это например 10, 20, 106 и так далее. В десятичном системе счислении содержится всего 10 цифры: 0,1,2,3,4,5,6,7,8,9,0. И именно с этих 10 цифр мы создаём любое число: 100, 125, 23465, 168945 ... 

Большинство людей всегда используют десятичное представление числа. В десятичной системе 10 цифр:

  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
  

Цифрами можно представить любое значение, например:

  754
  

Значение формируется путем суммирования всех цифр, умноженных на основание в степени, равной позиции цифры (отсчет ведется с нуля):

  

![[num1.gif]]
  

Позиция каждой цифры – очень важный фактор. Например, если вы поместите “7” в конец (547), то это будет совсем другое значение:

  

![[num2.gif]]
  

Запомни: любое число в нулевой степени равно единице, даже ноль в нулевой степени равен 1:


![[num3.gif]]




# Двоичная система счисления



Компьютеры используют двоичную систему, которая использует всего две цифры:

  - 0
  - 1
  

И поэтому основание в двоичной системе равно 2. Каждая цифра в двоичном числе называется БИТ, 4 бита – это ПОЛУБАЙТ, 8 битов это БАЙТ, два байта – это СЛОВО, два слова – это ДВОЙНОЕ СЛОВО:

![[num4.gif]]



В конец двоичного числа принято добавлять букву “b”. Таким образом можно определить, что 101b – это двоичное число, которое соответствует десятичному значению 5.

Чисто технически было бы очень сложно сделать компьютер, который бы «понимал» десятичные числа. А вот сделать компьютер, который понимает двоичные числа достаточно легко. Двоичное число оперирует только двумя цифрами – 0 и 1. Несложно сопоставить с этими цифрами два состояния – вЫключено и включено (или **нет напряжения** – **есть напряжение**). Процессор – это микросхема с множеством выводов. Если принять, что отсутствие напряжения на выводе – это 0 (ноль), а наличие напряжения на выводе – это 1 (единица), то каждый вывод может работать с одной двоичной цифрой. Сейчас мы говорим о процессоре очень упрощённо, потому что мы изучаем не процессоры, а системы исчисления. Об устройстве процессора вы можете почитать здесь: [Структура процессора](http://av-assembler.ru/asm/afd/asm-cpu.htm).

Конечно, это касается не только процессоров, но и других составляющих компьютера, например, [шины данных](http://av-assembler.ru/asm/afd/asm-computer.htm) или [шины адреса](http://av-assembler.ru/asm/afd/asm-computer.htm). И когда мы говорим, например, о разрядности шины данных, мы имеем ввиду количество выводов на шине данных, по которым передаются данные, то есть о количестве двоичных цифр в числе, которое может быть передано по шине данных за один раз. Но о разрядности чуть позже.

Итак, процессор (и компьютер в целом) использует двоичную систему, которая оперирует всего двумя цифрами: 0 и 1. И поэтому **основание двоичной системы** равно 2. Аналогично, основание десятичной системы равно 10, так как там используются 10 цифр.

Каждая цифра в двоичном числе называется **бит** (или **разряд**). Четыре бита – это **полубайт** (или **тетрада**), 8 бит – **байт**, 16 бит – **слово**, 32 бита – **двойное слово**. Запомните эти термины, потому что в программировании они используются очень часто. Возможно, вам уже приходилось слышать фразы типа **слово данных** или **байт данных**. Теперь, я надеюсь, вы понимаете, что это такое.

Отсчёт битов в числе начинается с нуля и справа. То есть в двоичном числе самый **младший бит** (нулевой бит) является крайним справа. Слева находится **старший бит**. Например, в слове старший бит – это 15-й бит, а в байте – 7-й. В конец двоичного числа принято добавлять букву **b**. Таким образом вы (и ассемблер) будете знать, что это двоичное число. Например, 101 – это десятичное число, а 101b – это двоичное число, которое эквивалентно десятичному числу 5.

А теперь попробуем понять, как формируется **двоичное число**.

Ноль, он и в Африке ноль. Здесь вопросов нет. Но что дальше. А дальше разряды двоичного числа заполняются по мере увеличения этого числа. Для примера рассмотрим тетраду. Тетрада (или полубайт) имеет 4 бита.

Итак, мы видим, что при формировании двоичных чисел разряды числа заполняются нулями и единицами в определённой последовательности:

Если младший равен нулю, то мы записываем туда единицу. Если в младшем бите единица, то мы переносим её в старший бит, а младший бит очищаем. Тот же принцип действует и в десятичной системе:

0…9
10 – очищаем младший разряд, а в старший добавляем 1

Всего для тетрады у нас получилось 16 комбинаций. То есть в тетраду можно записать 16 чисел от 0 до 15. Байт – это уже 256 комбинаций и числа от 0 до 255. Ну и так далее. На рис. 2.2 показано наглядно представление двоичного числа (двойное слово).

0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
...
Все устройства (а именно процессор устройства и другие его части) работают по такому принципу. Но только вместо 0 это когда нет тока, а 1 ток есть. можно разным способам считать двоичную систему. Первый способ:
  Если есть заряд то это 1 и если добовляется единица то наш один не может стать два потому что у нас только 0 и 1, так как быть. Наща единица передаётся соседнему биту (старшему) и предыдущий который содержал 1 освобождается и превращается в 0 и единица который добавляется приходить на место предыдущего единичка, который передал свою единицу страшеиу биту. И
  
  так идёт до бесконечности:
  
    0 = 0000
    1 = 0001
    2 = 0010
    3 = 0011
    4 = 0100
    5 = 0101
    6 = 0110
    7 = 0111
    8 = 1000
    9 = 1001
    ...
    
Второй способ:

1)Мы просто делим число на два берем результат и его делим два и записываем остаток.

2)Берем результат и его делим на два и записываем остаток.

3)Делаем все это до тех пор пока результат не будет 0.
Если при деление есть остаток то это один, а если его нет то это ноль.
И потом на полседок мы переварачиваем полученный результат и переварачиваем его, так мы конвертируем десятичное число в двоичную.

    5 = 101
    5/2 = 2 Остаток - 1
    2/2 = 1 Остаток - 0
    1/2 = 0 Остаток - 1

Результат: 101
     
     20 = 10100 
    20/2 = 10 Остаток - 0
    10/2 = 5 Остаток - 0
    5/2 = 2 Остаток - 1
    2/2 = 1 Остаток - 0
    1/2 = 0 Остаток - 1

И иы получили - 00101. И чтобы получить результат нужно переварачивать то что мы
получили. В нашем случае 00101 - 10100.
Результат: 10100

И можно переводить числа из одной системы счисления в другую например из десятичной в двоичную, из двоичной десятичной, из десятичной в восьмеричной и т.д. например давайте преобразуем десятичные числа в восьмеричной:
(77)^8 = 7 * 8^1 + 7 * 8^0 = 63

Например 1234 десятичном виде:
1 * 10^3 + 2 * 10^2 + 3 * 10^1 + 4 * 10^0 = 1234

Мы просто умножаем число на десят по цифрам со степенью по его расположении.
Как это степень по егот расположении?? Ну это типа он получает его по позиции Например:

     12345678

8 получает степень 0 потому что оно на самом первом.
1 получает степень 7 потому что он самый полследний.
А почему 8 самый полследний и получает степень 0, а 1 самый последний
и получает степень 7 (последний степень)? Как было упомянуто выше компьютер рассчитывает числа в обратном направлении он просто все переварачивает.
Короче примере преобразования десятичных и восьмеричный чисел, нам нужно просто умножить число на его систему (это восьмеричной десятичной) в степени где оно находится, степени считается обратном виде.


## ravesli
Каждая система счисления использует позиционные обозначения разрядов чисел (их значений). Каждое следующее позиционное значение состоит из предыдущего позиционного значения, умноженного на 2 (именно на 2, так как это бинарная система, которая состоит из двух чисел). Если битом является `1`, то позиционное значение умножается на 2, а если `0` — позиционное значение остается `0`. В бинарной системе счисления отсчет ведется справа налево, а не слева направо (как в десятичной системе).

Например, в следующей таблице показаны позиционные значения 8-битного двоичного числа `11111101`:


| Бит                  | 1   | 1  | 1  | 1  | 1 | 1 | 0 | 1 |
| -------------------- | --- | -- | -- | -- | - | - | - | - |
| Позиционное значение | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| Номер бита           | 7   | 6  | 5  | 4  | 3 | 2 | 1 | 0 |

Значение бинарного числа равно сумме позиционных значений всех бит:

`1 + 4 + 8 + 16 + 32 + 64 + 128 = 253`

Двоичное `11111101` = десятичное `253`.

**_Примечание:_** Детально о конвертации чисел из двоичной системы в десятичную и наоборот, а также о сложении двоичных чисел, читайте в материалах [**урока №44**](https://ravesli.com/urok-44-perevod-chisel-iz-dvoichnoj-sistemy-v-desyatichnuyu-i-naoborot/).


