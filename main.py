from tkinter import Tk
from View.questions_view import ESGView
from Model.model import ESGModel

def main():
    root = Tk()
    questions = ESGModel().generate_questions()
    view = ESGView(root, questions, submit_callback)
    view.start()

def submit_callback(responses):
    print("Respostas submetidas:", responses)


if __name__ == "__main__":
    main()
