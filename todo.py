import os

FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE):
        return []
    
    with open(FILE, "r") as f:
        return [task.strip() for task in f.readlines()]

# Save tasks to file
def save_tasks(tasks):
    with open(FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Main Menu
def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    print("===========================\n")

def main():
    tasks = load_tasks()

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        # View tasks
        if choice == "1":
            if not tasks:
                print("\nNo tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        # Add task
        elif choice == "2":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added successfully!")

        # Delete task
        elif choice == "3":
            if not tasks:
                print("No tasks to delete.")
                continue

            try:
                delete_index = int(input("Enter task number to delete: "))
                tasks.pop(delete_index - 1)
                save_tasks(tasks)
                print("Task deleted successfully!")
            except (ValueError, IndexError):
                print("Invalid task number. Try again.")

        # Exit app
        elif choice == "4":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
