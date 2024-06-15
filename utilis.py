from models import User, Task, session

def get_user_by_id(user_id):
    return session.query(User).filter_by(id=user_id).first()

def list_user_tasks(user_id):
    user = get_user_by_id(user_id)
    if user:
        return user.tasks
    return []

def add_task_for_user(user_id, description, priority='Medium'):
    user = get_user_by_id(user_id)
    if user:
        new_task = Task(description=description, priority=priority, user_id=user_id)
        session.add(new_task)
        session.commit()
        return True
    return False

def add_mockup_data():
    # Add mockup data for testing
    user1 = User(name='John Doe')
    user2 = User(name='Jane Smith')

    task1 = Task(description='Complete Taskly Project', priority='High', user_id=1)
    task2 = Task(description='Review Code', priority='Medium', user_id=1)
    task3 = Task(description='Write Documentation', priority='Low', user_id=2)

    session.add_all([user1, user2, task1, task2, task3])
    session.commit()
