from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class TranslateMode(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        loadUi("game_view/frontend/translate_mode.ui", self)
        
        self.check_page_index = self.stacked_buttons.currentIndex()
        self.letters_shown = 0

    def connect_add_character_button(self, function):
        self.add_character_button.clicked.connect(function)

    def connect_check_button(self, function):
        self.check_button.clicked.connect(function)

    def connect_give_me_a_hint_button(self, function):
        self.give_me_a_hint_button.clicked.connect(function)

    def connect_go_to_summary_button(self, function):
        self.go_to_summary_button.clicked.connect(function)

    def connect_open_database_button(self, function):
        self.open_database_button.clicked.connect(function)

    def enable_go_to_summary_button(self):
        self.question_label.setText("")
        self.stacked_buttons.setCurrentWidget(self.summary_page)

    def give_me_a_hint(self, answers):
        if self.letters_shown < 3:
            current_text = self.input_line_edit.text()
            new_text = current_text + f"{answers[len(current_text)]}"
            self.input_line_edit.setText(new_text)
            if self.letters_shown == 2:
                self.give_me_a_hint_button.setStyleSheet("""background-color: rgba(255, 0, 0, 50);
                                                            border-radius: 20px;
                                                            """)
                self.give_me_a_hint_button.setEnabled(False)
        self.letters_shown += 1

    def add_character(self):
        current_text = self.input_line_edit.text()
        character_to_add = self.character_combo_box.currentText()
        new_text = current_text + f"{character_to_add}"
        self.input_line_edit.setText(new_text)

    def keyPressEvent(self, event):
        if  event.key() in [Qt.Key_Return, Qt.Key_Enter]:
            if self.stacked_buttons.currentIndex() == self.check_page_index:
                self.check_button.click()
            else:
                self.go_to_summary_button.click()

    def reset_give_me_a_hint_button(self):
        self.letters_shown = 0
        self.give_me_a_hint_button.setEnabled(True)
        self.give_me_a_hint_button.setStyleSheet("""QPushButton {
                                                        border-radius: 20px;	
                                                        background-color: #FFE3BB;}
                                                    QPushButton:hover {
                                                        background-color: #FFD28F;}
                                                    QPushButton:pressed {
                                                        background-color: #B4BDFF;}
                                                        """)
