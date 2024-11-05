def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to remove: "))
        removed_task = tasks.pop(task_number - 1)
        print(f"'{removed_task}' has been removed from your to-do list.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def todo_list():
    tasks = []
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. View To-Do List")
        print("2. Add a Task")
        print("3. Remove a Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    todo_list()
