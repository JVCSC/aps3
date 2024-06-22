import tkinter as tk
from Model.model import ESGModel
from View.login_view import LoginView
from View.employee_view import EmployeeView
from View.questions_view import QuestionsView
from View.results_view import ResultsView

class Controller(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.model = ESGModel()
        self.pack()
        self.show_login_view()

    def show_login_view(self):
        if hasattr(self, 'current_view'):
            self.current_view.pack_forget()
        self.current_view = LoginView(master=self, controller=self)
        self.current_view.pack()

    def show_employee_view(self):
        self.current_view.pack_forget()
        self.current_view = EmployeeView(master=self, controller=self)
        self.current_view.pack()

    def show_questions_view(self, num_employees):
        self.current_view.pack_forget()
        self.current_view = QuestionsView(master=self, controller=self)
        self.current_view.pack()

    def show_results_view(self):
        results = self.model.calculate_results()
        self.current_view.pack_forget()
        self.current_view = ResultsView(master=self, controller=self, results=results)
        self.current_view.pack()

    def login(self, username, password):
        # Aqui estamos removendo a verificação rígida de "usuário" e "senha"
        # Permitindo que qualquer combinação de entrada prossiga para o cadastro
        return True

    def register(self, company_name, person_name, num_employees):
        # Aqui você pode adicionar a lógica para salvar os dados de cadastro, se necessário
        print(f"Empresa: {company_name}, Pessoa: {person_name}, Funcionários: {num_employees}")
