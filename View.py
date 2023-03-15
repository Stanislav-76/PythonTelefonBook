from os import system
from msvcrt import getwch
import time
import pandas as pd


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
    # df = pd.DataFrame()
    table = [['Фамилия', 'Имя', 'Отчество', 'Номер телефона']]
    d = dict.fromkeys(['Last_name', 'First_name', 'Patronymic', 'Telefon'])
    print(d)
    for contact in book:
        d = d.update(contact)
    print(d)
    # for contact in book:
    #     contact = list(contact.values())
    #     table.append(contact)
    # for ind, item in enumerate(table):
    #     print(ind, *map(str, item))