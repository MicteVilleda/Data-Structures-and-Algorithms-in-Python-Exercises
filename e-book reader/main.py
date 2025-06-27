from PyInquirer import prompt
from pathlib import Path
import subprocess


class User:
    def __init__(self, name = 'USER', cash = 500, user_books = dict()):
        self._name = name
        self._cash = cash
        self._books = user_books

    def get_cash(self):
        return self._cash
    
    def get_books(self):
        return list(self._books.values())
    
    def add_books(self, book_and_file_name: tuple):
        book_name = book_and_file_name[0]
        file_name = book_and_file_name[1]
        self._books[book_name] = file_name

    def add_cash(self, ammount):
        self._cash += ammount


class Book:
    def __init__(self, book_name, synopsis):
        self._name = book_name
        self._synopsis = synopsis


def main():
    user = User()

    directory = Path('books')
    books = {file.name.replace('.txt', ''): file.name for file in directory.iterdir()}

    books_for_sale = list(books.values())
    books_for_sale.append('Return')

    user_books = user.get_books()
    user_books.append('Return')

    menus = {
        'Main menu': {
            'type': 'list',
            'name': 'Main menu',
            'message': "Main menu \nPlease select an option",
            'choices': ['Store', 'My books', 'My wallet', 'Close'],
        },
        'Store': {
            'type': 'list',
            'name': 'Main menu',
            'message': "Store:",
            'choices': books_for_sale
        },
        'My books': {
            'type': 'list',
            'name': 'Main menu',
            'message': 'My books',
            'choices': user_books,
        },
        'My wallet': {
            'type': 'list',
            'name': 'Main menu',
            'message': 'My Wallet',
            'choices': ['My cash', 'Add money', 'Return']
        },
        'Close': None,
    }

    current_menu = menus['Main menu']

    while current_menu:
        subprocess.run('cls', shell = True)

        options = prompt(current_menu)

        option_selected = list(options.items())[0]
        last_menu = option_selected[0]
        next = option_selected[1]

        if next in menus:
            current_menu = menus[next]
        elif next == 'Return':
            current_menu = menus[last_menu]
        else:
            print('Do something')
        

    subprocess.run('cls', shell = True)


main()