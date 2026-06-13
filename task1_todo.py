# Simple To-Do List App
# Stores tasks in memory with basic status tracking

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks yet. Add something!\n")
        return
    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "○"
        print(f"  {i}. [{status}] {task['name']}")
    print()

def add_task():
    name = input("Task description: ").strip()
    if not name:
        print("Can't add an empty task.")
        return
    tasks.append({"name": name, "done": False})
    print(f"Added: '{name}'")

def mark_done():
    show_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark complete: "))
        task = tasks[num - 1]
        if task["done"]:
            print("Already marked as done.")
        else:
            task["done"] = True
            print(f"Nice! '{task['name']}' marked as done.")
    except (ValueError, IndexError):
        print("Invalid number, try again.")

def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        print(f"Deleted: '{removed['name']}'")
    except (ValueError, IndexError):
        print("Invalid number.")

def update_task():
    show_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to edit: "))
        task = tasks[num - 1]
        new_name = input(f"New description (current: '{task['name']}'): ").strip()
        if new_name:
            task["name"] = new_name
            print("Task updated.")
        else:
            print("No changes made.")
    except (ValueError, IndexError):
        print("Invalid number.")

def main():
    print("=== To-Do List ===")
    menu = {
        "1": ("View tasks", show_tasks),
        "2": ("Add task", add_task),
        "3": ("Mark as done", mark_done),
        "4": ("Edit task", update_task),
        "5": ("Delete task", delete_task),
        "6": ("Quit", None),
    }

    while True:
        print("1. View  2. Add  3. Done  4. Edit  5. Delete  6. Quit")
        choice = input("Choose: ").strip()
        if choice == "6":
            print("See ya!")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("Invalid option, pick 1–6.")

if __name__ == "__main__":
    main()
