import os
TASKS_FILE = 'tasks.txt'
#loading tasks
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    return []
#saving tasks
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')
#adding new tasks
def add_task(tasks, task_description):
    tasks.append(f"[ ] {task_description}")
    save_tasks(tasks)
    print(f"Task '{task_description}' added successfully!")
#viewing the tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
#deleting task
def delete_task(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task}' has been deleted!")
    else:
        print("Invalid task number!")
#marking complated tasks
def mark_completed(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1] = tasks[task_number - 1].replace("[ ]", "[X]")
        save_tasks(tasks)
        print(f"Task {task_number} marked as completed!")
    else:
        print("Invalid task number!")
#main funtion for interacting with user
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Mark a task as completed")
        print("5. Exit")
        try:
            choice = int(input("Choose an option (1-5): "))
            if choice == 1:
                task_description = input("Enter the task description: ")
                add_task(tasks, task_description)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                task_number = int(input("Enter the task number to delete: "))
                delete_task(tasks, task_number)
            elif choice == 4:
                task_number = int(input("Enter the task number to mark as completed: "))
                mark_completed(tasks, task_number)
            elif choice == 5:
                print("Exiting application...")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()
