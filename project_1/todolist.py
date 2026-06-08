#! /usr/bin/python
#
# This script is written and tested on Archlinux

import sqlite3
import os


def clear_screen():
    os.system("clear")

    print("TODOLIST APP\n\n")


# this only works if no file exists
def check_db_exist():
    if os.path.exists("todolist.db"):
        return

    try:
        sqlite_connection = sqlite3.connect("todolist.db")
        cursor = sqlite_connection.cursor()
        cursor.execute("""
            CREATE TABLE todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item TEXT NOT NULL
            )
        """)
        sqlite_connection.commit()
    except Exception as e:
        print(e)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def connect_to_db():
    try:
        sqlite_connection = sqlite3.connect("todolist.db")
        cursor = sqlite_connection.cursor()
        return sqlite_connection, cursor
    except Exception as e:
        print(e)
        return None, None


def fetch_todolist():
    try:
        sqlite_connection, cursor = connect_to_db()
        cursor.execute("SELECT * FROM todos")
        items = cursor.fetchall()
        return items
    except Exception as e:
        print(e)
        return None
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def view_todolist():
    clear_screen()
    todo_items = fetch_todolist()
    print("# | Description")

    if todo_items:
        for item in todo_items:
            print(f"{item[0]} | {item[1]}")
    else:
        print("No todo items found")

    print("\n\n")


def add_todo_item(item):
    try:
        sqlite_connection, cursor = connect_to_db()
        cursor.execute("INSERT INTO todos (item) VALUES (?)", (item,))
        sqlite_connection.commit()
    except Exception as e:
        print(e)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def delete_item(item):
    print(f"Deleting Item {item}...")


def edit_item(item):
    print(f"Editing Item {item}...")


def main():
    check_db_exist()
    # clear_screen()

    while 1:
        view_todolist()

        print("1. Add Task")
        print("2. Delete Task (coming soon)")
        print("3. Edit Task (coming soon)")
        print("4. Exit/Quit")

        option = input("Enter Option: ")

        try:
            if int(option) == 1:
                item = input("Enter Item: ")
                print(item)
                add_todo_item(item)
                continue
            elif int(option) == 2:
                item = input("Enter Item to Delete: ")
                delete_item(item)
                continue
            elif int(option) == 3:
                edit_item()
                continue
            elif int(option) == 4:
                break
            else:
                print("Option Not Found")
                continue
        except ValueError:
            print("Option Not Found")
            continue


if __name__ == "__main__":
    main()
