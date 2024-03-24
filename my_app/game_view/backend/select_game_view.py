from PyQt5.QtWidgets import QWidget
from game_view.frontend.select_game_mode import Ui_SelectGameMode

GERMAN_TO_ITALIAN: int = 1
ITALIAN_TO_GERMAN: int = 2


class SelectGameMode(QWidget):
    def __init__(self):
        super().__init__()

        self.widget: Ui_SelectGameMode = Ui_SelectGameMode()
        self.widget.setupUi(self)

    def connect_translate_mode_button(self,function) -> None:
        self.widget.translate_mode_button.clicked.connect(function)

    def connect_paradigm_mode_button(self,function) -> None:
        self.widget.paradigm_mode_button.clicked.connect(function)

    def connect_article_mode_button(self, function) -> None:
        self.widget.article_mode_button.clicked.connect(function)

