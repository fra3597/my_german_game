from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from random import randint
from PyQt5.QtCore import Qt
from game_view.frontend.mode_views.verb_paradigm_mode import Ui_VerbParadigmMode

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

        self.widget = Ui_VerbParadigmMode()
        self.widget.setupUi(self)

        self.check_page_index = self.widget.stacked_buttons.currentIndex()

    def set_row_in_table(self, current_paradigm):
        given_entry_index = randint(0, 2)
        self.clear_entry_row()

        if given_entry_index == 0:
            self.widget.paradigm_table.setItem(0, 0, QTableWidgetItem(current_paradigm[PRESENT]))
        elif given_entry_index == 1:
            self.widget.paradigm_table.setItem(0, 1, QTableWidgetItem(current_paradigm[PRÄTERITUM]))
        else:
            self.widget.paradigm_table.setItem(0, 2, QTableWidgetItem(current_paradigm[PERFEKT]))

        self.widget.paradigm_table.setItem(0, 3, QTableWidgetItem(current_paradigm[ITALIAN]))

        return given_entry_index

    def add_character(self):
        current_item = self.widget.paradigm_table.currentItem()
        if current_item is not None:
            current_text = current_item.text()
            character_to_add = self.widget.character_combo_box.currentText()
            new_text = current_text + f"{character_to_add}"
            current_item.setText(new_text)

    def read_entries_in_table(self):
        row_data = []

        for col in range(self.widget.paradigm_table.columnCount() - 1):
            item = self.widget.paradigm_table.item(ROW_INDEX, col)
            if item is not None:
                item_text = item.text()
            else:
                item_text = ""

            row_data.append(item_text)

        return row_data

    def enable_go_to_summary_button(self):
        self.clear_entry_row()
        self.widget.stacked_buttons.setCurrentWidget(self.widget.summary_page)

    def clear_entry_row(self):
        for col in range(self.widget.paradigm_table.columnCount()):
            item = self.widget.paradigm_table.takeItem(ROW_INDEX, col)
            if item:
                del item

    def connect_add_character_button(self, function):
        self.widget.add_character_button_3.clicked.connect(function)

    def connect_check_button(self, function):
        self.widget.check_button.clicked.connect(function)

    def connect_go_to_summary_button(self, function):
        self.widget.go_to_summary_button.clicked.connect(function)

    def connect_open_database_button(self,function):
        self.widget.open_database_button.clicked.connect(function)

    #TO DO: this function has to be fixed. The currentIndex set at the init depends on th efirst page available when you save the .ui file
    def keyPressEvent(self, event):
        if event.key() in [Qt.Key_Return, Qt.Key_Enter]:
            if self.widget.stacked_buttons.currentIndex() == self.check_page_index:
                self.widget.check_button.click()
            else:
                self.widget.go_to_summary_button.click()
