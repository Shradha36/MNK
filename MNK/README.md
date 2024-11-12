# Task Manager
* A simple command-line task manager implemented in Python that allows users to add, view, delete, and mark tasks as complete. The tasks are stored in a JSON file, ensuring persistence between sessions.

## Features
* Add Task: Create a new task by providing a title.
* View Tasks: List all tasks along with their status (completed or not).
* Delete Task: Remove a task using its unique ID.
* Mark Task as Complete: Update the status of a task to completed.
* Data Persistence: Tasks are saved in a JSON file (tasks.json) and are loaded upon starting the program.

## Installation
* To run this program, you need Python 3.x installed on your machine. You can download it from python.org.

1. Clone the repository or download the script file.

2. Open a terminal and navigate to the directory containing the script.

3. Run the script with the following command:
* python task_manager.py

## Usage
* Once you run the script, a command-line interface will be displayed with the following options:

1. Add Task: You will be prompted to enter a task title.
2. View Tasks: All current tasks will be displayed with their IDs and status.
3. Delete Task: After viewing the tasks, you can enter the ID of the task you wish to delete.
4. Mark Task as Complete: Similar to deleting a task, you can enter the ID of the task you want to mark as completed.
5. Exit: Choose this option to exit the program.

### Example
* Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Exit
* Choose an option: 1
* Enter task title: Buy groceries

## Implementation Details
### Task Class
* The Task class represents a single task. It has the following attributes:

    * id: Unique identifier for the task.
    * title: The title of the task.
    * completed: Boolean indicating whether the task is completed.

### TaskManager Class
* The TaskManager class manages the collection of tasks and provides functionality to load and save tasks to a JSON file.
* load_tasks: Loads tasks from the tasks.json file.
* save_tasks: Saves the current tasks to the tasks.json file.
* add_task: Adds a new task and saves it.
* view_tasks: Displays all tasks.
* delete_task: Removes a task by ID.
* mark_task_complete: Marks a task as completed by ID.
* run: Starts the command-line interface for user interaction.

### Data Storage
* Tasks are stored in a JSON file (tasks.json) in the following format:
* [
    {
        "id": 1,
        "title": "Buy groceries",
        "completed": false
    },
    {
        "id": 2,
        "title": "Finish homework",
        "completed": true
    }
]
