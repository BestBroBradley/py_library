import sqlite3


def create_file():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS library(title text primary key, author text, read integer)")

    connection.commit()
    connection.close()


def view_all():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("SELECT title, author FROM library")
    library = [{'title': row[0], 'author': row[1]} for row in cursor.fetchall()]

    connection.close()
    return library


def add_book(title, author):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO library VALUES (?, ?, 0)", (title, author))

    connection.commit()
    connection.close()


def delete_book(title):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute(f"SELECT title, author FROM library WHERE title = '{title}'")
    book = cursor.fetchone()
    if book:
        cursor.execute(f"DELETE FROM library WHERE title = '{title}'")

        connection.commit()
        connection.close()
        return print("Successfully deleted.")
    connection.close()
    return print("Item not in library.")


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