import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.tasks = []

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=15, bd=0, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=10)

        self.entry_task = tk.Entry(self.entry_frame, width=40)
        self.entry_task.pack(side=tk.LEFT, padx=(0, 10))

        self.btn_add_task = tk.Button(self.entry_frame, text="Add Task", width=10, command=self.add_task, bg='lightgreen')
        self.btn_add_task.pack(side=tk.LEFT)

        self.btn_delete_task = tk.Button(self.root, text="Delete Task", width=48, command=self.delete_task, bg='lightcoral')
        self.btn_delete_task.pack(pady=5)
    #making add task function
    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    #making delete task function
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    #updating the listbox function
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{index}. {task}")
#main function to run
if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(0,0)
    app = ToDoListApp(root)
    root.mainloop()
