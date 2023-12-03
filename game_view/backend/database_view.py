from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
import pandas
from game_model.question.translate_word import TranslationWord
from game_model.question.verb_paradigm import VerbParadigm
from game_model.question.article_word import ArticleWord

NUMBER_OF_COLUMNS_TRANSLATION = 3
NUMBER_OF_COLUMNS_PARADIGM = 4
NUMBER_OF_COLUMNS_ARTICLE = 4


class DatabaseView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        loadUi("game_view/frontend/database.ui", self)
        self.model = QtGui.QStandardItemModel(self)

    def connect_go_back_button(self, function):
        self.go_back_button.clicked.connect(function)

    def show_translation_database(self):
        headers = ['German Word', 'Italian Word', 'Score']
        self.set_up_table(NUMBER_OF_COLUMNS_TRANSLATION, headers)

        translation_database = pandas.read_csv("database/questions.csv")
        translation_database_dict = translation_database.to_dict(orient="records")

        for row in translation_database_dict:
            word = TranslationWord(row)

            german_item = QtGui.QStandardItem(word.german_word)
            italian_item = QtGui.QStandardItem(word.italian_word)

            score_item = QtGui.QStandardItem()
            score_item.setData(self.set_score_color(word.num_of_correct_guesses), QtCore.Qt.BackgroundRole)

            new_row = [german_item, italian_item, score_item]
            self.model.appendRow(new_row)

        self.title_label.setText("Translation Game Database")

    def show_paradigm_database(self):
        headers = ['Present', 'Präteritum', 'Perfekt', 'Italian']
        self.set_up_table(NUMBER_OF_COLUMNS_PARADIGM, headers)

        paradigm_database = pandas.read_csv("database/verb_paradigm_database.csv")
        paradigm_database_dict = paradigm_database.to_dict(orient="records")

        for row in paradigm_database_dict:
            paradigm = VerbParadigm(row)

            present_item = QtGui.QStandardItem(paradigm.present)
            present_item.setData(self.set_score_color(paradigm.present_score), QtCore.Qt.ForegroundRole)
            praeteritum_item = QtGui.QStandardItem(paradigm.praeteritum)
            praeteritum_item.setData(self.set_score_color(paradigm.praeteritum_score), QtCore.Qt.ForegroundRole)
            perfekt_item = QtGui.QStandardItem(paradigm.perfekt)
            perfekt_item.setData(self.set_score_color(paradigm.perfekt_score), QtCore.Qt.ForegroundRole)
            italian_item = QtGui.QStandardItem(paradigm.italian)

            new_row = [present_item, praeteritum_item, perfekt_item, italian_item]
            self.model.appendRow(new_row)

        self.title_label.setText("Verb Paradigm Game Database")

    def show_article_database(self):
        headers = ['Article', 'German Noun', 'Italian', 'Score']
        self.set_up_table(NUMBER_OF_COLUMNS_ARTICLE, headers)

        article_database = pandas.read_csv("database/words_with_article_database.csv")
        article_database_dict = article_database.to_dict(orient="records")

        for row in article_database_dict:
            word = ArticleWord(row)

            article_item = QtGui.QStandardItem(word.article)
            german_item = QtGui.QStandardItem(word.german_word)
            italian_item = QtGui.QStandardItem(word.italian_word)

            score_item = QtGui.QStandardItem()
            score_item.setData(self.set_score_color(word.num_of_correct_guesses), QtCore.Qt.BackgroundRole)

            new_row = [article_item, german_item, italian_item, score_item]
            self.model.appendRow(new_row)

        self.title_label.setText("Article Game Database")

    def set_up_table(self, num_of_columns, headers):
        self.model.setColumnCount(num_of_columns)
        self.model.setHorizontalHeaderLabels(headers)
        self.summary_table.setModel(self.model)
        self.summary_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.summary_table.verticalHeader().hide()
        self.summary_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def set_score_color(self, score):
        if score <= 2:
            return QtGui.QColor("red")
        elif score <= 4:
            return QtGui.QColor("orange")
        elif score <= 7:
            return QtGui.QColor("yellow")
        elif score <= 9:
            return QtGui.QColor("lightgreen")
        else:
            return QtGui.QColor("green")
