В программировании тип данных является важной концепцией.

Переменные могут хранить данные разных типов, и разные типы могут выполнять разные вещи.

В Python по умолчанию встроены следующие типы данных в следующих категориях:

Тип текста:   `str`

Числовые типы:  `int`, `float`, `complex`

Типы последовательностей:  `list`, `tuple`, `range`

Тип отображения:  `dict`

Типы наборов:      `set`, `frozenset`

Логический тип:   `bool`

Бинарные типы:  `bytes`, `bytearray`, `memoryview`

Тип:   `NoneType`

---

## Получение типа данных

Вы можете получить тип данных любого объекта, используя `type()`функция:

### Пример

Выведите тип данных переменной x:


```python
x = 5  
print(type(x))
```

**Результат:

<class 'int'>

---

## Установка типа данных

В Python тип данных устанавливается, когда вы присваиваете значение переменной:

| Example                                      | Data Type  |
|:-------------------------------------------- |:---------- |
| x = "Hello World"                            | str        |
| x = 20                                       | int        |
| x = 20.5                                     | float      |
| x = 1j                                       | complex    |
| x = ["apple", "banana", "cherry"]            | list       |
| x = ("apple", "banana", "cherry")            | tuple      |
| x = range(6)                                 | range      |
| x = {"name" : "John", "age" : 36}            | dict       |
| x = {"apple", "banana", "cherry"}            | set        |
| x = frozenset({"apple", "banana", "cherry"}) | frozenset  |
| x = True                                     | bool       |
| x = b"Hello"                                 | bytes      |
| x = bytearray(5)                             | bytearray  |
| x = memoryview(bytes(5))                     | memoryview |
| x = None                                     | NoneType   |

```python
num = 5     #int
fnum = 5.6  #float
name = “Alex” #string
status = False #bool
```

1) Если значание переменной целое число, то это переменная типа int (interger).
2) Если значение переменной чило с точкой, то это переменная типа float.
3) Если значение переменной в кавычках, то это переменная типа stringб то есть строка.
4) Тип данных bool, может принимать только два значаения – это True и False.

Типы переменных в языке Python не объявляются очевидно, тем не менее они присутствуют. Интерпретатор понимает что записывается в
переменную и на основании этого добавляет тип к этой переменной.