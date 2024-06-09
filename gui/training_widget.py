from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QProgressBar, QTextEdit

class TrainingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.status_label = QLabel('Status: Não Treinando')
        self.progress_bar = QProgressBar()
        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)

        self.start_button = QPushButton('Iniciar Treinamento')
        self.start_button.clicked.connect(self.start_training)

        self.back_button = QPushButton('Voltar ao Menu Inicial')
        self.back_button.clicked.connect(self.back_to_menu)

        layout.addWidget(self.status_label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(QLabel('Log de Treinamento'))
        layout.addWidget(self.log_display)
        layout.addWidget(self.start_button)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def start_training(self):
        self.status_label.setText('Status: Treinando')
        self.progress_bar.setValue(0)
        self.log_display.append('Iniciando treinamento...')

        # Simular progresso de treinamento
        import time
        for i in range(1, 101):
            time.sleep(0.1)
            self.progress_bar.setValue(i)
            self.log_display.append(f'Progresso: {i}%')

        self.status_label.setText('Status: Treinamento Concluído')
        self.log_display.append('Treinamento concluído.')

    def back_to_menu(self):
        self.parentWidget().setCurrentIndex(0)
