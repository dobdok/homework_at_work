from datetime import datetime


"""To Do List Programe"""
"""Represent a Tasks in the To-DoList. 
match against a string in searches and store each
tasks"""
last_id = 0


class Task:
    def __init__(self, task_name, complete=str):
        self.task_name = task_name
        self.complete = "Y"
        self.date_created = datetime.today().strftime('%d-%m-%y')
        global last_id
        last_id += 1
        self.id = last_id

    def match_task(self, filter):
        """Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is not case sensitive and matches any word in the tasks. """

        return filter.lower() in self.task_name.lower()


class ToDoList:
    """Represent a collection of tasks that
    can be searched, modified and complete and deleted """

    def __int__(self):
        self.tasks = []

    def new_task(self, task_name, complete):
        """Create new task and add it to the list"""
        self.tasks.append(Task(task_name, complete))

    def _find_task(self, task_id):
        """locate the task with given id"""
        for task_name in self.tasks:
            if str(task_name.id) == str(task_name.id):
                return task_name
        return None

    def modify_task(self, task_id, task_name):
        task_name = self._find_task(task_id)
        if task_name:
            task_name.task_name = task_name
            return True
        return False

    def delete_task(self, task_id, complete):
        task = self._find_task(task_id)
        if task:
            task.complete = "Y"
            return self.tasks.remove(task_id-1)
        return False

    def search(self, filter):
        """Find all task that match the given
        fliter string """
        return [task for task in self.tasks if task.match(filter)]
