from game_controller.controller import Controller
from game_model.game_mode.translation_game import TranslationGame

CORRECT = True
WRONG = False


class TranslationController(Controller):
    def __init__(self, ui_controller):
        super().__init__(ui_controller)
        self.game_model: TranslationGame = TranslationGame()

        self.connect_buttons()
        
    def start_game(self):
        self.ui_controller.set_translate_mode_window()
        self.ui_controller.translate_mode_window.stacked_buttons.setCurrentWidget(self.ui_controller.translate_mode_window.check_page)
        self.game_model.set_mode(self.ui_controller.select_language_window.read_selected_language())

        self.game_model.load_questions()

        text_to_show = f"<html>How do you translate <i>'{self.game_model.questions[0]}'</i> ? </html>"
        self.ui_controller.translate_mode_window.question_label.setText(text_to_show)
        
    def check_answer(self):
        user_answer = self.ui_controller.translate_mode_window.input_line_edit.text()
        self.ui_controller.translate_mode_window.reset_give_me_a_hint_button()

        if user_answer == self.game_model.answers[self.game_model.current_word]:
            result = "<html><font color='green'>Genau!</font></html>"
            self.ui_controller.translate_mode_window.solution_label.setText(result)
            self.game_model.score.update_partial_score()
            self.ui_controller.translation_summary_window.append_row_to_summary_table(
                self.game_model.questions[self.game_model.current_word],
                user_answer,
                self.game_model.answers[self.game_model.current_word],
                CORRECT
            )
            self.game_model.guessed_entries.append(True)
        else:
            result = f"<html><font color='red'>Wrong!</font> The correct answer was <i><font color='green'>'{self.game_model.answers[self.game_model.current_word]}'</font></i></html>"
            self.ui_controller.translate_mode_window.solution_label.setText(result)
            self.ui_controller.translation_summary_window.append_row_to_summary_table(
                self.game_model.questions[self.game_model.current_word],
                user_answer,
                self.game_model.answers[self.game_model.current_word],
                WRONG
            )
            self.game_model.guessed_entries.append(False)
        self.update_question()
        if self.game_model.current_word == self.game_model.QUESTIONS_PER_GAME:
            self.ui_controller.translate_mode_window.enable_go_to_summary_button()
            self.game_model.score.update_total_score()
            self.game_model.update_score_in_database()
                
    def update_question(self):
        self.game_model.update_current_word()
        if self.game_model.current_word < self.game_model.QUESTIONS_PER_GAME:
            text_to_show = f"<html>How do you translate <i>'{self.game_model.questions[self.game_model.current_word]}'</i> ? </html>"
            self.ui_controller.translate_mode_window.question_label.setText(text_to_show)
        self.ui_controller.translate_mode_window.input_line_edit.clear()

    def show_hint(self):
        current_word = self.game_model.answers[self.game_model.current_word]
        self.ui_controller.translate_mode_window.give_me_a_hint(current_word)

    def show_summary(self):
        self.ui_controller.stacked_widget.setCurrentWidget(self.ui_controller.translation_summary_window)
        #I don't like a lot the previous function, should it be higher level?
        self.ui_controller.translation_summary_window.show_score(
            self.game_model.score.partial_score,
            self.game_model.score.total_score,
            self.game_model.number_of_matches
        )
        self.ui_controller.translation_summary_window.adjust_table_height()

    def play_again(self):
        self.ui_controller.reset_user_interfaces()
        self.game_model.reset_game()
        
    def add_character(self):
        self.ui_controller.translate_mode_window.add_character()

    def open_database(self):
        self.ui_controller.set_previous_index(self.ui_controller.stacked_widget.currentIndex())
        self.ui_controller.database_window.show_translation_database()
        self.ui_controller.stacked_widget.setCurrentWidget(self.ui_controller.database_window)

    def connect_buttons(self):
        self.ui_controller.select_language_window.connect_german_to_italian_button(self.start_game)
        self.ui_controller.select_language_window.connect_italian_to_german_button(self.start_game)

        self.ui_controller.translate_mode_window.connect_add_character_button(self.add_character)
        self.ui_controller.translate_mode_window.connect_check_button(self.check_answer)
        self.ui_controller.translate_mode_window.connect_give_me_a_hint_button(self.show_hint)
        self.ui_controller.translate_mode_window.connect_go_to_summary_button(self.show_summary)
        self.ui_controller.translate_mode_window.connect_open_database_button(self.open_database)

        self.ui_controller.translation_summary_window.connect_play_again_button(self.play_again)
        self.ui_controller.translation_summary_window.connect_quit_button(self.ui_controller.quit_game)
        
