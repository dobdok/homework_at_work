"""
do napisania program przypominający działaniem listę TODO
aplikacja do przechowywania zadań wraz ze stanami - TODO, IN PROGRESS, DONE
aplikacja powinna
wyświetlać aktualne zadania - można użyć zewnętrznej biblioteki do "rysowania" tabeli
dać możliwość dodawania nowych zadań
dać możliwość edytowania aktualnych zadań
dać możliwość usuwania istniejących zadań
zapisywanie stanu do pliku przy kończeniu pracy
pobieranie stanu z pliku przy uruchomieniu aplikacji
dodać menu mówiące użytkownikowi w jakim miejscu się znajduje / co wykonuje
budowa aplikacji powinna być przemyślana, aplikacja powinna być rozbita na kilka mniejszych modułów / pakietów
wykorzystać poznane elementy języka Python
wykorzystać klasy do modelowania danych
"""

import json
from tabulate import tabulate


class Ticket:

    def __init__(self, status, description, id):
        self.status = status
        self.description = description
        self.id = id

    def __repr__(self):
        return f"id: {self.id} \n{self.description}"

    def edit_desc(self, changed_desc):
        self.description = changed_desc

    def edit_status(self, changed_status):
        self.status = changed_status

    def to_json(self):
        json_dic = {
            "Status": self.status,
            "Description": self.description,
            "ID": self.id
            }
        return json_dic

    @classmethod
    def from_json(cls, json_dict):
        ticket = cls(
            status=json_dict['Status'],
            description=json_dict['Description'],
            id=json_dict['ID'])
        return ticket


def save_to_json():
    todolist_dict = {
        "TODO": [],
        "IN PROGRESS": [],
        "DONE": []
        }
    for elem_dict in TODO_list_data:
        for elem_list in TODO_list_data[elem_dict]:
            todolist_dict[elem_dict].append(elem_list.to_json())

    into_file = json.dumps(todolist_dict, indent=4)
    with open("TODO_List_app.json", "w") as f:
        f.write(into_file)


def read_file():
    TODO_list_data = {
        "TODO": [],
        "IN PROGRESS": [],
        "DONE": []
        }

    try:
        with open("TODO_List_app.json", "r") as f:
            from_file = json.load(f)

        for elem in from_file:
            for subelem in from_file[elem]:
                TODO_list_data[elem].append(Ticket.from_json(subelem))

    except FileNotFoundError:
        print("There is no file with the following name. Check the name of the file.")
    return TODO_list_data


def menu_glowne():
    commands = ["a", "e", "d", "q"]
    print(
        """
What action do you want to take?
[A]dd new task
[E]dit
[D]elete
[Q]uit
    """
        )
    choice1 = input("Choose action: ").lower()
    if choice1 not in commands:
        print("Wrong input. What do you wish to do?")
        return None

    if choice1 == "a":
        print("Adding new task")
        columns_manage()
        new_ticket()

    elif choice1 == "e":
        print("Editing task")
        edit()

    elif choice1 == "d":
        print("Deleting task")
        delete()

    else:
        return choice1


def columns_manage():
    global choice2
    columns = ["1", "2", "3"]
    print(
        """Changes should be done in the column:
    1 - TODO
    2 - IN PROGRESS
    3 - DONE"""
        )
    choice2 = input("Column nr: ")
    if choice2 not in columns:
        print("Wrong input! Please try again!")
        return columns_manage()

    if choice2 == "1":
        choice2 = "TODO"
        print(choice2)
    elif choice2 == "2":
        choice2 = "IN PROGRESS"
        print(choice2)
    elif choice2 == "3":
        choice2 = "DONE"
        print(choice2)
    return choice2


def new_ticket():
    max_id = max_ID()
    max_id += 1
    task_description = input("Input your task description: ")

    ticket = Ticket(status=choice2, description=task_description, id=max_id)
    if choice2 == "TODO":
        key = "TODO"
        TODO_list_data.setdefault(key)
        TODO_list_data[key].append(ticket)

    elif choice2 == "IN PROGRESS":
        key = "IN PROGRESS"
        TODO_list_data.setdefault(key)
        TODO_list_data[key].append(ticket)

    elif choice2 == "DONE":
        key = "DONE"
        TODO_list_data.setdefault(key)
        TODO_list_data[key].append(ticket)


def search(id):
    for elem in TODO_list_data:
        for subelem in TODO_list_data[elem]:
            if subelem.id == int(id):
                return elem, subelem

def delete():
    which_id = input("Type id of the ticket to be deleted: ")
    id = search(which_id)
    if id == None:
        print("id out of range, task does not exist. ")
    else:
        search_id = TODO_list_data[id[0]].index(id[1])
        del TODO_list_data[id[0]][search_id]


def edit():
    while True:
        edit_task = input("Type the id nr of the ticket, or type q to quit application. ").lower()
        if edit_task == "q":
            return
        try:
            where, task = search(edit_task)
            break
        except:
            print("Task with following id does not exist.")

    print(
        f"""You are currently editing the ticket: 
    id: {task.id}
    Description: {task.description}""")

    column_change = input(f"""
    1 - TODO
    2 - IN PROGRESS
    3 - DONE
To which column do you want to move the task? If no changes in column, press enter.""")
    if column_change == "":
        pass
    if column_change == "1":
        print("Task moved to TODO column.")
        task.edit_status("TODO")
        move = TODO_list_data[where].index(task)
        TODO_list_data["TODO"].append(task)
        del TODO_list_data[where][move]

    elif column_change == "2":
        print("Task moved to IN PROGRESS column.")
        task.edit_status("IN PROGRESS")
        move = TODO_list_data[where].index(task)
        TODO_list_data["IN PROGRESS"].append(task)
        del TODO_list_data[where][move]

    elif column_change == "3":
        print("Task moved to DONE column.")
        task.edit_status("DONE")
        move = TODO_list_data[where].index(task)
        TODO_list_data["DONE"].append(task)
        del TODO_list_data[where][move]

    change_description = input("New task description, if no changes in description, press enter:")
    if change_description == "":
        pass
    if change_description != "":
        task.edit_desc(change_description)


def max_ID():
    max_id = 0
    for elem in TODO_list_data:
        for subelem in TODO_list_data[elem]:
            if subelem.id > max_id:
                max_id = subelem.id
    return max_id


result = ""
TODO_list_data = read_file()
while result != "q":
    print(tabulate(TODO_list_data, headers="keys", tablefmt="rounded_grid"))
    result = menu_glowne()


save_to_json()
