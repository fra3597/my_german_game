from PyQt5.QtWidgets import QMainWindow, QStackedWidget, qApp
from game_view.backend.select_game_view import SelectGameMode

MINIMUM_WIDTH = 1600
MINIMUM_HEIGHT = 1000


class UIController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget(self)

        self.select_game_mode_window = SelectGameMode()
        self.previous_index = None

        self.init_stacked_widget()

    def init_stacked_widget(self):
        self.setCentralWidget(self.stacked_widget)

        self.stacked_widget.addWidget(self.select_game_mode_window)

        self.stacked_widget.setMinimumSize(MINIMUM_WIDTH, MINIMUM_HEIGHT)
        self.stacked_widget.setStyleSheet("background-color: #83A2FF;")

    def set_previous_index(self, previous_index):
        self.previous_index = previous_index

    def set_previous_window(self):
        current_index = self.stacked_widget.currentIndex()
        if current_index > 0:
            self.stacked_widget.setCurrentIndex(self.previous_index)

    @staticmethod
    def quit_game():
        qApp.quit()
