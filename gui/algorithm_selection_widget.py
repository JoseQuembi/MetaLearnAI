# MetaLearnAI gui algorithm_selection_widget.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QComboBox, QLabel
from PyQt5.QtCore import pyqtSignal

class AlgorithmSelectionWidget(QWidget):
    algorithmSelected = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.strategy_input = QComboBox()
        self.strategy_input.addItems(['DummyStrategy'])  # Adicione outras estratégias aqui

        self.stop_criterion_input = QComboBox()
        self.stop_criterion_input.addItems(['DummyStopCriterion'])  # Adicione outros critérios de parada aqui

        self.update_strategy_input = QComboBox()
        self.update_strategy_input.addItems(['DummyUpdateStrategy'])  # Adicione outras estratégias de atualização aqui

        layout.addWidget(QLabel('Estratégia'))
        layout.addWidget(self.strategy_input)
        layout.addWidget(QLabel('Critério de Parada'))
        layout.addWidget(self.stop_criterion_input)
        layout.addWidget(QLabel('Estratégia de Atualização'))
        layout.addWidget(self.update_strategy_input)

        self.select_algorithm_button = QPushButton('Selecionar Algoritmo')
        self.select_algorithm_button.clicked.connect(self.select_algorithm)
        layout.addWidget(self.select_algorithm_button)

        self.setLayout(layout)

    def select_algorithm(self):
        strategy_name = self.strategy_input.currentText()
        stop_criterion_name = self.stop_criterion_input.currentText()
        update_strategy_name = self.update_strategy_input.currentText()

        from metalearnai.meta_learning_algorithms import MetaLearningAlgorithm, DummyStrategy, DummyStopCriterion, DummyUpdateStrategy

        if strategy_name == 'DummyStrategy':
            Strategy = DummyStrategy
        if stop_criterion_name == 'DummyStopCriterion':
            StopCriterion = DummyStopCriterion
        if update_strategy_name == 'DummyUpdateStrategy':
            UpdateStrategy = DummyUpdateStrategy

        algorithm = MetaLearningAlgorithm(Strategy(), StopCriterion(), UpdateStrategy())
        self.algorithmSelected.emit(algorithm)
