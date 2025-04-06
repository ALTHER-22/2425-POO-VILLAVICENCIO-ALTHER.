import tkinter as tk
from tkinter import messagebox

# Función para añadir una tarea
def add_task(event=None):
    task = task_entry.get().strip()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, escribe una tarea.")

# Función para marcar una tarea como completada
def mark_completed(event=None):
    selected = tasks_listbox.curselection()
    for index in selected:
        task = tasks_listbox.get(index)
        if not task.startswith("[✔]"):
            tasks_listbox.delete(index)
            tasks_listbox.insert(index, "[✔] " + task)
            tasks_listbox.itemconfig(index, fg="gray")

# Función para eliminar una tarea
def delete_task(event=None):
    selected = tasks_listbox.curselection()
    for index in reversed(selected):  # Reversed para eliminar de atrás hacia adelante
        tasks_listbox.delete(index)

# Cerrar la aplicación
def close_app(event=None):
    root.quit()

# Cambiar color al pasar el mouse por encima del botón
def on_mouse_enter(event):
    event.widget.config(bg='lightblue')

def on_mouse_leave(event):
    event.widget.config(bg='SystemButtonFace')

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas Pendientes")
root.geometry("500x400")

# Campo de entrada de tareas
task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10, padx=10, fill=tk.X)
task_entry.focus()

# Botones
button_frame = tk.Frame(root)
button_frame.pack()

add_btn = tk.Button(button_frame, text="Añadir", command=add_task)
add_btn.grid(row=0, column=0, padx=5)

complete_btn = tk.Button(button_frame, text="Marcar Completada", command=mark_completed)
complete_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(button_frame, text="Eliminar", command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)

# Efectos visuales para los botones
for btn in [add_btn, complete_btn, delete_btn]:
    btn.bind("<Enter>", on_mouse_enter)
    btn.bind("<Leave>", on_mouse_leave)

# Lista de tareas
tasks_listbox = tk.Listbox(root, font=("Arial", 14), selectmode=tk.MULTIPLE)
tasks_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Enlazar teclas
root.bind("<Return>", add_task)       # Enter para añadir
root.bind("<c>", mark_completed)      # 'c' para completar
root.bind("<C>", mark_completed)      # 'C' para completar
root.bind("<d>", delete_task)         # 'd' para eliminar
root.bind("<D>", delete_task)         # 'D' para eliminar
root.bind("<Delete>", delete_task)    # Supr para eliminar
root.bind("<Escape>", close_app)      # Escape para salir

# Iniciar la interfaz
root.mainloop()
