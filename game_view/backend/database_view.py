from PyQt5.QtWidgets import QWidget, QHeaderView, QAbstractItemView
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QColor
from PyQt5. QtCore import Qt
from game_model.question.translate_word import TranslationWord
from game_model.question.verb_paradigm import VerbParadigm
from game_model.question.article_word import ArticleWord
from game_view.frontend.database import Ui_Database

NUMBER_OF_COLUMNS_TRANSLATION = 3
NUMBER_OF_COLUMNS_PARADIGM = 4
NUMBER_OF_COLUMNS_ARTICLE = 4


class DatabaseView(QWidget):
    def __init__(self, database_handler):
        super().__init__()

        self.widget = Ui_Database()
        self.widget.setupUi(self)

        self.db_handler = database_handler

        self.model = QStandardItemModel(self)

        self.widget.legend.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.widget.legend.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def connect_go_back_button(self, function):
        self.widget.go_back_button.clicked.connect(function)

    def show_translation_database(self):
        headers = ['German Word', 'Italian Word', 'Score']
        self.set_up_table(NUMBER_OF_COLUMNS_TRANSLATION, headers)

        all_rows = self.db_handler.get_all_rows()

        for row in all_rows:
            word = TranslationWord(row)

            german_item = QStandardItem(word.german_word)
            italian_item = QStandardItem(word.italian_word)
            score_item = QStandardItem()
            score_item.setData(self.set_score_color(word.num_of_correct_guesses), Qt.BackgroundRole)

            new_row = [german_item, italian_item, score_item]
            self.model.appendRow(new_row)

        self.widget.title_label.setText("Translation Game Database")

    def show_paradigm_database(self):
        headers = ['Present', 'Präteritum', 'Perfekt', 'Italian']
        self.set_up_table(NUMBER_OF_COLUMNS_PARADIGM, headers)

        all_rows = self.db_handler.get_all_rows()

        for row in all_rows:
            paradigm = VerbParadigm(row)

            present_item = QStandardItem(paradigm.present)
            present_item.setData(self.set_score_color(paradigm.present_score), Qt.ForegroundRole)
            praeteritum_item = QStandardItem(paradigm.praeteritum)
            praeteritum_item.setData(self.set_score_color(paradigm.praeteritum_score), Qt.ForegroundRole)
            perfekt_item = QStandardItem(paradigm.perfekt)
            perfekt_item.setData(self.set_score_color(paradigm.perfekt_score), Qt.ForegroundRole)
            italian_item = QStandardItem(paradigm.italian)

            new_row = [present_item, praeteritum_item, perfekt_item, italian_item]
            self.model.appendRow(new_row)

        self.widget.title_label.setText("Verb Paradigm Game Database")

    def show_article_database(self):
        headers = ['Article', 'German Noun', 'Italian', 'Score']
        self.set_up_table(NUMBER_OF_COLUMNS_ARTICLE, headers)

        all_rows = self.db_handler.get_all_rows()

        for row in all_rows:
            word = ArticleWord(row)

            article_item = QStandardItem(word.article)
            german_item = QStandardItem(word.german_word)
            italian_item = QStandardItem(word.italian_word)

            score_item = QStandardItem()
            score_item.setData(self.set_score_color(word.num_of_correct_guesses), Qt.BackgroundRole)

            new_row = [article_item, german_item, italian_item, score_item]
            self.model.appendRow(new_row)

        self.widget.title_label.setText("Article Game Database")

    def set_up_table(self, num_of_columns: int, headers: list[str]):
        self.model.setColumnCount(num_of_columns)
        self.model.setHorizontalHeaderLabels(headers)
        self.widget.summary_table.setModel(self.model)
        self.widget.summary_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.widget.summary_table.verticalHeader().hide()
        self.widget.summary_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def set_score_color(self, score):
        if score <= 2:
            return QColor("red")
        elif score <= 4:
            return QColor("orange")
        elif score <= 7:
            return QColor("yellow")
        elif score <= 9:
            return QColor("lightgreen")
        else:
            return QColor("green")
