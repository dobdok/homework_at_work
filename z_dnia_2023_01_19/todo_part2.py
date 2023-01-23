
"""Main File to Run the programe"""
import sys
from todo_part1 import ToDoList


class Menu:
    """Display a menu and respond to choices when
    run """

    def __init__(self):
        self.toDoList = ToDoList()
        self.choices = {
            "1": self.show_tasks,
            "2": self.search_tasks,
            "3": self.add_tasks,
            "4": self.delete_tasks,
            "5": self.quit,
        }

    def display_menu(self):
        print(
            """
            To Do List menu
            ===============

            1. Show all Tasks 
            2. Search Tasks
            3. Add Tasks
            4. Delete Tasks
            5. Quit

            """

        )

    def run(self):
        """Display the menu and repond to the choices"""
        while True:
            self.display_menu()
            choice = input("Enter an option")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_tasks(self, tasks=None):
        if not tasks:
            tasks = self.toDoList.tasks
        for task in tasks:
            print("{0}: {1}".format(task.id, task))

    def search_tasks(self):
        filter = input("Search tasks:")
        tasks = self.toDoList.search(filter)
        self.show_tasks(tasks)

    def add_tasks(self):
        task_name = input("Enter a task:")
        self.toDoList.new_task(task_name, complete="Y")
        print("Your task has been added:")

    def delete_tasks(self):
        id = input("Enter a task id:")
        task = input("Enter task name:")
        if task:
            self.toDoList.delete_task(id, task)

    def quit(self):
        print("Thank you for using To-Do-List today")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()

