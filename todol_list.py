import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        pass

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=15)

listbox = tk.Listbox(frame, width=180, height=15)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
listbox.config(bg='red')


scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
scrollbar.config(bg='blue')

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=100)
entry.pack()
entry.config(bg='yellow')


add_button = tk.Button(root, text="Add Task", width=15,command=add_task)
add_button.pack(side=tk.RIGHT,fill=tk.BOTH)
add_button.config(bg='green')

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(side=tk.LEFT,fill=tk.BOTH)
delete_button.config(bg='red')


root.mainloop()