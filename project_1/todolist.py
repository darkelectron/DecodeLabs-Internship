#! /usr/bin/python

def fetch_todolist():
    print("fetching to-do list")


def view_todolist():
    print("TODO LIST")


def add_todo_item(item):
    print("Enter Item: ")


def delete_item(item):
    print(f"Deleting Item {item}...")


def edit_item(item):
    print(f"Editing Item {item}...")


def main():
    while 1:
        print("TODOLIST\n\n")
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
