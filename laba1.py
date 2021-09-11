import matplotlib.pyplot as pyplot
import control.matlab as matlab
import numpy as numpy
import math


def choise():
    inertialessUnitName = 'Безынерционое звено'
    aperiodicUnitName = 'Апериодическое звено'

    needNewChoise = True

    while needNewChoise:
        userInput = input('Введите номер команды: \n'+
                          '1- ' + inertialessUnitName+ '\n '+
                          '2- ' + aperiodicUnitName+ '\n' )
        if userInput.isdigit():
            needNewChoise = False
            userInput = int(userInput)
            if userInput == 1:
                name = 'Безынерционое звено'
            elif userInput == 2:
                name = 'Апериодическое звено'
            else:
                print('Недопустимое значение')
                needNewChoise = True

        else:
            print('\n Пожалуста введите числовое значение!\n')
            needNewChoise = True
    return name

def getUnit(name):
    k = input('пожалуймта введите k :')
    t = input('пожалуймта введите t :')

    if k.isdigit() and t.isdigit():
        k = int(k)
        t = int(t)
        if name == 'Безынерционное звено':
            unit = matlab.tf([k],[1])
        elif name == 'Апериодическое звено':
            unit = matlab.tf([k],[t, 1])
    else:
        print('\n Пожалуста введите числовое значение!\n')
        needNewChoise = True
    return unit

def graph(num, title, y, x):
    pyplot.subplot(2,1, num)
    pyplot.grid(True)
    if title == 'Переходная характеристика':
        pyplot.plot(x, y, 'purple')
    elif title == 'Импульсная характеристика':
        pyplot.plot(x, y, 'green')
    pyplot.title(title)
    pyplot.ylabel('Амплитуда')
    pyplot.xlabel('Время, c')



unitName = choise()
unit = getUnit(unitName)

timeLine = []
for i in range(0, 10000):
    timeLine.append(i/1000)

[y, x] = matlab.step(unit, timeLine)
graph(1, 'Переходная характеристика', y, x)
[y, x] = matlab.impulse(unit, timeLine)
graph(2, 'Импульсная характеристика', y, x)
pyplot.show()