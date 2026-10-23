'''
The task is to create a to-do list application

Specification:
You should design an appropriate data structure for the to-do list.
You should use functions where appropriate.
You should create an appropriate programming structure to "drive" the application.

Good programming practice:
Functions should have one purpose (single responsibility principle).
Meaningful names for variables and functions.
Document your functions.
'''

# ---------------------------------------------------------------------------
# Design notes
#
# Data structure: a list of dictionaries, e.g.
#     [{"description": "buy milk", "done": False},
#      {"description": "finish week 5", "done": True}]
# The list keeps the tasks in the order they were added, each dictionary gives
# the task a readable name for its fields, and the boolean makes it easy to
# mark a task complete without adding or removing anything.
#
# Storage: the list is saved to todo_list.json (JSON handles lists,
# dictionaries and booleans directly) so tasks survive between runs.
#
# Structure: each function does one job, and main() is the driver - it holds
# the loop and calls the other functions based on the user's choice.
# ---------------------------------------------------------------------------
import os
import sys
import time
import datetime
import json

FILENAME = "todo_list.json"


def load_tasks():
    """Read the task list from the file, or return an empty list on first run."""
    pass


def save_tasks(tasks):
    """Write the current task list to the file."""
    pass


def add_task(tasks):
    """Ask for a description and append a new, unfinished task to the list."""

    new_description = input("Please enter a new task:").strip()

    if new_description == "":
        print("The task cannot be empty.The addition failed.")
        return
    
    new_task = {"description": new_description, "done": False}
    tasks.append(new_task)              #这个list叫什么
    print("The task was added successfully.")


def view_tasks(tasks):
    """Print every task with a number and a completion marker."""
    pass


def complete_task(tasks):
    """Ask for a task number and mark that task as done."""
    if not tasks:
        print("No tasks to mark as done.")
        return False

    raw = input("Enter the number of the task to mark as done: ").strip()
    try:
        number = int(raw)
    except ValueError:
        print("Please enter a valid task number.")
        return False

    index = number - 1
    if index < 0 or index >= len(tasks):
        print(f"No task number {number}. Choose between 1 and {len(tasks)}.")
        return False

    tasks[index]["done"] = True
    print(f"Task {number} marked as done: {tasks[index]['description']}")
    return True


def delete_task(tasks):
    """Ask for a task number and remove that task from the list."""
    pass


def show_progress(tasks):
    """Report how many tasks are finished."""
    pass


def main():
    """Drive the application: load the tasks, then run the menu loop."""
    """=== To-Do List ===
    1. View tasks
    2. Add a task
    3. Mark a task as done
    4. Delete a task
    5. Show progress
    6. Quit
    Choose an option (1-6):"""
    tasks=load_tasks()
    print(f"Loaded{len(tasks)} task(s) from {FILENAME}.")
    while True:
        print("\n=== To-Do List ===")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark a task as done")
        print("4. Delete a task")
        print("5. Show progress")
        print("6. Quit")
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == '5':
            show_progress(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print(f"Saved {len(tasks)} task(s) to {FILENAME}. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
if __name__ == "__main__":
    main()