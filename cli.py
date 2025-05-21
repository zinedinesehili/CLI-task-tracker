"""
Author: Zinedine Sehili
Filename: cli.py

Purpose:

"""

from dataclasses import dataclass
import json

#list with all tasks
#TODO import tasks from a json so it doesn't restart every time it runs
tasks = []

def help():
    """
    prints all commands
    """
    print("Commands:")
    print("\tadd [TASK_DESCRIPTION]                 adds a task")
    print("\tupdate [TASK_ID] [NEW_DESCRIPTION]     updates a tasks description")
    print("\tdelete [TASK_ID]                       deletes a task")
    print("\tmark-in-progress [TASK_ID]             marks task in progress")
    print("\tmark-done [TASK_ID]                    marks task done")
    print("\tlist                                   lists all tasks")
    print("\tlist [done/todo/in-progress]           lists tasks by status")

def add(description):
    """
    creates a task (a dictionary)

    dictionary items:
    - id
    - description
    - status
    """

    task = {}
    task["id"] = len(tasks) + 1
    task["description"] = description
    task["status"] = "todo"

def main():
    id = 1;

    print("Task Tracker: type help for commands")
    action = input()    #action is whatever the user wants to do
    while action != "":
        if action == "help":
            help()
        elif action == "add":
            #TODO
            print()

if __name__ == "__main__":
    main()