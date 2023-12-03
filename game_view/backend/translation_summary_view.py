from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui

NUMBER_OF_COLUMNS = 3


class TranslationSummary(QtWidgets.QWidget):
    def __init__(self, ):
        super().__init__()
        loadUi("game_view/frontend/summary.ui", self)

        self.model = QtGui.QStandardItemModel(self)
        self.init_model()
        self.init_table()

    def init_model(self):
        self.model.setColumnCount(NUMBER_OF_COLUMNS)
        self.model.setHorizontalHeaderLabels(['Word to translate', 'Your Answer', 'Correct Answer'])
        self.summary_table.setModel(self.model)

    def init_table(self):
        self.summary_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.summary_table.verticalHeader().hide()

    def connect_play_again_button(self, function):
        self.play_again_button.clicked.connect(function)

    def connect_quit_button(self, function):
        self.quit_button.clicked.connect(function)

    def append_row_to_summary_table(self, word_to_translate, user_answer, correct_answer, is_correct):
        word_to_translate = QtGui.QStandardItem(word_to_translate)
        user_answer = QtGui.QStandardItem(user_answer)
        correct_answer = QtGui.QStandardItem(correct_answer)

        if is_correct:
            user_answer.setForeground(QtGui.QColor("green"))
        else:
            user_answer.setForeground(QtGui.QColor("red"))

        new_row = [word_to_translate, user_answer, correct_answer]
        self.model.appendRow(new_row)

    def show_score(self, partial_score, total_score, number_of_matches):
        text_to_show = f"Your Partial Score: {partial_score}/10\nYour Total Score: {total_score}/{10*number_of_matches}"
        self.score_label.setText(text_to_show)
