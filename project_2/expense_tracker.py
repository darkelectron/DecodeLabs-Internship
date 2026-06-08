#! /usr/bin/python
#
# This script is written and tested on Archlinux

import sqlite3
import os


def clear_screen():
    os.system("clear")

    print("EXPENSE TRACKING APP\n\n")


def check_db_exist():
    if os.path.exists("expenses.db"):
        return

    try:
        sqlite_connection = sqlite3.connect("expenses.db")
        cursor = sqlite_connection.cursor()
        cursor.execute("""
            CREATE TABLE sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cursor.execute("""
            CREATE TABLE expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id INTEGER NOT NULL,
                item TEXT NOT NULL,
                amount REAL NOT NULL DEFAULT 0,
                FOREIGN KEY (session_id) REFERENCES sessions(id)
            )
        """)
        sqlite_connection.commit()
        sqlite_connection.close()
    except Exception as e:
        print(e)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def connect_to_db():
    try:
        sqlite_connection = sqlite3.connect("expenses.db")
        cursor = sqlite_connection.cursor()
        return sqlite_connection, cursor
    except Exception as e:
        print(e)
        return None, None


def fetch_expenses():
    try:
        sqlite_connection, cursor = connect_to_db()
        cursor.execute("""
            SELECT s.id, s.created_at,
                   COALESCE(SUM(e.amount), 0),
                   COUNT(e.id)
            FROM sessions s
            LEFT JOIN expenses e ON e.session_id = s.id
            GROUP BY s.id
            ORDER BY s.id DESC
        """)
        sessions = cursor.fetchall()
        return sessions
    except Exception as e:
        print(e)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def create_session():
    try:
        sqlite_connection, cursor = connect_to_db()
        cursor.execute("INSERT INTO sessions DEFAULT VALUES")
        session_id = cursor.lastrowid
        sqlite_connection.commit()
        sqlite_connection.close()
        return session_id
    except Exception as e:
        print(e)


def view_previous_expenses():
    clear_screen()
    sessions = fetch_expenses()

    if not sessions:
        print("No sessions found.")
    else:
        for id, created_at, total, count in sessions:
            print(f"Session {id}  ({created_at[:19]})  {count} items  {total:.2f}")
    print("\n\n")


def accumulate_expenses():
    # TODO: use try-except-finally for sqlite
    session_id = create_session()
    sqlite_connection, cursor = connect_to_db()

    print("Enter expenses one by one (press Enter with no value to stop): \n\n")

    while True:
        value = input("Enter Expense: ")

        if value == "":
            break
        try:
            amount = float(value)
            cursor.execute(
                "INSERT INTO expenses (session_id, item, amount) VALUES (?, ?, ?)",
                (session_id, "Expense", amount),
            )
        except ValueError:
            print("Invalid Data")
            continue

    sqlite_connection.commit()
    sqlite_connection.close()


def main():
    check_db_exist()

    while 1:
        view_previous_expenses()

        print("1. Add Expenses")
        print("2. Edit Expenses (coming soon)")
        print("3. Exit")

        print("\n\n")

        try:
            option = int(input("Enter Option: "))
        except ValueError:
            print("Option Not Found")
            continue

        if option == 1:
            accumulate_expenses()
        elif option == 2:
            continue
        elif option == 3:
            break
        else:
            print("Option Not Found")
            continue


if __name__ == "__main__":
    main()
