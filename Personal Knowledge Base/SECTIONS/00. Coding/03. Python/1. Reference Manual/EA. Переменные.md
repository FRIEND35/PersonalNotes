## Что такое переменные

Переменные — это контейнеры для хранения значений данных.

Переменная (от англ. variable) — поименованная или адресуемая иным способом область памяти, которую можно использовать для доступа к данным. Звучит сложно и пугающе, не правда ли? Однако на практике такое определение вашему ребенку не потребуется. По крайней мере, на начальных этапах изучения программирования.

Переменная простыми словами — это хранилище данных. Сюда можно положить какое-то значение (например, число, строку или другой тип данных). Еще более простой вариант представить себе переменную — подумать о том, что нас окружает. Например, переменной может быть какой-то небольшой мешочек, куда можно положить, к примеру, яблоко. Оно будет там находиться до тех пор, пока мы не решим произвести с яблоком какие-то действия. 

Переменную в любой программе необходимо объявлять. То есть достать этот мешочек перед тем, как положить в него яблоко. В современных приложениях переменных может быть сколько угодно много. Например, в одном мешочке хранится яблоко, в другом — конфета.

Переменные — это не что иное, как зарезервированные области памяти для хранения значений. Это означает, что когда вы создаете переменную, вы резервируете место в памяти. В зависимости от типа данных переменной интерпретатор выделяет память и решает, что можно хранить в зарезервированной памяти. Следовательно, присваивая переменным разные типы данных, вы можете хранить в этих переменных целые числа, десятичные дроби или символы. Простыми словами, переменные — это контейнеры для хранения значений данных. И когда нам
нужно мы берем значение из переменной и при необходимости выполняем над ним какие небудь операции.

В переменных хранятся определенные данные, которые можно впоследствии использовать в программе. Для того, чтобы переменная появилась, необходимо ее объявить (зарезервировать ячейку памяти под определенные данные). В разных языках переменные объявляются по-разному в зависимости от синтаксиса. Где-то это может быть слово «var», где-то «let». Существуют также неизменяемые переменные, которые задаются только раз и объявляются словом «const».  
  
Переменные в программе нужны не только для хранения данных, но и для различных операций с ними. Например, можно создать простой калькулятор, используя всего три переменные — a, b и c. Как это будет работать? Не углубляясь в тонкости синтаксиса каждого отдельно взятого языка программирования, покажем простой пример:  
  
a+b =c  
  
То есть у нас есть три переменные. Первые две используются для вычисления, а третья служит для того, чтобы в нее записывалось значение суммы. Причем первые две переменные могут быть с заданными исходными значениями, а могут быть и пустыми (то есть переменная объявляется, но ей не присваивается никакое значение). Во втором случае, можно самим подставлять значения и на их основе будут производиться расчеты.  
  
Кстати, данные можно записывать сразу в программе. Если взять наш пример выше, вместо латинских букв мы можем сразу же использоваться цифры. Например, 1+2 = 3. Однако в этом случае программа, которую вы напишете, не будет обладать должной гибкостью. То есть можно посчитать в ней только заданные значения и для того, чтобы что-то изменить, каждый раз придется в коде писать новые числа и только тогда мы получим другой результат.  
  
Переменные позволяют добавить гибкости приложению. То есть мы сами можем менять их значения и каждый раз получать необходимые результаты без вмешательства в код программы.

## Создание переменных

В Python нет команды для объявления переменной.

Переменная создается в тот момент, когда вы впервые присваиваете ей значение.

```python
x = 5  
y = "John"  
print(x)  
print(y)
```

Переменные не нужно объявлять с каким-либо конкретным _типом_ , и они могут даже изменить тип после того, как они были установлены.

```python
x = 4       # x is of type int  
x = "Sally" # x is now of type str  
print(x)
```

---

## Присвоение значений переменным

Переменные Python не нуждаются в явном объявлении для резервирования памяти. Объявление происходит автоматически, когда вы присваиваете значение переменной. Знак равенства (=) используется для присвоения значений переменным. 

Операнд слева от оператора = — это имя переменной, а операнд справа от оператора = — это значение, хранящееся в переменной. Инными словами, в Python нет команды для объявления переменной. Переменная создается в тот момент, когда вы впервые присваиваете ей значение.

```python
#!/usr/bin/python

counter = 100    # An integer assignment
miles  = 1000.0  # A floating point
name  = "John"   # A string

print(counter)
print(miles)
print(name)



```

Здесь 100, 1000.0 и «Джон» — это значения, присвоенные counter , miles и name переменным соответственно. Это дает следующий результат —

**100
1000.0
John

Множественное назначение Python позволяет одновременно присваивать одно значение нескольким переменным. Например:
`a = b = c = 1

---

## Кастинг

Если вы хотите указать тип данных переменной, это можно сделать с помощью приведения типов.

```python
x = str(3)    # x will be '3'  
y = int(3)    # y will be 3  
z = float(3)  # z will be 3.0
```

---

---

## Получить тип

Вы можете получить тип данных переменной с помощью `type()`функция.

```python
x = 5  
y = "John"  
print(type(x))  
print(type(y))
```

Вы узнаете больше о [типы данных](https://www.w3schools.com/python/python_datatypes.asp) и [кастинг](https://www.w3schools.com/python/python_casting.asp) позже в этом уроке.

---

## Одинарные или двойные кавычки?

Строковые переменные могут быть объявлены с использованием одинарных или двойных кавычек:

```python
x = "John"  
# is the same as  
x = 'John'
```

---

## Деликатный случай

Имена переменных чувствительны к регистру.

Это создаст две переменные:

```python
a = 4  
A = "Sally"  

#A will not overwrite a
```

## Имена переменных

Переменная может иметь короткое имя (например, x и y) или более описательное имя (возраст, имя автомобиля, общий_объем). Правила для переменных Python:

-   Имя переменной должно начинаться с буквы или символа подчеркивания.
-   Имя переменной не может начинаться с цифры или такими символами как: !@#$%^&*( - так нельзя!
-   Имя переменной может содержать только буквенно-цифровые символы и символы подчеркивания (Az, 0–9 и _ ).
-   Имена переменных чувствительны к регистру (age, Age и AGE — это три разные переменные).


Допустимые имена переменных:

```python
myvar = "John"  
my_var = "John"  
_my_var = "John"  
myVar = "John"  
MYVAR = "John"  
myvar2 = "John"
```

опустимые имена переменных:


```python
2myvar = "John"  
my-var = "John"  
my var = "John"
```

Помните, что имена переменных чувствительны к регистру.

---

---

## Имена переменных из нескольких слов

Имена переменных, состоящие более чем из одного слова, могут быть трудночитаемыми.

Есть несколько методов, которые вы можете использовать, чтобы сделать их более читабельными:

## Верблюжий чехол

Каждое слово, кроме первого, начинается с заглавной буквы:

`myVariableName = "John"

---

## Паскаль Кейс

Каждое слово начинается с заглавной буквы:

`MyVariableName = "John"

---

## Змеиный случай

Каждое слово отделяется символом подчеркивания:

`my_variable_name = "John"

---

## Одно значение для нескольких переменных

И вы можете присвоить одно и то _же_ значение нескольким переменным в одной строке:

```python
x = y = z = "Orange"  

print(x)  
print(y)  
print(z)
```

---

## Множество значений для нескольких переменных

Python позволяет вам присваивать значения нескольким переменным в одной строке:

```python
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)
```

Результат выполнения программы:

**Orange
Banana
Cherry

## Распаковать коллекцию

Если у вас есть набор значений в списке, кортеже и т. Python позволяет извлекать значения в переменные. Это называется
распаковкой .

Распаковать список:

```python
fruits = ["apple", "banana", "cherry"]

x, y, z = fruits

print(x)
print(y)
print(z)
```

Результат выполнения программы:

**apple
banana
cherry

---

## Выходные переменные

Питон `print()`функция часто используется для вывода переменных.

```python
x = "Python is awesome"  

print(x)
```

в `print()`функция, вы выводите несколько переменные, разделенные запятой:

```python
x = "Python"  
y = "is"  
z = "awesome"  

print(x, y, z)
```

Вы также можете использовать `+`оператор для вывода несколько переменных:

```python
x = "Python "  
y = "is "  
z = "awesome"  

print(x + y + z)
```

Обратите внимание на пробел после `"Python "`а также `"is "`, без них результат был бы "Pythonisawesome".

Для чисел, `+`символ работает как математический оператор:

```python
x = 5  
y = 10  

print(x + y)
```

в `print()`функция, когда вы пытаетесь объединить строку и число с `+` оператор, Python выдаст вам ошибку:

```python
x = 5  
y = "John"  

print(x + y)
```

Лучший способ вывести несколько переменных в `print()`функция состоит в том, чтобы разделить их запятыми, которые даже поддерживают разные типы данных:

```python

x = 5  
y = "John"  

print(x, y)
```


## Глобальные переменные

Переменные, созданные вне функции (как во всех примерах выше) называются глобальными переменными.

Глобальные переменные могут использоваться всеми, как внутри функции и снаружи.


Ключевое слово `global` позволяет изменять переменную вне текущей области видимости в Python. `global` используется для создания глобальной переменной и изменения ее в локальной области видимости.

**Что нужно знать прежде, чем работать с global

-   Когда мы создаем переменную внутри функции, она по умолчанию является локальной.

-   Когда мы определяем переменную вне функции, она по умолчанию является глобальной. В этом случае не нужно использовать ключевое слово `global`.

-   Ключевое слово `global` нужно для получения доступа к глобальной переменной и изменения ее внутри функции, то есть внутри локальной области видимости.  

-   Использовать ключевое слово `global` вне функции бессмысленно.

## Как использовать global

#### Пример 1. Получаем доступ к глобальной переменной внутри функции

```python
c = 1 # глобальная переменная

def add():
    print(c)

add()
```

**Вывод:**

```python
1
```

Все работает! Но что если нам нужно изменить глобальную переменную внутри функции?

#### Пример 2. Изменяем глобальную переменную внутри функции

```python
c = 1 # глобальная переменная
    
def add():
    c = c + 2 # прибавляем 2 к c 
    print(c)

add()
```

**Вывод:**

```python
UnboundLocalError: local variable 'c' referenced before assignment
```

Python сообщает нам, что мы использовали локальную переменную `c` до ее объявления. Дело в том, что получить доступ к глобальной переменной внутри функции мы можем, а вот изменять ее в локальной области видимости — уже нет.

Для этого и нужно ключевое слово `global`.

#### Пример 3. Изменяем глобальную переменную внутри функции с помощью global

```python
c = 0 # глобальная переменная

def add():
    global c
    c = c + 2 # прибавляем 2 к c
    print("Внутри функции add():", c)

add()
print("В глобальной области видимости:", c)
```

**Вывод:** 

```python
Внутри функции add(): 2
В глобальной области видимости: 2
```

В приведенной выше программе мы определяем `c` как глобальную переменную внутри функции `add()` с помощью ключевого слова `global`.

Внутри функции мы также увеличиваем переменную `c` на 2, то есть выполняем действие `c = c + 2`. И, наконец, выводим на экран глобальную переменную `c`.

Как мы видим, глобальная переменная `c` изменилась не только внутри функции, но и в глобальной области видимости. И там, и там `c = 2`.


Создайте переменную вне функции и используйте ее внутри функции

```python
x = "awesome"  
  
def myfunc():  
  print("Python is " + x)  
  
myfunc()
```

Результат:

**Python is awesome

Если вы создаете переменную с тем же именем внутри функции, эта переменная будет локальным и может использоваться только внутри функции. Глобальная переменная с тем же именем останется как было, глобальным и с первоначальным значением.

Создайте переменную внутри функции с тем же именем, что и у глобальной переменная

```python
x = "awesome"  
  
def myfunc():  
  x = "fantastic"  
  print("Python is " + x)  
  
myfunc()  
  
print("Python is " + x)
```

Результат:

**Python is fantastic  
Python is awesome

---

---

## Глобальное ключевое слово

Обычно, когда вы создаете переменную внутри функции, эта переменная local и может использоваться только внутри этой функции.

Чтобы создать глобальную переменную внутри функции, вы можете использовать `global` ключевое слово.

Если вы используете `global` ключевое слово, переменная принадлежит глобальной области видимости:

```python
def myfunc():  
  global x  
  x = "fantastic"  
  
myfunc()  
  
print("Python is " + x)
```

Результат:

**Python is fantastic

Кроме того, используйте `global` ключевое слово, если вы хотите изменить глобальную переменную внутри функции.

Чтобы изменить значение глобальной переменной внутри функции, см. переменная с помощью `global` ключевое слово:

```python
x = "awesome"  
  
def myfunc():  
  global x  
  x = "fantastic"  
  
myfunc()  
  
print("Python is " + x)
```

Рузультат:

**Python is fantastic