import utils.operations as operations

welcome = '''
    Welcome to your library!
'''

menu = '''
    Would you like to:
-View your library (view)
-Add a book to your library (add)
-Delete a book from your library (delete)
-Mark a book as read (update)
-Exit (exit)

'''

goodbye = '''
    Thank you for using our service.
'''


def initiate():
    print(welcome)
    selection = input(menu)
    switchboard[selection]()


def view():
    library = operations.open_file()
    print(library)
    repeat()


def add():
    title = input("What title would you like to add? ")
    author = input(f"Who wrote {title}? ")
    confirm = input(f"{title} by {author} will be added to your library.  Is this ok? (y/n) ")
    if confirm == "y":
        operations.add_book(title, author)
        print("Added to library!")
    repeat()


def update():
    repeat()


def delete():
    repeat()


def repeat():
    selection = input(menu)
    switchboard[selection]()


def leave():
    print(goodbye)


switchboard = {
    "view": view,
    "add": add,
    "delete": delete,
    "update": update,
    "exit": leave
}

initiate()
