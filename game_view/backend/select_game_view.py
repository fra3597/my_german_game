from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

GERMAN_TO_ITALIAN = 1
ITALIAN_TO_GERMAN = 2


class SelectGameMode(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        loadUi("game_view/frontend/select_game_mode.ui", self)

    def connect_translate_mode_button(self,function):
        self.translate_mode_button.clicked.connect(function)

    def connect_paradigm_mode_button(self,function):
        self.paradigm_mode_button.clicked.connect(function)

    def connect_article_mode_button(self, function):
        self.article_mode_button.clicked.connect(function)

