import Model
import View



def start():    
    book = Model.read()
    while True:        
        n = View.menu()
        if n == 1:
            Model.create_contact(book)
        if n == 2:
            View.view(book)
        if n == 3:
            Model.update_contact(book)
        if n == 4:
            Model.del_contact(book)
        if n == 5:
            break        