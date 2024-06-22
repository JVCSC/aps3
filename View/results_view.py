import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ResultsView(tk.Frame):
    def __init__(self, master=None, controller=None, results=None):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.results = results
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Resultados dos Indicadores ESG")
        self.label.pack()

        self.plot_results()

    def plot_results(self):
        categories = list(self.results.keys())
        scores = list(self.results.values())

        fig, ax = plt.subplots()
        ax.bar(categories, scores, color=['green', 'blue', 'purple'])
        ax.set_xlabel('Categorias')
        ax.set_ylabel('Pontuação')
        ax.set_title('Indicadores ESG')

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()
