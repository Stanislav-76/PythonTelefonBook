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
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    num_tel = input("Введите телефон: ")
    contact = {"First_name": first_name, "Last_name": last_name,
               "Patronymic": patronymic, "Telefon": num_tel}
    # book = controller.book
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
        lst.append([note['Last_name'], note['First_name'], note["Patronymic"], note["Telefon"]])
    lst.sort()
    for note in lst:
        book_sort.append([note[1], note[0], note[2], note[3]])
    return book_sort