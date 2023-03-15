import json
import controller


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
    book.append(contact)
    print('\nКонтакт создан')
    book = sort(book)
    save(book)


def update_contact(book):
    return


def del_contact(book):
    return


def sort(book):
    lst = []
    book_sort = []
    for note in book:
        lst.append([note['Last_name'], note['First_name'],
                   note["Patronymic"], note["Telefon"]])
    lst.sort()
    for note in lst:
        book_sort.append({"Last_name": note[0], "First_name": note[1], "Patronymic": note[2], "Telefon": note[3]})
    return book_sort