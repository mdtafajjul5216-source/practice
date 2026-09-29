tasks = []


def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task():
    task = input("\nEnter a task: ")
    tasks.append(task)
    print("Task added successfully!")


def delete_task():
    show_tasks()

    if len(tasks) > 0:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted_task = tasks.pop(number - 1)
            print(f"'{deleted_task}' deleted successfully!")
        else:
            print("Invalid task number.")


while True:
    print("\n===== TO-DO LIST =====")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")