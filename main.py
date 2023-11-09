import tkinter as tk
from tkinter import ttk

# Create a list to store tasks and their completion status
tasks = []

# Create a function to update the task list
def update_task_list():
    task_list.delete(0, tk.END)  # Clear the existing list

    # Iterate through tasks and add them to the listbox with checkboxes
    for i, (task, completed) in enumerate(tasks):
        task_list.insert(tk.END, f"[{'X' if completed else ' '}] {task}")

# Create a function to add a task
def add_task():
    task_type = task_type_var.get()
    task_description = task_description_entry.get()

    if task_type and task_description:
        tasks.append((f"{task_type}: {task_description}", False))  # Add the task with its completion status
        update_task_list()
        task_description_entry.delete(0, tk.END)  # Clear the task description entry

# Create a function to mark a task as completed
def mark_completed():
    selected_index = task_list.curselection()
    if selected_index:
        index = selected_index[0]
        task, completed = tasks[index]
        tasks[index] = (task, not completed)
        update_task_list()

# Create the main application window
root = tk.Tk()
root.title("Weekly Report System")

# Create a sidebar menu for adding tasks
sidebar = ttk.LabelFrame(root, text="Add Task")
sidebar.grid(row=0, column=0, padx=10, pady=10, sticky="n")

# Task Type Dropdown
ttk.Label(sidebar, text="Task Type:").grid(row=0, column=0, padx=5, pady=5)
task_type_var = tk.StringVar()
task_type_dropdown = ttk.Combobox(sidebar, textvariable=task_type_var, values=["Assignment", "Lab Report", "Quiz", "Discussion"])
task_type_dropdown.grid(row=0, column=1, padx=5, pady=5)

# Task Description Entry
ttk.Label(sidebar, text="Task Description:").grid(row=1, column=0, padx=5, pady=5)
task_description_var = tk.StringVar()
task_description_entry = ttk.Entry(sidebar, textvariable=task_description_var)
task_description_entry.grid(row=1, column=1, padx=5, pady=5)

# Add Task Button
add_task_button = ttk.Button(sidebar, text="Create Task", command=add_task)
add_task_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

# Create a listbox to display tasks with checkboxes
task_list = tk.Listbox(root, selectmode=tk.SINGLE)
task_list.grid(row=1, column=0, padx=10, pady=10)

# Add a button to mark tasks as completed
mark_completed_button = ttk.Button(root, text="Mark as Completed", command=mark_completed)
mark_completed_button.grid(row=2, column=0, padx=10, pady=5)

# Run the application
update_task_list()  # Initial update of the task list
root.mainloop()
