
# using a list to store tasks - probably could use a file later
tasks = []

def show_menu():
    print("\n" + "="*50)
    print("           TO-DO LIST MANAGER")
    print("="*50)
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Exit")
    print("="*50)

def view_tasks():
    if len(tasks) == 0:
        print("\nYour to-do list is empty! Nothing to do :)")
        return
    
    print("\nYour Tasks:")
    print("-"*50)
    for i in range(len(tasks)):
        task = tasks[i]
        status = "[✓]" if task["done"] else "[ ]"
        print(f"{i+1}. {status} {task['name']}")
    print("-"*50)

def add_task():
    task_name = input("\nWhat task do you want to add? ")
    if task_name.strip() == "":
        print("You can't add an empty task!")
        return
    
    # store as dictionary so we can track if its done
    new_task = {
        "name": task_name,
        "done": False
    }
    tasks.append(new_task)
    print(f"Added: '{task_name}'")

def mark_complete():
    if len(tasks) == 0:
        print("\nNo tasks to mark as complete!")
        return
    
    view_tasks()
    try:
        task_num = int(input("\nWhich task did you complete? (enter number): "))
        if task_num < 1 or task_num > len(tasks):
            print("That task number doesn't exist!")
            return
        
        tasks[task_num - 1]["done"] = True
        print(f"Nice! Marked task {task_num} as complete!")
    except:
        print("Please enter a valid number")

def delete_task():
    if len(tasks) == 0:
        print("\nNo tasks to delete!")
        return
    
    view_tasks()
    try:
        task_num = int(input("\nWhich task do you want to delete? "))
        if task_num < 1 or task_num > len(tasks):
            print("That task doesn't exist!")
            return
        
        deleted = tasks.pop(task_num - 1)
        print(f"Deleted: '{deleted['name']}'")
    except:
        print("Invalid input")

# main program loop
def run():
    print("\nWelcome to your To-Do List!")
    
    while True:
        show_menu()
        choice = input("\nWhat would you like to do? ")
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("\nGoodbye! Stay productive!")
            break
        else:
            print("Invalid choice! Pick a number between 1-5")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    run()
