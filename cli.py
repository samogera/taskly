import argparse
from models import User, Task, session

def add_user(name):
    user = User(name=name)
    session.add(user)
    session.commit()
    print(f"User '{name}' added.")

def list_users():
    users = session.query(User).all()
    if users:
        print("List of Users:")
        for user in users:
            print(f"User ID: {user.id}, Name: {user.name}")
    else:
        print("No users found.")

def add_task(description, user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        task = Task(description=description, user=user)
        session.add(task)
        session.commit()
        print(f"Task '{description}' added for user '{user.name}'.")
    else:
        print(f"User with ID {user_id} does not exist.")

def list_tasks(user_id):
    tasks = session.query(Task).filter_by(user_id=user_id).all()
    if tasks:
        print(f"Tasks for User ID {user_id}:")
        for task in tasks:
            print(f"Task ID: {task.id}, Description: {task.description}, Due Date: {task.due_date}")
    else:
        print(f"No tasks found for User ID {user_id}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Taskly CLI")
    parser.add_argument('--add-user', help="Add a new user")
    parser.add_argument('--list-users', action='store_true', help="List all users")
    parser.add_argument('--add-task', nargs=2, metavar=('DESC', 'USER_ID'), help="Add a new task")
    parser.add_argument('--list-tasks', metavar='USER_ID', help="List tasks for a user")

    args = parser.parse_args()

    if args.add_user:
        add_user(args.add_user)
    elif args.list_users:
        list_users()
    elif args.add_task:
        add_task(*args.add_task)
    elif args.list_tasks:
        list_tasks(args.list_tasks)
