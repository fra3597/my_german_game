from PyQt5.QtWidgets import QWidget, QHeaderView, QAbstractItemView
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QColor
from PyQt5. QtCore import Qt
from game_model.question.translate_word import TranslationWord
from game_model.question.verb_paradigm import VerbParadigm
from game_model.question.article_word import ArticleWord
from game_view.frontend.database import Ui_Database
from database.database_handler import DatabaseHandler

NUMBER_OF_COLUMNS_TRANSLATION: int = 3
NUMBER_OF_COLUMNS_PARADIGM: int = 4
NUMBER_OF_COLUMNS_ARTICLE: int = 4


class DatabaseView(QWidget):
    def __init__(self, database_handler: DatabaseHandler):
        super().__init__()

        self.widget: Ui_Database = Ui_Database()
        self.widget.setupUi(self)

        self.db_handler: DatabaseHandler = database_handler

        self.model: QStandardItemModel = QStandardItemModel(self)

        self.widget.legend.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.widget.legend.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def connect_go_back_button(self, function) -> None:
        self.widget.go_back_button.clicked.connect(function)

    def show_translation_database(self) -> None:
        headers: list[str] = ['German Word', 'Italian Word', 'Score']
        self.set_up_table(NUMBER_OF_COLUMNS_TRANSLATION, headers)

        all_rows = self.db_handler.get_all_rows()

        for row in all_rows:
            word: TranslationWord = TranslationWord(row)

            german_item: QStandardItem = QStandardItem(word.german_word)
            italian_item: QStandardItem = QStandardItem(word.italian_word)
            score_item: QStandardItem = QStandardItem()
            score_item.setData(self.set_score_color(word.num_of_correct_guesses), Qt.BackgroundRole)

            new_row: list[QStandardItem] = [german_item, italian_item, score_item]
            self.model.appendRow(new_row)

        self.widget.title_label.setText("Translation Game Database")

    def show_paradigm_database(self) -> None:
        headers: list[str] = ['Present', 'Präteritum', 'Perfekt', 'Italian']
        self.set_up_table(NUMBER_OF_COLUMNS_PARADIGM, headers)

        all_rows = self.db_handler.get_all_rows()

        for row in all_rows:
            paradigm: VerbParadigm = VerbParadigm(row)

            present_item: QStandardItem = QStandardItem(paradigm.present)
            praeteritum_item: QStandardItem = QStandardItem(paradigm.praeteritum)
            perfekt_item: QStandardItem = QStandardItem(paradigm.perfekt)
            italian_item: QStandardItem = QStandardItem(paradigm.italian)

            present_item.setData(self.set_score_color(paradigm.present_score), Qt.ForegroundRole)
            praeteritum_item.setData(self.set_score_color(paradigm.praeteritum_score), Qt.ForegroundRole)
            perfekt_item.setData(self.set_score_color(paradigm.perfekt_score), Qt.ForegroundRole)

            new_row: list[QStandardItem] = [present_item, praeteritum_item, perfekt_item, italian_item]
            self.model.appendRow(new_row)

        self.widget.title_label.setText("Verb Paradigm Game Database")

    def show_article_database(self) -> None:
        headers: list[str] = ['Article', 'German Noun', 'Italian', 'Score']
        self.set_up_table(NUMBER_OF_COLUMNS_ARTICLE, headers)

        all_rows = self.db_handler.get_all_rows()

        for row in all_rows:
            word: ArticleWord = ArticleWord(row)

            article_item: QStandardItem = QStandardItem(word.article)
            german_item: QStandardItem = QStandardItem(word.german_word)
            italian_item: QStandardItem = QStandardItem(word.italian_word)
            score_item : QStandardItem = QStandardItem()
            
            score_item.setData(self.set_score_color(word.num_of_correct_guesses), Qt.BackgroundRole)

            new_row: list[QStandardItem] = [article_item, german_item, italian_item, score_item]
            self.model.appendRow(new_row)

        self.widget.title_label.setText("Article Game Database")

    def set_up_table(self, num_of_columns: int, headers: list[str]) -> None:
        self.model.setColumnCount(num_of_columns)
        self.model.setHorizontalHeaderLabels(headers)
        self.widget.summary_table.setModel(self.model)
        self.widget.summary_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.widget.summary_table.verticalHeader().hide()
        self.widget.summary_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def set_score_color(self, score) -> QColor:
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
