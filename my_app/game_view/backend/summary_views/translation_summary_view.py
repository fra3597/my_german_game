from math import floor
from PyQt5.QtWidgets import QWidget, QHeaderView, QPushButton
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QColor
from game_view.frontend.summary_views.translation_summary import Ui_TranslationSummary



NUMBER_OF_COLUMNS = 3
BUTTON_FONT_SIZE_TO_WIDTH_RATIO = 0.00875
TABLE_FONT_SIZE_TO_WIDTH_RATIO = 0.004375


class TranslationSummary(QWidget):
    def __init__(self, ):
        super().__init__()

        self.widget = Ui_TranslationSummary()
        self.widget.setupUi(self)

        self.model = QStandardItemModel(self)
        self.init_model()
        self.init_table()

    def init_model(self):
        self.model.setColumnCount(NUMBER_OF_COLUMNS)
        self.model.setHorizontalHeaderLabels(['Word to translate', 'Your Answer', 'Correct Answer'])
        self.widget.summary_table.setModel(self.model)

    def init_table(self):
        self.widget.summary_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.widget.summary_table.verticalHeader().hide()

    def connect_play_again_button(self, function):
        self.widget.play_again_button.clicked.connect(function)

    def connect_quit_button(self, function):
        self.widget.quit_button.clicked.connect(function)

    def append_row_to_summary_table(self, word_to_translate, user_answer, correct_answer, is_correct):
        word_to_translate = QStandardItem(word_to_translate)
        user_answer = QStandardItem(user_answer)
        correct_answer = QStandardItem(correct_answer)

        if is_correct:
            user_answer.setForeground(QColor("green"))
        else:
            user_answer.setForeground(QColor("red"))

        new_row = [word_to_translate, user_answer, correct_answer]
        self.model.appendRow(new_row)

    def show_score(self, partial_score, total_score, number_of_matches):
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

    # def resizeEvent(self, event):
    #     self.resize_buttons()
    #     self.resize_table()

    # def resize_buttons(self):
    #     for button in self.findChildren(QPushButton):
    #         new_font_size = floor(self.width() * BUTTON_FONT_SIZE_TO_WIDTH_RATIO)
    #         font = button.font()
    #         print(new_font_size)
    #         font.setPointSize(new_font_size)
    #         button.setFont(font)

    # def resize_table(self):
    #     # print(f"{current_font.pointSize() / self.width()}")
    #     new_font_size = floor(self.width() * TABLE_FONT_SIZE_TO_WIDTH_RATIO)
    #     new_row_height = self.height()
    #     for row in range(self.model.rowCount()):
    #         self.summary_table.setRowHeight(row, 40)
    #         for col in range(self.model.columnCount()):
    #             item = self.model.item(row, col)
    #             if item is not None:
    #                 current_font = item.font()
    #                 print(f"{current_font.pointSize()}")
    #                 print(new_font_size)
    #                 current_font.setPointSize(new_font_size)
    #                 item.setFont(current_font)

    #     #PRoblema font tabella troppo piccolo

    #     header = self.summary_table.horizontalHeader()
    #     header_font = header.font()
    #     header_font.setPointSize(new_font_size)
    #     header.setFont(header_font)

    #     self.adjust_table_height()

