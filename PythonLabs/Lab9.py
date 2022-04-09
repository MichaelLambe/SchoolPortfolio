import sqlite3
import os
import sys
from contextlib import closing

# connect to db
conn = sqlite3.connect(os.path.join(sys.path[0], "task_list_db.sqlite"))
conn.row_factory = sqlite3.Row # return dictionary instead of tuple for rows


def view():
    sql = '''SELECT * FROM Task WHERE completed = 0'''
    with closing(conn.cursor()) as c:
        c.execute(sql)
        conn.commit()
        tasks = c.fetchall()
    for task in tasks:
        print(f"{task['taskID']}. {task['description']} ")
    print()


def history():
    sql = '''SELECT * FROM Task WHERE completed = 1'''
    with closing(conn.cursor()) as c:
        c.execute(sql)
        conn.commit()
        tasks = c.fetchall()
    for task in tasks:
        print(f"{task['taskID']}. {task['description']} (DONE!)")
    print()

def complete(taskid):
    sql = '''UPDATE Task SET description = 1 WHERE taskID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, taskid)
        conn.commit()
        print(f"Task {taskid} has been completed.")
        print()


def add(added:dict):
    sql = '''INSERT INTO Task (taskID, description, completed)
                VALUES (?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (added['taskID'], added['description'], 
                        added['completed']))
        conn.commit()
        print(f"{added['description']} was added.")
    
        

def delete(taskID):
    sql = '''DELETE FROM Task WHERE taskID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (taskID))
        conn.commit()
        print(f" Task with the id {taskID} was deleted")
        print()


def main():
    print("Task List")
    print()
    print("COMMAND MENU")
    print("view     - view pending tasks")
    print("history  - view completed tasks")
    print("add      - Add a task")
    print("complete - Complete a task")
    print("delete   - Delete a task")
    print("exit     - Exit program")
    while True:
        choice = input("Command: ")
        if choice == "view":
            view()
            print()
        elif choice == "history":
            history()
            print()
        elif choice == "add":
            desc = input("Description: ")
            add(desc)
        elif choice == "complete":
            num = input("Number: ")
            complete(num)
        elif choice == "delete":
            id = input("Task Number: ")
            delete(id)
        elif choice == "exit":
            print("Bye!")
            quit()
        else:
            print("Invalid input. Please try again.")

if __name__ == '__main__':
    main()


