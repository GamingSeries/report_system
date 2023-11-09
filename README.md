# Weekly Report System

This is a Python-based Weekly Report System with a graphical user interface (GUI) for managing and tracking tasks. It allows you to add, list, and mark tasks as completed. Additionally, a macOS status bar application is provided for users who want the application to start at login and stay in the macOS menu bar.

## Features

- Add tasks with a task type (Assignment, Lab Report, Quiz, Discussion) and a description.
- Display tasks in a list with checkboxes to mark them as completed.
- Mark tasks as completed by selecting them and using the "Mark as Completed" button.
- Dynamically update the task list when tasks are added or marked as completed.
- A separate macOS status bar application is available for those who want the application to start at login and stay in the macOS menu bar.

## Requirements

- Python 3
- Tkinter (usually included with Python)
- Operating System (Windows, macOS, or Linux)

## Usage

1. Run the main application by executing the Python script (`weekly_report_app.py`).
2. Use the "Add Task" section to input the task type and description, and then click the "Create Task" button to add a new task.
3. View the list of tasks in the main application window. Each task has a checkbox to mark it as completed.
4. Use the "Mark as Completed" button to toggle the completion status of selected tasks.
5. For macOS users, a separate macOS status bar application (`mac_status_bar.py`) is available to start the application at login and keep it in the macOS menu bar.

## To-Do

- Add automatic task clearing based on the day of the week.
- Implement the persistence of tasks even after system restart.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
