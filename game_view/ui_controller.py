from PyQt5.QtWidgets import QMainWindow, QStackedWidget, qApp
from game_view.backend.select_game_view import SelectGameMode
from game_view.backend.select_language_view import SelectLanguage
from game_view.backend.translate_mode_view import TranslateMode
from game_view.backend.paradigm_mode_view import ParadigmMode
from game_view.backend.article_mode_view import ArticleMode
from game_view.backend.database_view import DatabaseView
from game_view.backend.translation_summary_view import TranslationSummary
from game_view.backend.paradigm_summary_view import ParadigmSummary
from game_view.backend.article_summary_view import ArticleSummary


class UIController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget(self)

        self.select_game_mode_window = SelectGameMode()
        self.select_language_window = SelectLanguage()
        self.translate_mode_window = TranslateMode()
        self.verb_paradigm_window = ParadigmMode()
        self.article_mode_window = ArticleMode()
        self.database_window = DatabaseView()
        self.translation_summary_window = TranslationSummary()
        self.paradigm_summary_window = ParadigmSummary()
        self.article_summary_window = ArticleSummary()

        self.previous_index = None

        self.init_stacked_widget()
        self.init_select_game_mode_window_buttons()
        self.connect_go_back_button_database()

    def set_select_language_window(self):
        self.stacked_widget.setCurrentWidget(self.select_language_window)

    def set_translate_mode_window(self):
        self.stacked_widget.setCurrentWidget(self.translate_mode_window)

    def set_verb_paradigm_window(self):
        self.stacked_widget.setCurrentWidget(self.verb_paradigm_window)

    def set_article_mode_window(self):
        self.stacked_widget.setCurrentWidget(self.article_mode_window)

    def set_previous_window(self):
        current_index = self.stacked_widget.currentIndex()
        if current_index > 0:
            self.stacked_widget.setCurrentIndex(self.previous_index)

    def set_previous_index(self, previous_index):
        self.previous_index = previous_index

    def connect_go_back_button_database(self):
        self.database_window.connect_go_back_button(self.set_previous_window)

    def init_stacked_widget(self):
        self.setCentralWidget(self.stacked_widget)
        self.stacked_widget.setFixedHeight(800)
        self.stacked_widget.setFixedWidth(1000)

        self.stacked_widget.addWidget(self.select_game_mode_window)
        self.stacked_widget.addWidget(self.select_language_window)
        self.stacked_widget.addWidget(self.translate_mode_window)
        self.stacked_widget.addWidget(self.verb_paradigm_window)
        self.stacked_widget.addWidget(self.article_mode_window)
        self.stacked_widget.addWidget(self.database_window)
        self.stacked_widget.addWidget(self.translation_summary_window)
        self.stacked_widget.addWidget(self.paradigm_summary_window)
        self.stacked_widget.addWidget(self.article_summary_window)

    def init_select_game_mode_window_buttons(self):
        self.select_game_mode_window.connect_translate_mode_button(self.set_select_language_window)

    def reset_translation_mode_view(self):
        self.stacked_widget.setCurrentWidget(self.select_language_window)
        self.translate_mode_window.solution_label.setText("")
        self.translate_mode_window.check_button.setVisible(True)
        self.translate_mode_window.give_me_a_hint_button.setVisible(True)
        self.translate_mode_window.go_to_summary_button.setVisible(False)
        self.translation_summary_window.model.removeRows(0, self.summary_window.model.rowCount())

    def reset_paradigm_mode_view(self):
        self.stacked_widget.setCurrentWidget(self.verb_paradigm_window)
        self.verb_paradigm_window.check_button.setVisible(True)
        self.verb_paradigm_window.go_to_summary_button.setVisible(False)
        self.verb_paradigm_window.comparison_result_label.setText("")
        self.verb_paradigm_window.clear_entry_row()
        self.paradigm_summary_window.model.removeRows(0, self.paradigm_summary_window.model.rowCount())

    def reset_article_mode_view(self):
        self.stacked_widget.setCurrentWidget(self.article_mode_window)
        self.article_mode_window.der_button.setVisible(True)
        self.article_mode_window.die_button.setVisible(True)
        self.article_mode_window.das_button.setVisible(True)
        self.article_mode_window.go_to_summary_button.setVisible(False)
        self.article_mode_window.comparison_result_label.setText("")
        self.article_summary_window.model.removeRows(0, self.article_summary_window.model.rowCount())

    def quit_game(self):
        qApp.quit()
