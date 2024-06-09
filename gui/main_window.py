import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QStackedWidget

from gui.navigation_widget import NavigationWidget
from gui.problem_definition_widget import ProblemDefinitionWidget
from gui.algorithm_selection_widget import AlgorithmSelectionWidget
from gui.training_widget import TrainingWidget
from gui.results_widget import ResultsWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('MetaLearnAI Interface Gráfica')

        self.stack = QStackedWidget()
        self.navigation_widget = NavigationWidget()
        self.problem_widget = ProblemDefinitionWidget()
        self.algorithm_widget = AlgorithmSelectionWidget()
        self.training_widget = TrainingWidget()
        self.results_widget = ResultsWidget()

        self.stack.addWidget(self.problem_widget)
        self.stack.addWidget(self.algorithm_widget)
        self.stack.addWidget(self.training_widget)
        self.stack.addWidget(self.results_widget)

        layout = QVBoxLayout()
        layout.addWidget(self.navigation_widget)
        layout.addWidget(self.stack)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.navigation_widget.navigateToProblemDefinition.connect(self.show_problem_definition)
        self.navigation_widget.navigateToAlgorithmSelection.connect(self.show_algorithm_selection)
        self.navigation_widget.navigateToTraining.connect(self.show_training)
        self.navigation_widget.navigateToResults.connect(self.show_results)

    def show_problem_definition(self):
        self.stack.setCurrentWidget(self.problem_widget)

    def show_algorithm_selection(self):
        self.stack.setCurrentWidget(self.algorithm_widget)

    def show_training(self):
        self.stack.setCurrentWidget(self.training_widget)

    def show_results(self):
        self.stack.setCurrentWidget(self.results_widget)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
