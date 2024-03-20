from PyQt5.QtWidgets import QWidget, QHeaderView, qApp
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QColor
from game_view.frontend.summary_views.article_summary import Ui_ArticleSummary


NUMBER_OF_COLUMNS = 4


class ArticleSummary(QWidget):
    def __init__(self):
        super().__init__()

        self.widget = Ui_ArticleSummary()
        self.widget.setupUi(self)

        self.model = QStandardItemModel(self)
        self.init_model()
        self.init_table()

    def init_model(self):
        self.model.setColumnCount(NUMBER_OF_COLUMNS)
        self.model.setHorizontalHeaderLabels(['User', 'Correct', 'German', 'Italian'])
        self.widget.summary_table.setModel(self.model)

    def init_table(self):
        self.widget.summary_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.widget.summary_table.verticalHeader().hide()

    def connect_play_again_button(self, function):
        self.widget.play_again_button.clicked.connect(function)

    def connect_quit_button(self, function):
        self.widget.quit_button.clicked.connect(function)

    def append_row_to_summary_table(self, user_answer: str, correct_article: str, german_word: str, italian_word: str, is_correct: bool):
        correct_article_item = QStandardItem(correct_article)
        user_answer_item = QStandardItem(user_answer)
        german_word_item = QStandardItem(german_word)
        italian_word_item = QStandardItem(italian_word)

        if is_correct:
            user_answer_item.setForeground(QColor("green"))
        else:
            user_answer_item.setForeground(QColor("red"))

        new_row = [user_answer, correct_article, german_word, italian_word]
        new_row = [user_answer_item, correct_article_item, german_word_item, italian_word_item]
        self.model.appendRow(new_row)

    def show_score(self, partial_score: int, total_score: int, number_of_matches: int):
        text_to_show = f"Your Partial Score: {partial_score}/10\nYour Total Score: {total_score}/{10*number_of_matches}"
        self.widget.score_label.setText(text_to_show)

    def adjust_table_height(self):
        new_table_height = 0
        bottom_margin = 0
        EXTRA_HEIGHT = 20

        initial_layout_geometry = self.widget.table_layout.geometry()
        initial_height = initial_layout_geometry.height()

        num_of_rows = self.model.rowCount()

        for row in range(num_of_rows):
            new_table_height += self.widget.summary_table.rowHeight(row)

        new_table_height += self.widget.summary_table.horizontalHeader().height()

        if initial_height > new_table_height:
            bottom_margin = abs(new_table_height - initial_height) - EXTRA_HEIGHT

        self.widget.table_layout.setContentsMargins(0, 0, 0, bottom_margin)