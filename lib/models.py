# Task class
class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True
        print(f" Task '{self.title}' completed.")


# User class
class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f" Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title):
        # Search for a task by its title in the user's task list
        for task in self.tasks:
            if task.title == title:
                return task
        return None
