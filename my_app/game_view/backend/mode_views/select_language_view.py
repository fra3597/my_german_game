from PyQt5.QtWidgets import QWidget
from game_view.frontend.mode_views.select_language import Ui_SelectLanguage


GERMAN_TO_ITALIAN = 1
ITALIAN_TO_GERMAN = 2


class SelectLanguage(QWidget):
    def __init__(self):
        super().__init__()

        self.widget = Ui_SelectLanguage()
        self.widget.setupUi(self)

    def connect_german_to_italian_button(self,function):
        self.widget.german_to_italian_button.clicked.connect(function)

    def connect_italian_to_german_button(self,function):
        self.widget.italian_to_german_button.clicked.connect(function)

    def read_selected_language(self):
        button_pressed = self.sender()

        if button_pressed == self.widget.italian_to_german_button:
            return ITALIAN_TO_GERMAN
        else:
            return GERMAN_TO_ITALIAN
