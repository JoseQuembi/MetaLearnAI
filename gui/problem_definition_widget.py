from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSignal

class ProblemDefinitionWidget(QWidget):
    problemDefined = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.search_space_input = QLineEdit()
        self.objective_function_input = QLineEdit()
        self.constraints_input = QLineEdit()

        layout.addWidget(QLabel('Espaço de Busca'))
        layout.addWidget(self.search_space_input)
        layout.addWidget(QLabel('Função Objetivo'))
        layout.addWidget(self.objective_function_input)
        layout.addWidget(QLabel('Restrições'))
        layout.addWidget(self.constraints_input)

        self.define_problem_button = QPushButton('Definir Problema')
        self.define_problem_button.clicked.connect(self.define_problem)
        layout.addWidget(self.define_problem_button)

        self.save_problem_button = QPushButton('Salvar Problema')
        self.save_problem_button.clicked.connect(self.save_problem)
        layout.addWidget(self.save_problem_button)

        self.setLayout(layout)

    def define_problem(self):
        search_space = eval(self.search_space_input.text())
        objective_function = eval(f"lambda x: {self.objective_function_input.text()}")
        constraints = [eval(f"lambda x: {c}") for c in self.constraints_input.text().split(',')]
        
        from metalearnai.problem_definition import LearningProblem
        problem = LearningProblem(search_space, objective_function, constraints)
        self.problemDefined.emit(problem)

    def save_problem(self):
        search_space = self.search_space_input.text()
        objective_function = self.objective_function_input.text()
        constraints = self.constraints_input.text()
        
        from metalearnai.database import create_connection, add_problem
        conn = create_connection("metalearnai.db")
        add_problem(conn, (search_space, objective_function, constraints))
        conn.close()
