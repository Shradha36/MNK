import json
import os

class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"ID: {self.id} | Title: {self.title} | Status: {status}"

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    tasks_data = json.load(file)
                    self.tasks = [Task(task['id'], task['title'], task['completed']) for task in tasks_data]
                except json.JSONDecodeError:
                    self.tasks = []
        else:
            self.tasks = []

    def save_tasks(self):
        """Save tasks to the file."""
        tasks_data = [{'id': task.id, 'title': task.title, 'completed': task.completed} for task in self.tasks]
        with open(self.filename, 'w') as file:
            json.dump(tasks_data, file)

    def add_task(self, title):
        """Add a new task."""
        task_id = max([task.id for task in self.tasks], default=0) + 1  # Incremental ID
        new_task = Task(task_id, title)
        self.tasks.append(new_task)
        self.save_tasks()

    def view_tasks(self):
        """View all tasks."""
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def delete_task(self, task_id):
        """Delete a task by ID."""
        task_to_remove = next((task for task in self.tasks if task.id == task_id), None)
        if task_to_remove:
            self.tasks.remove(task_to_remove)
            self.save_tasks()
        else:
            print(f"Task with ID {task_id} not found.")

    def mark_task_complete(self, task_id):
        """Mark a task as completed."""
        task_to_mark = next((task for task in self.tasks if task.id == task_id), None)
        if task_to_mark:
            task_to_mark.completed = True
            self.save_tasks()
        else:
            print(f"Task with ID {task_id} not found.")

    def run(self):
        """Run the CLI interface."""
        while True:
            print("\nTask Manager")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Mark Task as Complete")
            print("5. Exit")
            
            choice = input("Choose an option: ")

            if choice == '1':
                title = input("Enter task title: ")
                self.add_task(title)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.view_tasks()
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    self.delete_task(task_id)
                except ValueError:
                    print("Invalid input. Please enter a valid ID.")
            elif choice == '4':
                self.view_tasks()
                try:
                    task_id = int(input("Enter task ID to mark as complete: "))
                    self.mark_task_complete(task_id)
                except ValueError:
                    print("Invalid input. Please enter a valid ID.")
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()
