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
    # book = controller.book
    book.append(contact)
    print('\nКонтакт создан')
    save(book)


def update_contact(book):
    return


def del_contact(book):
    return

# def sort(book):
