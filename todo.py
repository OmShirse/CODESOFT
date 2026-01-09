import json
import os
from datetime import datetime
import shutil

FILENAME = "todo_data.json"


def load_tasks(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except:
            return []
    return []


def save_tasks(tasks, filename):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=2)


def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\n" + "=" * 50)
    print("TASK LIST")
    print("=" * 50)

    for task in tasks:
        status = "✓" if task.get("completed") else " "
        priority = task.get("priority", "medium")

        if priority == "high":
            p_symbol = " (High)"
        elif priority == "low":
            p_symbol = " (Low)"
        else:
            p_symbol = " (Medium)"

        due = f" | Due: {task['due_date']}" if task.get("due_date") else ""
        print(f"{task['id']:3d}. [{status}] {task['title']}{p_symbol}{due}")


def add_task(tasks):
    print("\nADD NEW TASK")
    print("-" * 30)

    title = input("Title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return tasks

    description = input("Description (optional): ").strip()

    print("\nPriority:")
    print("1. High")
    print("2. Medium (default)")
    print("3. Low")
    choice = input("Choose (1-3): ").strip()

    priority = "medium"
    if choice == "1":
        priority = "high"
    elif choice == "3":
        priority = "low"

    due_date = input("Due date (YYYY-MM-DD, optional): ").strip()

    new_id = max([t["id"] for t in tasks], default=0) + 1

    tasks.append({
        "id": new_id,
        "title": title,
        "description": description,
        "priority": priority,
        "due_date": due_date if due_date else None,
        "completed": False,
        "created_at": datetime.now().isoformat(),
        "completed_at": None
    })

    save_tasks(tasks, FILENAME)
    print("Task added successfully.")
    return tasks


def complete_task(tasks):
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks.")
        return tasks

    display_tasks(pending)
    task_id = input("Enter task ID to mark complete: ").strip()

    if not task_id.isdigit():
        print("Invalid input.")
        return tasks

    task_id = int(task_id)

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("Task already completed.")
            else:
                task["completed"] = True
                task["completed_at"] = datetime.now().isoformat()
                save_tasks(tasks, FILENAME)
                print("Task marked as completed.")
            return tasks

    print("Task not found.")
    return tasks


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return tasks

    display_tasks(tasks)
    task_id = input("Enter task ID to delete: ").strip()

    if not task_id.isdigit():
        print("Invalid input.")
        return tasks

    task_id = int(task_id)

    for task in tasks:
        if task["id"] == task_id:
            confirm = input(f"Delete '{task['title']}'? (y/N): ").lower()
            if confirm == "y":
                tasks.remove(task)
                save_tasks(tasks, FILENAME)
                print("Task deleted.")
            return tasks

    print("Task not found.")
    return tasks


def view_task_details(tasks):
    display_tasks(tasks)
    task_id = input("Enter task ID to view details: ").strip()

    if not task_id.isdigit():
        print("Invalid input.")
        return

    task_id = int(task_id)

    for task in tasks:
        if task["id"] == task_id:
            print("\nTASK DETAILS")
            print("-" * 30)
            print(f"Title: {task['title']}")
            print(f"Description: {task['description'] or 'None'}")
            print(f"Priority: {task['priority']}")
            print(f"Due Date: {task['due_date'] or 'Not set'}")
            print(f"Status: {'Completed' if task['completed'] else 'Pending'}")
            print(f"Created: {task['created_at']}")
            if task["completed_at"]:
                print(f"Completed: {task['completed_at']}")
            return

    print("Task not found.")


def show_statistics(tasks):
    total = len(tasks)
    completed = sum(t["completed"] for t in tasks)

    print("\nTASK STATISTICS")
    print("-" * 30)
    print(f"Total Tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {total - completed}")


def main():
    tasks = load_tasks(FILENAME)
    print("Simple To-Do List Application")

    while True:
        print("\nMENU")
        print("1. View all tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. View task details")
        print("6. Statistics")
        print("7. Backup data")
        print("0. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            tasks = add_task(tasks)
        elif choice == "3":
            tasks = complete_task(tasks)
        elif choice == "4":
            tasks = delete_task(tasks)
        elif choice == "5":
            view_task_details(tasks)
        elif choice == "6":
            show_statistics(tasks)
        elif choice == "7":
            if os.path.exists(FILENAME):
                name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                shutil.copy(FILENAME, name)
                print("Backup created.")
            else:
                print("No data to backup.")
        elif choice == "0":
            print("Exiting application.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
