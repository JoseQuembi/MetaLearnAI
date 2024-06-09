import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from gui.navigation_widget import NavigationWidget
from gui.problem_definition_widget import ProblemDefinitionWidget
from gui.algorithm_selection_widget import AlgorithmSelectionWidget
from gui.training_widget import TrainingWidget
from gui.results_widget import ResultsWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MetaLearnAI')

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.navigation_widget = NavigationWidget(self.stacked_widget)
        self.problem_definition_widget = ProblemDefinitionWidget()
        self.algorithm_selection_widget = AlgorithmSelectionWidget()
        self.training_widget = TrainingWidget()
        self.results_widget = ResultsWidget()

        self.stacked_widget.addWidget(self.navigation_widget)
        self.stacked_widget.addWidget(self.problem_definition_widget)
        self.stacked_widget.addWidget(self.algorithm_selection_widget)
        self.stacked_widget.addWidget(self.training_widget)
        self.stacked_widget.addWidget(self.results_widget)

        self.navigation_widget.navigate.connect(self.navigate)

    def navigate(self, index):
        self.stacked_widget.setCurrentIndex(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
