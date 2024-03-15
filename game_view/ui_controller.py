from PyQt5.QtWidgets import QMainWindow, QStackedWidget, qApp
from game_view.backend.select_game_view import SelectGameMode
from game_view.backend.mode_views.select_language_view import SelectLanguage
from game_view.backend.mode_views.translate_mode_view import TranslateMode
from game_view.backend.mode_views.paradigm_mode_view import VerbParadigmMode
from game_view.backend.mode_views.article_mode_view import ArticleMode
from game_view.backend.database_view import DatabaseView
from game_view.backend.summary_views.translation_summary_view import TranslationSummary
from game_view.backend.summary_views.paradigm_summary_view import ParadigmSummary
from game_view.backend.summary_views.article_summary_view import ArticleSummary

MINIMUM_WIDTH = 1600
MINIMUM_HEIGHT = 1000


class UIController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget(self)

        #TODO: instantiate the objects only related to the chosen game mode

        self.select_game_mode_window = SelectGameMode()
        self.select_language_window = SelectLanguage()
        self.translate_mode_window = TranslateMode()
        self.verb_paradigm_window = VerbParadigmMode()
        self.article_mode_window = ArticleMode()
        self.translation_summary_window = TranslationSummary()
        self.paradigm_summary_window = ParadigmSummary()
        self.article_summary_window = ArticleSummary()
        self.previous_index = None

        self.init_stacked_widget()
        self.init_select_game_mode_window_buttons()

    def set_translate_mode_window(self):
        self.stacked_widget.setCurrentWidget(self.translate_mode_window)

    def set_select_language_window(self):
        self.stacked_widget.setCurrentWidget(self.select_language_window)

    def set_verb_paradigm_window(self):
        self.stacked_widget.setCurrentWidget(self.verb_paradigm_window)

    def set_article_mode_window(self):
        self.stacked_widget.setCurrentWidget(self.article_mode_window)

    def init_stacked_widget(self):
        self.setCentralWidget(self.stacked_widget)

        self.stacked_widget.addWidget(self.select_game_mode_window)
        self.stacked_widget.addWidget(self.select_language_window)
        self.stacked_widget.addWidget(self.translate_mode_window)
        self.stacked_widget.addWidget(self.verb_paradigm_window)
        self.stacked_widget.addWidget(self.article_mode_window)
        self.stacked_widget.addWidget(self.translation_summary_window)
        self.stacked_widget.addWidget(self.paradigm_summary_window)
        self.stacked_widget.addWidget(self.article_summary_window)

        self.stacked_widget.setMinimumSize(MINIMUM_WIDTH, MINIMUM_HEIGHT)
        self.stacked_widget.setStyleSheet("background-color: #83A2FF;")

    def init_select_game_mode_window_buttons(self):
        self.select_game_mode_window.connect_translate_mode_button(self.set_select_language_window)

    def reset_translate_mode(self):
        self.stacked_widget.setCurrentWidget(self.select_language_window)
        self.translate_mode_window.widget.solution_label.setText("")
        self.translate_mode_window.widget.stacked_buttons.setCurrentWidget(self.translate_mode_window.widget.check_page)
        self.translation_summary_window.model.removeRows(0, self.translation_summary_window.model.rowCount())

    def reset_paradigm_mode_view(self):
        self.stacked_widget.setCurrentWidget(self.verb_paradigm_window)
        self.verb_paradigm_window.widget.stacked_buttons.setCurrentWidget(self.verb_paradigm_window.widget.check_page)
        self.verb_paradigm_window.widget.comparison_result_label.setText("")
        self.verb_paradigm_window.clear_entry_row()
        self.paradigm_summary_window.model.removeRows(0, self.paradigm_summary_window.model.rowCount())

    def reset_article_mode_view(self):
        self.stacked_widget.setCurrentWidget(self.article_mode_window)
        self.article_mode_window.widget.stacked_buttons.setCurrentWidget(self.article_mode_window.widget.article_page)
        self.article_mode_window.widget.comparison_result_label.setText("")
        self.article_summary_window.model.removeRows(0, self.article_summary_window.model.rowCount())

    def set_previous_index(self, previous_index):
        self.previous_index = previous_index

    def set_previous_window(self):
        current_index = self.stacked_widget.currentIndex()
        if current_index > 0:
            self.stacked_widget.setCurrentIndex(self.previous_index)

    @staticmethod
    def quit_game():
        qApp.quit()
