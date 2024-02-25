from PyQt5.uic import loadUi
from PyQt5 import QtWidgets


class ArticleMode(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        loadUi("game_view/frontend/article_mode.ui", self)

    def connect_der_button(self, function):
        self.der_button.clicked.connect(function)

    def connect_die_button(self, function):
        self.die_button.clicked.connect(function)

    def connect_das_button(self, function):
        self.das_button.clicked.connect(function)

    def connect_go_to_summary_button(self, function):
        self.go_to_summary_button.clicked.connect(function)

    def connect_open_database_button(self, function):
        self.open_database_button.clicked.connect(function)

    def read_user_answer(self) -> str:
        button_pressed = self.sender()

        if button_pressed == self.der_button:
            return "der"
        elif button_pressed == self.die_button:
            return "die"
        else:
            return "das"

    def enable_go_to_summary_button(self):
        self.title_label.setText("")
        self.stacked_buttons.setCurrentWidget(self.summary_page)

