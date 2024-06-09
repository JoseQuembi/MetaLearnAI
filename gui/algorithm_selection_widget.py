from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class AlgorithmSelectionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.strategy_input = QLineEdit()
        self.criteria_input = QLineEdit()

        layout.addWidget(QLabel('Estratégia'))
        layout.addWidget(self.strategy_input)
        layout.addWidget(QLabel('Critério de Parada'))
        layout.addWidget(self.criteria_input)

        self.save_button = QPushButton('Salvar Algoritmo')
        self.save_button.clicked.connect(self.save_algorithm)
        layout.addWidget(self.save_button)

        self.back_button = QPushButton('Voltar ao Menu Inicial')
        self.back_button.clicked.connect(self.back_to_menu)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def save_algorithm(self):
        strategy = self.strategy_input.text()
        criteria = self.criteria_input.text()

        from metalearnai.database import create_connection, add_algorithm
        conn = create_connection('metalearnai.db')
        add_algorithm(conn, strategy, criteria)

    def back_to_menu(self):
        self.parentWidget().setCurrentIndex(0)
