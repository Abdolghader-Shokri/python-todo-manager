from todo.storage import load_tasks
from todo.manager import add_task, list_tasks, complete_task, delete_task


def show_menu():

    print("\nTodo Manager")
    print("1. Add task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def main():

    tasks = load_tasks()

    while True:

        show_menu()

        choice = input("Choose: ")

        if choice == "1":

            title = input("Task title: ")
            add_task(tasks, title)

        elif choice == "2":

            list_tasks(tasks)

        elif choice == "3":

            task_id = int(input("Task id: "))

            if not complete_task(tasks, task_id):
                print("Task not found")

        elif choice == "4":

            task_id = int(input("Task id: "))

            if not delete_task(tasks, task_id):
                print("Task not found")

        elif choice == "5":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
