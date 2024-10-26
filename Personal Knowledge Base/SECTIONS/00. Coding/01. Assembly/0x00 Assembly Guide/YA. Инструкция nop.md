Команда NOP в Ассемблере ничего не делает. Синтаксис:

>NOP

Состояние флагов не изменяется.

NOP - это однобайтовая команда, которая ничего не выполняет, а только занимает место и время.

# Зачем нужна команда NOP

Возникает закономерный вопрос - для чего нужна команда NOP, которая ничего не делает, а только занимает место в программе и
отнимает время у процессора? И, тем не менее, такая команда есть практически во всех ассемблерах, включая ассемблеры для микроконтроллеров. 

Эта команда, в основном, используется для выполнения небольшой задержки в программе. Если говорить о микроконтроллерах, то такая задержка может потребоваться, например, для подавления “дребезга контактов”.


# Как рассчитать время задержки командой NOP

Но что делать, если нужно выполнить задержку не абы как, а на определённое время? Как узнать, на какое время команда
NOP задержит выполнение программы? Приблизительно это можно рассчитать. Для этого потребуется знать два параметра:

 - Тактовую частоту процессора.
 - Количество тактов, которое требуется на выполнение команды NOP.

Тактовая частота процессора известна из его характеристик. Тактовая частота микроконтроллера также известна из его
характеристик, но ещё зависит от частоты времязадающей цепи в обвязке микроконтроллера. Количество тактов, которое занимает выполнение команды NOP, зависит от процессора (микроконтроллера) и берётся из документации на процессор.

Для примера и для упрощения представим, что команда NOP выполняется за 2 такта, а тактовая частота процессора 1 МГц.
Что такое Герц (Гц)? Это количество колебаний в секунду (курсы по электротехнике и электронике ищи здесь). 1 МГц = 1000000 Гц
То есть каждую секунду в процессоре выполняется миллион тактов (в нашем примере). Если в нашем примере команда NOP
выполняется за 2 такта, то получается, что за одну секунду процессор может выполнить таких команд:

  1000000 / 2 = 500000

Следовательно, одна такая команда будет выполнена за:

  1 / 500000 секунды = 0,002 мс = 2 мкс

То есть одна инструкция NOP в нашем примере задержит выполнение программы на 2 микросекунды. Если же нам
потребуется задержать программу, например, на 10 мкс, то нам надо будет вызвать команду NOP пять раз подряд:

>
NOP
NOP
NOP
NOP
NOP

При желании можно вызвать инструкции NOP в цикле, но тогда ещё придётся учитывать время на выполнение команды цикла. А теперь о происхождении мнемоники NOP. Всё, как всегда, просто. Это сокращение словосочетания “Nо OPeration“, что, как вы понимаете, переводится с английского как “нет операции” или “никакая операция”. То есть это отсутствие операции, программа ничего не
делает.

