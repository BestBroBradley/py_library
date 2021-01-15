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
    selection = input(menu).lower()
    switchboard[selection]()


def view():
    library = operations.view_all()
    if library:
        for book in library:
            if book["read"]:
                book["read"] = "yes"
            else:
                book["read"] = "no"
            print(f"Title: {book['title']} | Author: {book['author']} | Read? {book['read']}")
    else:
        print("No titles in library.")
    repeat()


def add():
    title = input("What title would you like to add? ").title()
    author = input(f"Who wrote {title}? ").title()
    confirm = input(f"{title} by {author} will be added to your library.  Is this ok? (y/n) ")
    if confirm.lower() == "y":
        result = operations.add_book(title, author)
        if result:
            print("Added to library!")
        else:
            print("Item already in library.")
    repeat()


def update():
    title = input("Which title would you like to mark as 'read'? ").title()
    confirm = input(f"You will be updating {title}.  Is this ok? (y/n) ")
    if confirm.lower() == "y":
        operations.update_book(title)
    repeat()


def delete():
    title = input("Which title would you like to delete? ").title()
    confirm = input(f"You will be deleting {title}. Is this ok? (y/n) ")
    if confirm == "y":
        operations.delete_book(title)
    repeat()


def repeat():
    selection = input(menu).lower()
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
