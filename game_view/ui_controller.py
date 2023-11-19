from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from game_view.backend.select_game_view import SelectGameMode
from game_view.backend.select_language_view import SelectLanguage
from game_view.backend.translate_mode import TranslateMode
from game_view.backend.verb_paradigm_view import VerbParadigmMode
from game_view.backend.translation_summary_view import Summary
from game_view.backend.paradigm_summary_view import ParadigmSummary


class UIController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget(self)

        self.select_game_mode_window = SelectGameMode()
        self.select_language_window = SelectLanguage()
        self.translate_mode_window = TranslateMode()
        self.verb_paradigm_window = VerbParadigmMode()
        self.summary_window = Summary()
        self.paradigm_summary_window = ParadigmSummary()

        self.init_stacked_widget()
        self.init_select_game_mode_window_buttons()

    def set_translate_mode_window(self):
        self.stacked_widget.setCurrentWidget(self.translate_mode_window)

    def set_select_language_window(self):
        self.stacked_widget.setCurrentWidget(self.select_language_window)

    def set_verb_paradigm_window(self):
        self.stacked_widget.setCurrentWidget(self.verb_paradigm_window)

    def init_stacked_widget(self):
        self.setCentralWidget(self.stacked_widget)
        self.stacked_widget.setFixedHeight(800)
        self.stacked_widget.setFixedWidth(1000)

        self.stacked_widget.addWidget(self.select_game_mode_window)
        self.stacked_widget.addWidget(self.select_language_window)
        self.stacked_widget.addWidget(self.translate_mode_window)
        self.stacked_widget.addWidget(self.verb_paradigm_window)
        self.stacked_widget.addWidget(self.summary_window)
        self.stacked_widget.addWidget(self.paradigm_summary_window)

    def init_select_game_mode_window_buttons(self):
        self.select_game_mode_window.connect_translate_mode_button(self.set_select_language_window)

    def reset_user_interfaces(self):
        self.select_game_mode_window.welcome_game_label.setVisible(False)
        self.stacked_widget.setCurrentWidget(self.select_game_mode_window)
        self.translate_mode_window.solution_label.setText("")
        self.translate_mode_window.check_button.setVisible(True)
        self.translate_mode_window.give_me_a_hint_button.setVisible(True)
        self.translate_mode_window.go_to_summary_button.setVisible(False)
        self.summary_window.model.removeRows(0, self.summary_window.model.rowCount())




