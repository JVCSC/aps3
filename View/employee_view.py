import tkinter as tk
from tkinter import messagebox

class EmployeeView(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Número de funcionários:")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.button = tk.Button(self, text="Next", command=self.next)
        self.button.pack()

    def next(self):
        num_employees = self.entry.get()
        if num_employees.isdigit():
            self.controller.show_questions_view(int(num_employees))
        else:
            messagebox.showerror("Input Error", "Por favor, insira um número válido de funcionários")
