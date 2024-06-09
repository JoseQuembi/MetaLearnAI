from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal

class NavigationWidget(QWidget):
    navigateToProblemDefinition = pyqtSignal()
    navigateToAlgorithmSelection = pyqtSignal()
    navigateToTraining = pyqtSignal()
    navigateToResults = pyqtSignal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.problem_button = QPushButton('Definir Problema')
        self.problem_button.clicked.connect(self.navigateToProblemDefinition.emit)
        layout.addWidget(self.problem_button)

        self.algorithm_button = QPushButton('Selecionar Algoritmo')
        self.algorithm_button.clicked.connect(self.navigateToAlgorithmSelection.emit)
        layout.addWidget(self.algorithm_button)

        self.training_button = QPushButton('Treinar Modelo')
        self.training_button.clicked.connect(self.navigateToTraining.emit)
        layout.addWidget(self.training_button)

        self.results_button = QPushButton('Resultados')
        self.results_button.clicked.connect(self.navigateToResults.emit)
        layout.addWidget(self.results_button)

        self.setLayout(layout)
