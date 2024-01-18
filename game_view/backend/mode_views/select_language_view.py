from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

GERMAN_TO_ITALIAN = 1
ITALIAN_TO_GERMAN = 2


class SelectLanguage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        loadUi("game_view/frontend/select_language.ui", self)

    def connect_german_to_italian_button(self,function):
        self.german_to_italian_button.clicked.connect(function)

    def connect_italian_to_german_button(self,function):
        self.italian_to_german_button.clicked.connect(function)

    def read_selected_language(self):
        button_pressed = self.sender()

        if button_pressed == self.italian_to_german_button:
            return ITALIAN_TO_GERMAN
        else:
            return GERMAN_TO_ITALIAN
