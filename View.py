from os import system
from msvcrt import getwch
import time


def menu():
    time.sleep(1)
    system('CLS')
    move = {1: 'Создать контакт', 2: 'Прочитать книгу',
            3: 'Изменить контакт', 4: 'Удалить контакт', 5: 'Выход'}
    print('Выберите операцию', move)
    n = getwch() # input()
    if n.isdigit() and n in '12345':
        system('CLS')
        return int(n)
    else:
        system('CLS')
        print('Введите из предложенных вариантов')

def view(book):
    return