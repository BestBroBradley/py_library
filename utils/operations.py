import json


def open_file():
    with open("utils/library.txt", "r") as file:
        library = json.load(file)
    return library


def write_file(library):
    with open("utils/library.txt", "w") as file:
        json.dump(library, file)


def add_book(title, author):
    library = open_file()
    print(library)
    library.append({"title": title, "author": author, "is_read": False})
    write_file(library)


def delete_book(title):
    pass


def update_book(title):
    pass

