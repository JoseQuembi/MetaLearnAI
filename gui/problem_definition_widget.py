from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class ProblemDefinitionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.problem_name_input = QLineEdit()
        self.search_space_input = QLineEdit()
        self.objective_function_input = QLineEdit()
        self.constraints_input = QLineEdit()

        layout.addWidget(QLabel('Nome do Problema'))
        layout.addWidget(self.problem_name_input)
        layout.addWidget(QLabel('Espaço de Busca'))
        layout.addWidget(self.search_space_input)
        layout.addWidget(QLabel('Função Objetivo'))
        layout.addWidget(self.objective_function_input)
        layout.addWidget(QLabel('Restrições'))
        layout.addWidget(self.constraints_input)

        self.save_button = QPushButton('Salvar Problema')
        self.save_button.clicked.connect(self.save_problem)
        layout.addWidget(self.save_button)

        self.back_button = QPushButton('Voltar ao Menu Inicial')
        self.back_button.clicked.connect(self.back_to_menu)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def save_problem(self):
        problem_name = self.problem_name_input.text()
        search_space = self.search_space_input.text()
        objective_function = self.objective_function_input.text()
        constraints = self.constraints_input.text()

        from metalearnai.database import create_connection, add_problem
        conn = create_connection('metalearnai.db')
        add_problem(conn, problem_name, search_space, objective_function, constraints)

    def back_to_menu(self):
        self.parentWidget().setCurrentIndex(0)
