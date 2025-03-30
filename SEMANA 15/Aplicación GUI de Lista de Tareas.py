import tkinter as tk
from tkinter import messagebox, Listbox


class TaskManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestor de Tareas")
        self.master.geometry("400x400")

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.bind('<Return>', self.add_task)

        # Botones de control
        self.add_button = tk.Button(master, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(master, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Lista de tareas
        self.task_listbox = Listbox(master, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.task_listbox.bind('<Double-Button-1>', self.complete_task)  # Doble clic para completar tarea

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

    def complete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task_text = self.task_listbox.get(selected_task_index)

            # Verificar si ya está marcada como completada
            if not task_text.startswith("✔ "):
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, "✔ " + task_text)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")


if __name__ == '__main__':
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
