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
    dodać menu mówiące użytkownikowi w jakim miejscu się znajduje/ co wykonuje
    budowa aplikacji powinna być przemyślana, aplikacja powinna być rozbita na kilka mniejszych modułów / pakietów
        wykorzystać poznane elementy języka Python
        wykorzystać klasy do modelowania danych
"""

import json
import os

from tabulate import tabulate


class Task:
    __count = 0

    def __init__(self, description, status):
        self.description = description
        self.status = status
        self.id = Task.incr()

    def __repr__(self):
        return f' [Desc{self.description}]'

    @classmethod
    def set_count(cls, val):
        cls.__count = val

    @classmethod
    def incr(cls):
        with open(TaskManager.DB_FILE_PATH, 'r') as f:
            file = json.load(f)
            __count = Task.set_count(int(max(file.keys())))
            cls.__count += 1
            return cls.__count

    def describe(self):
        return f'{self.id} id {self.description}'


class TaskManager:
    DB_FILE_PATH = 'todo_list_2.json'

    def __init__(self):
        self._task_dict = self._load_state_from_file(self.DB_FILE_PATH)

    def _load_state_from_file(self, filepath):
        if not os.path.exists(filepath):
            return {}

        with open(filepath, 'r') as f:
            temp = {}
            file = json.load(f)
            for task in file.values():
                desc, column = task
                t = Task(desc, column)
                temp[t.id] = t

            return temp

    def _print_visual_table(self):
        pass
        # TODO = []
        # IN_PROGRESS = []
        # DONE = []
        #
        # with open('todo_list.json', 'a') as f:
        #     for line in f.readlines():
        #         if 'DONE' in line:
        #             DONE.append(line)
        #         elif 'IN PROGRESS' in line:
        #             IN_PROGRESS.append(line)
        #         elif 'TODO' in line:
        #             TODO.append(line)
        #
        # dict_example = {
        #     "TODO": TODO,
        #     "IN_PROGRESS": IN_PROGRESS,
        #     "DONE": DONE
        #     }

        # visualisation = tabulate(dict_example, headers=["TODO", "IN_PROGRESS", "DONE"], tablefmt="fancy_outline")
        # print(visualisation)

    def _save_state_to_file(self, filepath):
        dict_to_save = {
            k: [v.description, v.status]
            for k, v in self._task_dict.items()
            }
        with open(filepath, 'r+') as f:
            file_data = json.load(f)
            print(file_data, 'file_data')   # working on it
            file_data.update(dict_to_save)
            f.seek(0)
            json.dump(file_data, f, indent=4)




    def _exit_program(self):
        exit()

    def _print_dict(self):
        print(self._task_dict)

    def _add_task(self):
        text = input('Wpisz treść zadania: ').lower()
        column = input(
            """Do jakiej kolumny dodać
        [t]odo
        in [p]rogress
        [d]one
          """
            ).lower()
        if column not in ('t', 'p', 'd'):
            raise ValueError('wrong value')
        task = Task(description=text, status=column)
        self._task_dict[task.id] = task
        self._save_state_to_file(self.DB_FILE_PATH)

    def _show_singl_task(self):
        pass

    def _edit_task(self):
        pass

    def _delete_task(self):
        pass

    @property
    def command_list(cls):
        return {
            'a': {'desc': 'add a new task', 'func': cls._add_task},
            'x': {'desc': 'stop/exit', 'func': cls._exit_program},
            's': {'desc': 'show TODO\'s table', 'func': cls._print_dict},
            'f': {'desc': 'show a single task', 'func': cls._show_singl_task},
            'e': {'desc': 'edit existing task', 'func': cls._edit_task},
            'r': {'desc': 'remove task', 'func': cls._delete_task},
            }


    def print_commands(self):
        print('Available commands')
        print(
            {
                k: v['desc']
                for k, v in self.command_list.items()})

    def execute_command(self, inp):
        while True:
            try:
                return self.command_list.get(inp)['func']
            except Exception:
                print("--> Oops!  That was no valid input.  Try again...\n")
                obj.run()

    def run(self):
        self._print_visual_table()
        try:
            while True:
                self.print_commands()
                command = input('Please insert value: ').lower()
                self.execute_command(command)()
        except Exception:
            print("--> Oops!  That was no valid input.  Try again...\n")
            obj.run()


obj = TaskManager()
obj.run()

