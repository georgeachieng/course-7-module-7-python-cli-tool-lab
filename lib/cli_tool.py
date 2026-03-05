import argparse

try:
    from lib.models import Task, User
except ImportError:  # Allows direct execution: python lib/cli_tool.py ...
    from models import Task, User

# Global dictionary to store users and their tasks
users = {}

# Function to add a task for a user
def add_task(args):
    user = users.get(args.user) or User(args.user)
    users[args.user] = user

    task = Task(args.title)
    user.add_task(task)

# Function to mark a task as complete
def complete_task(args):
    user = users.get(args.user)
    if user:
        task = user.get_task_by_title(args.title)
        if task:
            task.complete()
        else:
            print("❌ Task not found.")
    else:
        print("❌ User not found.")

# CLI entry point
def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user", help="Name of the user")
    add_parser.add_argument("title", help="Title of the task")
    add_parser.set_defaults(func=add_task)

    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user", help="Name of the user")
    complete_parser.add_argument("title", help="Title of the task")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
