# MetaLearnAI gui main_window.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from gui.problem_definition_widget import ProblemDefinitionWidget
from gui.algorithm_selection_widget import AlgorithmSelectionWidget
from gui.training_widget import TrainingWidget
from gui.results_widget import ResultsWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('MetaLearnAI Interface Gráfica')

        self.problem_widget = ProblemDefinitionWidget()
        self.algorithm_widget = AlgorithmSelectionWidget()
        self.training_widget = TrainingWidget()
        self.results_widget = ResultsWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.problem_widget)
        layout.addWidget(self.algorithm_widget)
        layout.addWidget(self.training_widget)
        layout.addWidget(self.results_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.problem_widget.problemDefined.connect(self.on_problem_defined)
        self.algorithm_widget.algorithmSelected.connect(self.on_algorithm_selected)
        self.training_widget.trainingCompleted.connect(self.on_training_completed)

    def on_problem_defined(self, problem):
        self.problem = problem

    def on_algorithm_selected(self, algorithm):
        self.algorithm = algorithm

    def on_training_completed(self, results):
        self.results_widget.display_results(results)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
