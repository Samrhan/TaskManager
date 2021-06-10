class Task:
    def __init__(self, __description, __id):
        self._description = __description
        self._status = 0
        self._id = __id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, state):
        self._status = state

    @property
    def description(self):
        return self._description

    @property
    def id(self):
        return self._id

    def __repr__(self):
        return f"{self.id} [{' ' if self.status == 0 else 'x'}] {self.description}"


class TaskNotFound(Exception):
    pass


class TaskManager:
    def __init__(self):
        self._task_list = []

    def add_task(self, description):
        gen_id = 0
        if len(self._task_list) != 0:
            gen_id = max(task.id for task in self._task_list) + 1
        self._task_list.append(Task(description, gen_id))

    def remove_task(self, __id):
        task = next((task for task in self._task_list if task.id == int(__id)), None)
        if task is not None:
            self._task_list.remove(task)
        else:
            raise TaskNotFound

    def change_status(self, __id):
        task = next((task for task in self._task_list if task.id == int(__id)), None)
        if task is not None:
            task.status = not task.status
        else:
            raise TaskNotFound

    @property
    def task_list(self):
        return self._task_list

    def __repr__(self):
        return str(self._task_list)


class AddAction:
    def __init__(self, __task_manager, __user_input):
        action, args = self.parse_command(__user_input)
        self.triggers = {
            '+': __task_manager.add_task,
            '-': __task_manager.remove_task,
            'x': __task_manager.change_status,
            'o': __task_manager.change_status
        }
        self.triggers[action](args)

    @staticmethod
    def parse_command(user_input):
        return user_input[0], user_input[1:].strip()


def interaction_loop():
    user_input = ''
    task_manager = TaskManager()
    while user_input != 'q':
        try:
            AddAction(task_manager, input())
            if len(task_manager.task_list) == 0:
                print("No task yet")
            for i in task_manager.task_list:
                print(i)
        except TaskNotFound:
            print("Task not found")
        except ValueError:
            print("Incorrect Value")

#interaction_loop()
