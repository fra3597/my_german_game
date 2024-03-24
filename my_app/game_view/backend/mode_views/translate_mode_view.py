from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from game_view.frontend.mode_views.translate_mode import Ui_TranslationMode



class TranslateMode(QWidget):
    def __init__(self):
        super().__init__()

        self.widget: Ui_TranslationMode = Ui_TranslationMode()
        self.widget.setupUi(self)
        
        self.check_page_index: int = self.widget.stacked_buttons.currentIndex()
        self.letters_shown: int = 0

    def connect_add_character_button(self, function) -> None:
        self.widget.add_character_button.clicked.connect(function)

    def connect_check_button(self, function) -> None:
        self.widget.check_button.clicked.connect(function)

    def connect_give_me_a_hint_button(self, function) -> None:
        self.widget.give_me_a_hint_button.clicked.connect(function)

    def connect_go_to_summary_button(self, function) -> None:
        self.widget.go_to_summary_button.clicked.connect(function)

    def connect_open_database_button(self, function) -> None:
        self.widget.open_database_button.clicked.connect(function)

    def enable_go_to_summary_button(self) -> None:
        self.widget.question_label.setText("")
        self.widget.stacked_buttons.setCurrentWidget(self.widget.summary_page)

    def give_me_a_hint(self, answer: str) -> None:
        if self.letters_shown < 3:
            current_text: str = self.widget.input_line_edit.text()
            new_text: str = current_text + f"{answer[len(current_text)]}"
            self.widget.input_line_edit.setText(new_text)
            if self.letters_shown == 2:
                self.widget.give_me_a_hint_button.setStyleSheet("""background-color: rgba(255, 0, 0, 50);
                                                            border-radius: 20px;
                                                            """)
                self.widget.give_me_a_hint_button.setEnabled(False)
        self.letters_shown += 1

    def add_character(self) -> None:
        current_text: str = self.widget.input_line_edit.text()
        character_to_add: str = self.widget.character_combo_box.currentText()
        new_text: str = current_text + f"{character_to_add}"
        self.widget.input_line_edit.setText(new_text)

    def keyPressEvent(self, event)  -> None:
        if  event.key() in [Qt.Key_Return, Qt.Key_Enter]:
            if self.widget.stacked_buttons.currentIndex() == self.check_page_index:
                self.widget.check_button.click()
            else:
                self.widget.go_to_summary_button.click()

    def reset_give_me_a_hint_button(self) -> None:
        self.letters_shown = 0
        self.widget.give_me_a_hint_button.setEnabled(True)
        self.widget.give_me_a_hint_button.setStyleSheet("""QPushButton {
                                                        border-radius: 20px;	
                                                        background-color: #FFE3BB;}
                                                    QPushButton:hover {
                                                        background-color: #FFD28F;}
                                                    QPushButton:pressed {
                                                        background-color: #B4BDFF;}
                                                        """)
