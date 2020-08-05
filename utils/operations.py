import sqlite3


def create_file():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE library(name text, author text, read integer)")

    connection.commit()
    connection.close()


def open_file():
    with open("utils/library.txt", "r") as file:
        library = json.load(file)
    return library


def write_file(library):
    with open("utils/library.txt", "w") as file:
        json.dump(library, file)


def add_book(title, author):
    library = open_file()
    library.append({"title": title, "author": author, "is_read": False})
    write_file(library)


def delete_book(title):
    library = open_file()
    index = 0
    success = False
    for item in library:
        if item["title"] == title:
            library.pop(index)
            index += 1
            success = True
    write_file(library)
    if success:
        print("Successfully deleted.")
    else:
        print("Title not in library.")


def update_book(title):
    library = open_file()
    success = False
    for item in library:
        if item["title"] == title:
            item["is_read"] = True
            success = True
    write_file(library)
    if success:
        print("Successfully updated.")
    else:
        print("Title not in library.")
