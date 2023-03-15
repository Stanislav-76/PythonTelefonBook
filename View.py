from os import system
from msvcrt import getwch
import time


def menu():
    time.sleep(1)
    system('clear') # system('cmd /c cls')
    move = {1: 'Создать контакт', 2: 'Прочитать книгу',
            3: 'Изменить контакт', 4: 'Удалить контакт', 5: 'Выход'}
    print('Выберите операцию', move)
    n = getwch()  # input()
    if n.isdigit() and n in '12345':
        system('CLS')
        return int(n)
    else:
        system('CLS')
        print('Введите из предложенных вариантов')


def view(book):
    print('Список контактов телефонного справочника:\n')
    table = [['ФАМИЛИЯ', 'ИМЯ', 'ОТЧЕСТВО', 'НОМЕР ТЕЛЕФОНА']]
    for contact in book:
        contact = list(contact.values())
        table.append(contact)
    for ind, item in enumerate(table):
        if ind == 0:
            ind = '№'
        print(ind, '\t', *map(lambda x: str(x) + ' ' * (20 - len(x)), item))
    time.sleep(30)
