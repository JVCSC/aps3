from tkinter import Tk
from View.questions_view import ESGView
from Model.model import ESGModel

def main():
    root = Tk()
    questions = ESGModel().generate_questions()
    view = ESGView(root, questions, submit_callback)
    view.start()

def submit_callback(responses):
    # Lógica para processar as respostas
    print("Respostas submetidas:", responses)
    # Aqui você pode chamar a próxima etapa, como exibir os resultados
    # results_view = ResultsView(root, results_data)
    # results_view.start()

if __name__ == "__main__":
    main()
