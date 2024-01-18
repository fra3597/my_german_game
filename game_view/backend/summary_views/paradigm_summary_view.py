from PyQt5.uic import loadUi
# Import only what yuo need, not everything
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QColor, QFont

NUMBER_OF_COLUMNS = 4
NUMBER_OF_ROWS = 2


class ParadigmSummary(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        loadUi("game_view/frontend/paradigm_summary.ui", self)

        self.model = QStandardItemModel(self)
        self.init_model()
        self.init_table()

    def init_model(self):
        self.model.setColumnCount(NUMBER_OF_COLUMNS)
        #Think about setting the tenses list as an attribute
        self.model.setHorizontalHeaderLabels(['Present', 'Präteritum', 'Perfekt', 'Italian'])
        self.summary_table.setModel(self.model)

    def init_table(self):
        #self.summary_table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.summary_table.verticalHeader().setMaximumWidth(100)
        self.summary_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def connect_play_again_button(self, function):
        self.play_again_button.clicked.connect(function)

    def connect_quit_button(self, function):
        self.quit_button.clicked.connect(function)

    def append_row_to_summary_table(self, user_answer, current_paradigm, is_correct, given_entry_index):
        user_answer_item = []
        current_paradigm_item = []

        for answer in user_answer:
            user_answer_item.append(QStandardItem(answer))
        for verb in current_paradigm:
            current_paradigm_item.append(QStandardItem(verb))

        for index, element in enumerate(is_correct):
            if element and index != given_entry_index:
                user_answer_item[index].setForeground(QColor("green"))
            elif not element and index != given_entry_index:
                user_answer_item[index].setForeground(QColor("red"))

        new_row = current_paradigm_item
        self.model.appendRow(new_row)
        new_row = user_answer_item
        self.model.appendRow(new_row)

        self.model.setVerticalHeaderItem(self.model.rowCount() - 2, QStandardItem("Paradigm"))
        self.model.setVerticalHeaderItem(self.model.rowCount() - 1, QStandardItem("User Answer"))

    #Is it working?
    def update_columns_width(self):
        for col in range(NUMBER_OF_COLUMNS):
            max_width = 0
            for row in range(self.model.rowCount()):
                item = self.model.item(row, col)
                if item and len(item.text()) > max_width:
                    max_width = len(item.text())

            self.summary_table.setColumnWidth(col, max_width)

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

    def quit_game(self):
        QtWidgets.qApp.quit()
