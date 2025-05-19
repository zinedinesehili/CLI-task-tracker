from dataclasses import dataclass
import json


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

def main():
    id = 1;
    tasks = {}

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