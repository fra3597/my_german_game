from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from random import randint
from PyQt5.QtCore import Qt
from game_view.frontend.mode_views.verb_paradigm_mode import Ui_VerbParadigmMode

NUMBER_OF_COLUMNS: int = 4
NUMBER_OF_ROWS: int = 1
ROW_INDEX: int = 0

PRESENT: int = 0
PRÄTERITUM: int = 1
PERFEKT: int = 2
ITALIAN: int = 3


class VerbParadigmMode(QWidget):
    def __init__(self):
        super().__init__()

        self.widget: Ui_VerbParadigmMode = Ui_VerbParadigmMode()
        self.widget.setupUi(self)

        self.check_page_index: int = self.widget.stacked_buttons.currentIndex()

    def set_row_in_table(self, current_paradigm: list[str]) -> int:
        given_entry_index: int = randint(0, 2)
        self.clear_entry_row()

        if given_entry_index == 0:
            self.widget.paradigm_table.setItem(0, 0, QTableWidgetItem(current_paradigm[PRESENT]))
        elif given_entry_index == 1:
            self.widget.paradigm_table.setItem(0, 1, QTableWidgetItem(current_paradigm[PRÄTERITUM]))
        else:
            self.widget.paradigm_table.setItem(0, 2, QTableWidgetItem(current_paradigm[PERFEKT]))

        self.widget.paradigm_table.setItem(0, 3, QTableWidgetItem(current_paradigm[ITALIAN]))

        return given_entry_index

    def add_character(self) -> None:
        current_item: QTableWidgetItem = self.widget.paradigm_table.currentItem()
        
        if current_item is not None:
            current_text: str = current_item.text()
            character_to_add: str = self.widget.character_combo_box.currentText()
            new_text: str = current_text + f"{character_to_add}"
            current_item.setText(new_text)

    def read_entries_in_table(self) -> list[str]:
        row_data: list[str] = []

        for col in range(self.widget.paradigm_table.columnCount() - 1):
            item = self.widget.paradigm_table.item(ROW_INDEX, col)
            if item is not None:
                item_text = item.text()
            else:
                item_text = ""

            row_data.append(item_text)

        return row_data

    def enable_go_to_summary_button(self) -> None:
        self.clear_entry_row()
        self.widget.stacked_buttons.setCurrentWidget(self.widget.summary_page)

    def clear_entry_row(self) -> None:
        for col in range(self.widget.paradigm_table.columnCount()):
            item: QTableWidgetItem = self.widget.paradigm_table.takeItem(ROW_INDEX, col)
            if item:
                del item

    def connect_add_character_button(self, function) -> None:
        self.widget.add_character_button_3.clicked.connect(function)

    def connect_check_button(self, function) -> None:
        self.widget.check_button.clicked.connect(function)

    def connect_go_to_summary_button(self, function) -> None:
        self.widget.go_to_summary_button.clicked.connect(function)

    def connect_open_database_button(self,function) -> None:
        self.widget.open_database_button.clicked.connect(function)

    #TODO: this function has to be fixed. The currentIndex set at the init depends on th efirst page available when you save the .ui file
    def keyPressEvent(self, event) -> None:
        if event.key() in [Qt.Key_Return, Qt.Key_Enter]:
            if self.widget.stacked_buttons.currentIndex() == self.check_page_index:
                self.widget.check_button.click()
            else:
                self.widget.go_to_summary_button.click()
