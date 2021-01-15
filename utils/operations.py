from .database_connection import DatabaseConnection


def create_file():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS library(title text primary key, author text, read integer)")


def view_all():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT title, author, read FROM library")
        library = [{'title': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    return library


def add_book(title, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("INSERT INTO library VALUES (?, ?, 0)", (title, author))


def delete_book(title):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT title, author FROM library WHERE title = ?", (title,))
        book = cursor.fetchone()
        if book:
            cursor.execute("DELETE FROM library WHERE title = ?", (title,))
            return print("Successfully deleted.")
    return print("Item not in library.")


def update_book(title):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT title, author FROM library WHERE title = ?", (title,))
        book = cursor.fetchone()
        if book:
            cursor.execute("UPDATE library SET read = 1 WHERE title = ?", (title,))
            return print("Successfully updated.")
        return print("Item not in library.")


create_file()
