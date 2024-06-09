from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

class NavigationWidget(QWidget):
    navigate = pyqtSignal(int)

    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        buttons = [
            ('Definir Problema', 1),
            ('Selecionar Algoritmo', 2),
            ('Treinar', 3),
            ('Resultados', 4)
        ]

        for text, index in buttons:
            button = QPushButton(text)
            button.clicked.connect(lambda checked, index=index: self.navigate.emit(index))
            layout.addWidget(button)

        self.setLayout(layout)
