import sqlite3


def create_file():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS library(name text primary key, author text, read integer)")

    connection.commit()
    connection.close()


def add_book(title, author):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO library VALUES (?, ?, 0)", (title, author))

    connection.commit()
    connection.close()


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


create_file()