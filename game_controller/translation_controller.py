from game_controller.controller import Controller
from database.database_handler import DatabaseHandler
from game_model.game_mode.translation_game import TranslationGame
from game_view.backend.mode_views.select_language_view import SelectLanguage
from game_view.backend.mode_views.translate_mode_view import TranslateMode
from game_view.backend.summary_views.translation_summary_view import TranslationSummary
from game_view.backend.database_view import DatabaseView

TABLE_NAME = "Questions"
FILENAME_DB = "database/questions.db"

CORRECT = True
WRONG = False

class TranslationController(Controller):
    def __init__(self, ui_controller):
        super().__init__(ui_controller)

        self.db_handler = DatabaseHandler(db_path=FILENAME_DB, table_name=TABLE_NAME)

        self.game_model: TranslationGame = TranslationGame(self.db_handler)

        self.select_language_window = SelectLanguage()
        self.translate_mode_window = TranslateMode()       
        self.translation_summary_window = TranslationSummary()
        self.database_window = DatabaseView(self.db_handler)
        self.ui_controller.stacked_widget.addWidget(self.select_language_window)
        self.ui_controller.stacked_widget.addWidget(self.translate_mode_window)
        self.ui_controller.stacked_widget.addWidget(self.translation_summary_window)
        self.ui_controller.stacked_widget.addWidget(self.database_window)

        self.connect_buttons()

    def set_select_language_window(self):
        self.ui_controller.stacked_widget.setCurrentWidget(self.select_language_window)

    def set_translate_mode_window(self):
        self.ui_controller.stacked_widget.setCurrentWidget(self.translate_mode_window)
        
    def start_game(self):
        self.set_translate_mode_window()
        self.translate_mode_window.widget.stacked_buttons.setCurrentWidget(self.translate_mode_window.widget.check_page)
        self.game_model.set_mode(self.select_language_window.read_selected_language())

        self.game_model.load_questions()

        text_to_show = f"<html>How do you translate <i>'{self.game_model.questions[0]}'</i> ? </html>"
        self.translate_mode_window.widget.question_label.setText(text_to_show)
        
    def check_answer(self):
        user_answer = self.translate_mode_window.widget.input_line_edit.text()
        self.translate_mode_window.reset_give_me_a_hint_button()

        if user_answer == self.game_model.answers[self.game_model.current_word]:
            result = "<html><font color='green'>Genau!</font></html>"
            self.translate_mode_window.widget.solution_label.setText(result)
            self.game_model.score.update_partial_score()
            self.translation_summary_window.append_row_to_summary_table(
                self.game_model.questions[self.game_model.current_word],
                user_answer,
                self.game_model.answers[self.game_model.current_word],
                CORRECT
            )
            self.game_model.guessed_entries.append(True)
        else:
            result = f"<html><font color='red'>Wrong!</font> The correct answer was <i><font color='green'>'{self.game_model.answers[self.game_model.current_word]}'</font></i></html>"
            self.translate_mode_window.widget.solution_label.setText(result)
            self.translation_summary_window.append_row_to_summary_table(
                self.game_model.questions[self.game_model.current_word],
                user_answer,
                self.game_model.answers[self.game_model.current_word],
                WRONG
            )
            self.game_model.guessed_entries.append(False)
        self.update_question()
        if self.game_model.current_word == self.game_model.QUESTIONS_PER_GAME:
            self.translate_mode_window.enable_go_to_summary_button()
            self.game_model.score.update_total_score()
            self.game_model.update_score_in_database()
                
    def update_question(self):
        self.game_model.update_current_word()
        if self.game_model.current_word < self.game_model.QUESTIONS_PER_GAME:
            text_to_show = f"<html>How do you translate <i>'{self.game_model.questions[self.game_model.current_word]}'</i> ? </html>"
            self.translate_mode_window.widget.question_label.setText(text_to_show)
        self.translate_mode_window.widget.input_line_edit.clear()

    def show_hint(self):
        current_word = self.game_model.answers[self.game_model.current_word]
        self.translate_mode_window.give_me_a_hint(current_word)

    def show_summary(self):
        self.ui_controller.stacked_widget.setCurrentWidget(self.translation_summary_window)
        #I don't like a lot the previous function, should it be higher level?
        self.translation_summary_window.show_score(
            self.game_model.score.partial_score,
            self.game_model.score.total_score,
            self.game_model.number_of_matches
        )
        self.translation_summary_window.adjust_table_height()
        
    def add_character(self):
        self.translate_mode_window.add_character()

    def open_database(self):
        self.ui_controller.set_previous_index(self.ui_controller.stacked_widget.currentIndex())
        self.database_window.show_translation_database()
        self.ui_controller.stacked_widget.setCurrentWidget(self.database_window)

    def reset_translate_mode(self):
        self.ui_controller.stacked_widget.setCurrentWidget(self.select_language_window)
        self.translate_mode_window.widget.solution_label.setText("")
        self.translate_mode_window.widget.stacked_buttons.setCurrentWidget(self.translate_mode_window.widget.check_page)
        self.translation_summary_window.model.removeRows(0, self.translation_summary_window.model.rowCount())

    def play_again(self):
        self.reset_translate_mode()
        self.game_model.reset_game()

    def connect_buttons(self):
        self.ui_controller.select_game_mode_window.connect_translate_mode_button(self.set_select_language_window)

        self.select_language_window.connect_german_to_italian_button(self.start_game)
        self.select_language_window.connect_italian_to_german_button(self.start_game)

        self.translate_mode_window.connect_add_character_button(self.add_character)
        self.translate_mode_window.connect_check_button(self.check_answer)
        self.translate_mode_window.connect_give_me_a_hint_button(self.show_hint)
        self.translate_mode_window.connect_go_to_summary_button(self.show_summary)
        self.translate_mode_window.connect_open_database_button(self.open_database)

        self.translation_summary_window.connect_play_again_button(self.play_again)
        self.translation_summary_window.connect_quit_button(self.ui_controller.quit_game)

        self.database_window.connect_go_back_button(self.ui_controller.set_previous_window)

        
