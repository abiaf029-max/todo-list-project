
def load_tasks():
    tasks = []

    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                if "|" in line:
                    parts = line.split("|")
                    task_name = parts[0]
                    done = parts[1] == "True"
                    tasks.append({"task": task_name, "done": done})
                else:
                    # if old tasks.txt has only task names
                    tasks.append({"task": line, "done": False})

    except FileNotFoundError:
        with open("tasks.txt", "w") as file:
            pass

    return tasks


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['done']}\n")


def show_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks yet.")
        return

    print("\nYour tasks:")
    for i in range(len(tasks)):
        if tasks[i]["done"] == True:
            status = "[x]"
        else:
            status = "[ ]"

        print(f"{i + 1}. {status} {tasks[i]['task']}")


def add_task(tasks):
    task_name = input("Enter a new task: ").strip()

    if task_name == "":
        print("Task cannot be empty.")
        return

    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")


def delete_task(tasks):
    if len(tasks) == 0:
        print("No tasks to delete.")
        return

    show_tasks(tasks)

    try:
        delete_num = int(input("Enter task number to delete: "))

        if 1 <= delete_num <= len(tasks):
            removed_task = tasks.pop(delete_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a number only.")


def mark_complete(tasks):
    if len(tasks) == 0:
        print("No tasks to mark.")
        return

    show_tasks(tasks)

    try:
        task_num = int(input("Enter task number to mark as completed: "))

        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a number only.")


def edit_task(tasks):
    if len(tasks) == 0:
        print("No tasks to edit.")
        return

    show_tasks(tasks)

    try:
        task_num = int(input("Enter task number to edit: "))

        if 1 <= task_num <= len(tasks):
            new_name = input("Enter new task name: ").strip()

            if new_name == "":
                print("Task cannot be empty.")
            else:
                tasks[task_num - 1]["task"] = new_name
                save_tasks(tasks)
                print("Task updated successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a number only.")


def clear_all_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks to clear.")
        return

    confirm = input("Are you sure you want to delete all tasks? (y/n): ").lower()

    if confirm == "y":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks deleted.")
    else:
        print("Clear cancelled.")


tasks = load_tasks()
print("DEBUG:", tasks)

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task Complete")
    print("5. Edit Task")
    print("6. Clear All Tasks")
    print("7. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        show_tasks(tasks)

    elif choice == "2":
        add_task(tasks)

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4": 
        mark_complete(tasks)

    elif choice == "5":
        edit_task(tasks)

    elif choice == "6":
        clear_all_tasks(tasks)

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")