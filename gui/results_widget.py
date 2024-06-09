from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton

class ResultsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.results_display = QTextEdit()
        self.results_display.setReadOnly(True)
        layout.addWidget(QLabel('Resultados'))
        layout.addWidget(self.results_display)

        self.back_button = QPushButton('Voltar ao Menu Inicial')
        self.back_button.clicked.connect(self.back_to_menu)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def display_results(self, results):
        self.results_display.setText(str(results))

    def back_to_menu(self):
        self.parentWidget().setCurrentIndex(0)
