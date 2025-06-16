import tkinter as tk
from tkinter import messagebox
import os

# File to store tasks
TASKS_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = entry.get().strip()
    if task == "":
        messagebox.showwarning("Input Error", "Please enter a task")
        return
    listbox.insert(tk.END, task)
    entry.delete(0, tk.END)
    save_tasks()

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a task to delete")
        return
    for index in reversed(selected):
        listbox.delete(index)
    save_tasks()

# GUI setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("300x400")

title = tk.Label(root, text="📝 To-Do List", font=("Arial", 16))
title.pack(pady=10)

entry = tk.Entry(root, width=25, font=("Arial", 12))
entry.pack(pady=5)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

listbox = tk.Listbox(root, width=30, height=10, font=("Arial", 12))
listbox.pack(pady=10)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

load_tasks()  # Load tasks on startup
root.mainloop()
