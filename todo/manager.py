from datetime import datetime
from .storage import save_tasks


def generate_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def add_task(tasks, title):
    task = {
        "id": generate_id(tasks),
        "title": title,
        "done": False,
        "created_at": datetime.now().isoformat()
    }

    tasks.append(task)
    save_tasks(tasks)


def list_tasks(tasks):

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "✔" if task["done"] else "✗"

        print(
            f"{task['id']} | [{status}] {task['title']}"
        )


def complete_task(tasks, task_id):

    for task in tasks:

        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            return True

    return False


def delete_task(tasks, task_id):

    for task in tasks:

        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return True

    return False
