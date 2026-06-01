#! /usr/bin/python
#
# This script is written and tested on Archlinux

import sqlite3
import os


def clear_sreen():
    print('clear')

# this only works if no file exists
def check_db_exist():
    if os.path.exists('todolist.db'):
        return
    try:
        sqlite_connection = sqlite3.connect('todolist.db')
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
        sqlite_connection = sqlite3.connect('todolist.db')
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
    todo_items = fetch_todolist()
    print("# | ITEM")
    print(f"{todo_items[0][0]} | {todo_items[0][1]}")

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
    while 1:
        print("TODOLIST APP\n\n")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Edit Task")
        print("5. Exit/Quit")

        option = input("Enter Option: ")

        try:
            if int(option) == 1:
                view_todolist()
                continue
            elif int(option) == 2:
                item = input("Enter Item: ")
                add_todo_item(item)
                continue
            elif int(option) == 3:
                view_todolist()
                item = input("Enter Item to Delete: ")
                delete_item(item)
                continue
            elif int(option) == 4:
                edit_item()
                continue
            elif int(option) == 5:
                break
            else:
                print("Option Not Found")
                continue
        except ValueError:
            print("Option Not Found")
            continue


if __name__ == '__main__':
    main()
