from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit

class ResultsWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.results_display = QTextEdit()
        self.results_display.setReadOnly(True)
        layout.addWidget(QLabel('Resultados'))
        layout.addWidget(self.results_display)

        self.setLayout(layout)

    def display_results(self, results):
        self.results_display.setText(str(results))
