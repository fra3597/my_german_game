from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QPushButton
from math import floor


NUMBER_OF_COLUMNS = 3
BUTTON_FONT_SIZE_TO_WIDTH_RATIO = 0.00875
TABLE_FONT_SIZE_TO_WIDTH_RATIO = 0.004375


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

    def adjust_table_height(self):
        new_table_height = 0
        bottom_margin = 0
        EXTRA_HEIGHT = 20

        initial_layout_geometry = self.table_layout.geometry()
        initial_height = initial_layout_geometry.height()

        num_of_rows = self.model.rowCount()

        for row in range(num_of_rows):
            new_table_height += self.summary_table.rowHeight(row)

        new_table_height += self.summary_table.horizontalHeader().height()

        if initial_height > new_table_height:
            bottom_margin = abs(new_table_height - initial_height) - EXTRA_HEIGHT

        self.table_layout.setContentsMargins(0, 0, 0, bottom_margin)

    def resizeEvent(self, event):
        self.resize_buttons()
        self.resize_table()

    def resize_buttons(self):
        for button in self.findChildren(QPushButton):
            new_font_size = floor(self.width() * BUTTON_FONT_SIZE_TO_WIDTH_RATIO)
            font = button.font()
            print(new_font_size)
            font.setPointSize(new_font_size)
            button.setFont(font)

    def resize_table(self):
        # print(f"{current_font.pointSize() / self.width()}")
        new_font_size = floor(self.width() * TABLE_FONT_SIZE_TO_WIDTH_RATIO)
        new_row_height = self.height()
        for row in range(self.model.rowCount()):
            self.summary_table.setRowHeight(row, 40)
            for col in range(self.model.columnCount()):
                item = self.model.item(row, col)
                if item is not None:
                    current_font = item.font()
                    print(f"{current_font.pointSize()}")
                    print(new_font_size)
                    current_font.setPointSize(new_font_size)
                    item.setFont(current_font)

        #PRoblema font tabella troppo piccolo

        header = self.summary_table.horizontalHeader()
        header_font = header.font()
        header_font.setPointSize(new_font_size)
        header.setFont(header_font)

        self.adjust_table_height()

