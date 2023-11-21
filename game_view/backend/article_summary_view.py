from PyQt5.uic import loadUi
# Import only what yuo need, not everything
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QColor

NUMBER_OF_COLUMNS = 4


class ArticleSummary(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        loadUi("game_view/frontend/article_summary.ui", self)

        self.model = QStandardItemModel(self)
        self.init_model()
        self.init_table()

    def init_model(self):
        self.model.setColumnCount(NUMBER_OF_COLUMNS)
        self.model.setHorizontalHeaderLabels(['User', 'Correct', 'German', 'Italian'])
        self.summary_table.setModel(self.model)

    def init_table(self):
        #self.summary_table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.summary_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.summary_table.verticalHeader().hide()

    def connect_play_again_button(self, function):
        self.play_again_button.clicked.connect(function)

    def connect_quit_button(self, function):
        self.quit_button.clicked.connect(function)

    def append_row_to_summary_table(self, correct_article, user_answer, german_word, italian_word, is_correct):
        correct_article = QStandardItem(correct_article)
        user_answer = QStandardItem(user_answer)
        german_word = QStandardItem(german_word)
        italian_word = QStandardItem(italian_word)

        if is_correct:
            user_answer.setForeground(QColor("green"))
        else:
            user_answer.setForeground(QColor("red"))

        new_row = [correct_article, user_answer, german_word, italian_word]
        self.model.appendRow(new_row)

    def show_score(self, partial_score, total_score, number_of_matches):
        text_to_show = f"Your Partial Score: {partial_score}/10\nYour Total Score: {total_score}/{10*number_of_matches}"
        self.score_label.setText(text_to_show)

    def quit_game(self):
        QtWidgets.qApp.quit()