from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from random import randint

NUMBER_OF_COLUMNS = 4
NUMBER_OF_ROWS = 1
ROW_INDEX = 0

PRESENT = 0
PRÄTERITUM = 1
PERFEKT = 2
ITALIAN = 3


class VerbParadigmMode(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("game_view/frontend/verb_paradigm_mode.ui", self)
        self.go_to_summary_button.setVisible(False)

    def set_row_in_table(self, current_paradigm):
        given_entry_index = randint(0, 2)
        self.clear_entry_row()

        if given_entry_index == 0:
            self.paradigm_table.setItem(0, 0, QTableWidgetItem(current_paradigm[PRESENT]))
        elif given_entry_index == 1:
            self.paradigm_table.setItem(0, 1, QTableWidgetItem(current_paradigm[PRÄTERITUM]))
        else:
            self.paradigm_table.setItem(0, 2, QTableWidgetItem(current_paradigm[PERFEKT]))

        self.paradigm_table.setItem(0, 3, QTableWidgetItem(current_paradigm[ITALIAN]))

        return given_entry_index

    def add_character(self):
        current_item = self.paradigm_table.currentItem()
        if current_item is not None:
            current_text = current_item.text()
            character_to_add = self.character_combo_box.currentText()
            new_text = current_text + f"{character_to_add}"
            current_item.setText(new_text)

    def read_entries_in_table(self):
        row_data = []

        for col in range(self.paradigm_table.columnCount() - 1):
            item = self.paradigm_table.item(ROW_INDEX, col)
            if item is not None:
                item_text = item.text()
            else:
                item_text = ""

            row_data.append(item_text)

        return row_data

    def enable_go_to_summary_button(self):
        self.clear_entry_row()
        self.check_button.setVisible(False)
        self.go_to_summary_button.setVisible(True)

    def clear_entry_row(self):
        for col in range(self.paradigm_table.columnCount()):
            item = self.paradigm_table.takeItem(ROW_INDEX, col)
            if item:
                del item

    def connect_add_character_button(self, function):
        self.add_character_button.clicked.connect(function)

    def connect_check_button(self, function):
        self.check_button.clicked.connect(function)

    def connect_go_to_summary_button(self, function):
        self.go_to_summary_button.clicked.connect(function)

    def connect_open_database_button(self,function):
        self.open_database_button.clicked.connect(function)
