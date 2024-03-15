from PyQt5.QtWidgets import QWidget
from game_view.frontend.mode_views.article_mode import Ui_ArticleMode


class ArticleMode(QWidget):
    def __init__(self):
        super().__init__()

        self.widget = Ui_ArticleMode()
        self.widget.setupUi(self)

    def connect_der_button(self, function):
        self.widget.der_button.clicked.connect(function)

    def connect_die_button(self, function):
        self.widget.die_button.clicked.connect(function)

    def connect_das_button(self, function):
        self.widget.das_button.clicked.connect(function)

    def connect_go_to_summary_button(self, function):
        self.widget.go_to_summary_button.clicked.connect(function)

    def connect_open_database_button(self, function):
        self.widget.open_database_button.clicked.connect(function)

    def read_user_answer(self) -> str:
        button_pressed = self.sender()

        if button_pressed == self.widget.der_button:
            return "der"
        elif button_pressed == self.widget.die_button:
            return "die"
        else:
            return "das"

    def enable_go_to_summary_button(self):
        self.widget.title_label.setText("")
        self.widget.stacked_buttons.setCurrentWidget(self.widget.summary_page)

