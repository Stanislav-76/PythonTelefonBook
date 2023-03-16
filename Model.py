import json
import controller
import View
from os import system

def read():
    try:
        with open('phoneBook.json', 'r', encoding="utf-8") as data:
            book = json.loads(data.read())
        return book
    except:
        return []

def save(book):
    with open('phoneBook.json', 'w', encoding="utf-8") as data:
        json.dump(book, data, indent=4, ensure_ascii=False)

def create_contact(book):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    num_tel = input("Введите телефон: ")
    contact = {"Last_name": last_name, "First_name": first_name, 
               "Patronymic": patronymic, "Telefon": num_tel}
    # book = controller.book
    book.append(contact)
    print('\nКонтакт создан')
    save(book)

def update_contact(book):
    View.view(book)
    contact_change = input("Введите номер контакта для обновления: ")
    if contact_change.isdigit() and int(contact_change) <= len(book):
        system("CLS")
        contact_change = int(contact_change)
    else:
        system("CLS")
        print("В книге нет такого контакта")
    
    # print(book[contact_change])
   
    new_number = input(f"Введите новый номер телефона пользователя {contact_change}: ")
    book[contact_change-1]["Telefon"] = new_number
    # print(book[contact_change])
    print(f"\nКонтакт {contact_change} изменен")
    save(book)

# def update_contact(book):
#     return
#     View.view(book)
#     change_contact = int(input('Какой номер контакта изменить?: '))
#     book.pop(change_contact - 1)
#     new_num = int(input('Введите новый номер: '))
#     book.insert((change_contact(3, new_num))
#     print('\nКонтакт изменен')
#     save(book) 

# def del_contact(book):
#     return

# def sort(book):
