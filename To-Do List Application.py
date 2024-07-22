import tkinter as tk
from tkinter import messagebox

class Todo:
    def __init__(self, window):
        self.window = window
        self.window.title("To-Do List Application")

        
        self.tasks = []

        
        self.label_task = tk.Label(window, text="Enter Task:")
        self.label_task.grid(row=0, column=0, padx=10, pady=5)

        self.entry_task = tk.Entry(window, width=30)
        self.entry_task.grid(row=0, column=1, padx=10, pady=5)

        self.button_add_task = tk.Button(window, text="Add Task", command=self.add_task)
        self.button_add_task.grid(row=0, column=2, padx=10, pady=5)

        self.task_listbox = tk.Listbox(window, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

        self.button_complete_task = tk.Button(window, text="Mark as Completed", command=self.complete_task)
        self.button_complete_task.grid(row=2, column=0, padx=10, pady=5)

        self.button_delete_task = tk.Button(window, text="Delete Task", command=self.delete_task)
        self.button_delete_task.grid(row=2, column=1, padx=10, pady=5)

        self.button_view_tasks = tk.Button(window, text="View Tasks", command=self.view_tasks)
        self.button_view_tasks.grid(row=2, column=2, padx=10, pady=5)

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index] = f"{self.tasks[index]} - Completed"
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, self.tasks[index])
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def view_tasks(self):
        messagebox.showinfo("Tasks", "\n".join(self.tasks))


if __name__ == "__main__":
    window = tk.Tk()
    app = Todo(window)
    window.mainloop()



