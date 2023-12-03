from game_controller.controller import Controller
from game_model.game_mode.paradigm_game import ParadigmGame

GIVEN = 0
CORRECT = 1
WRONG = 2


class ParadigmController(Controller):
    def __init__(self, ui_controller):
        super().__init__(ui_controller)
        self.game_model = ParadigmGame()
        
        self.connect_buttons()
     
    def start_verb_paradigm_mode(self):
        self.ui_controller.set_verb_paradigm_window()

        self.game_model.load_questions_paradigm()
        self.game_model.set_current_paradigm()

        self.game_model.given_entry_index = self.ui_controller.verb_paradigm_window.set_row_in_table(
            self.game_model.current_paradigm)

    def add_character(self):
        self.ui_controller.verb_paradigm_window.add_character()

    def check_answer(self):
        is_correct = []
        tenses = ["Present", "Praeteritum", "Perfekt"]
        text_to_show = ""

        user_answer = self.ui_controller.verb_paradigm_window.read_entries_in_table()
        is_correct = self.game_model.check_entry(user_answer)

        current_guesses = []

        for index, entry in enumerate(user_answer):
            if is_correct[index] and index != self.game_model.given_entry_index:
                text_to_show += f"<html>{tenses[index]}: <font color='green'>Genau!</font><br></html>"
                current_guesses.append(True)
            elif index == self.game_model.given_entry_index:
                text_to_show += f"<html>{tenses[index]}: Given Entry<br></html>"
                current_guesses.append(False)
            else:
                text_to_show += f"<html>{tenses[index]}: <font color='red'>Wrong!</font> The correct answer was <font color='green'>{self.game_model.current_paradigm[index]}</font><br></html>"
                current_guesses.append(False)

        self.game_model.guessed_entries.append(current_guesses)
        self.ui_controller.verb_paradigm_window.comparison_result_label.setText(text_to_show)
        self.ui_controller.paradigm_summary_window.append_row_to_summary_table(user_answer,
                                                                               self.game_model.current_paradigm,
                                                                               is_correct,
                                                                               self.game_model.given_entry_index)

        self.update_question()
        if self.game_model.current_word == self.game_model.QUESTIONS_PER_GAME:
            self.ui_controller.verb_paradigm_window.enable_go_to_summary_button()
            self.update_final_score()
            self.game_model.update_score_in_database()

    def update_question(self):
        self.game_model.update_current_word()
        if self.game_model.current_word < self.game_model.QUESTIONS_PER_GAME:
            self.game_model.set_current_paradigm()
            self.game_model.given_entry_index = self.ui_controller.verb_paradigm_window.set_row_in_table(
                self.game_model.current_paradigm)

    def show_summary(self):
        self.ui_controller.stacked_widget.setCurrentWidget(self.ui_controller.paradigm_summary_window)

    def update_final_score(self):
        self.game_model.score.update_total_score()
        self.game_model.score.update_total_counter()
        present_partial_score = f"Present: Partial Score: {self.game_model.score.present_partial_score}/{self.game_model.score.present_partial_counter}\n"
        praeteritum_partial_score = f"Präteritum: Partial Score: {self.game_model.score.praeteritum_partial_score}/{self.game_model.score.praeteritum_partial_counter}\n"
        perfekt_partial_score = f"Perfekt: Partial Score: {self.game_model.score.perfekt_partial_score}/{self.game_model.score.perfekt_partial_counter}\n"

        text_to_show = present_partial_score + praeteritum_partial_score + perfekt_partial_score
        self.ui_controller.paradigm_summary_window.partial_score_label.setText(text_to_show)

        present_total_score = f"Total Score: {self.game_model.score.present_total_score}/{self.game_model.score.present_total_counter}\n"
        praeteritum_total_score = f"Total Score: {self.game_model.score.praeteritum_total_score}/{self.game_model.score.praeteritum_total_counter}\n"
        perfekt_total_score = f"Total Score: {self.game_model.score.perfekt_total_score}/{self.game_model.score.perfekt_total_counter}\n"

        text_to_show = present_total_score + praeteritum_total_score + perfekt_total_score
        self.ui_controller.paradigm_summary_window.total_score_label.setText(text_to_show)

    def open_database(self):
        self.ui_controller.set_previous_index(self.ui_controller.stacked_widget.currentIndex())
        self.ui_controller.database_window.show_paradigm_database()
        self.ui_controller.stacked_widget.setCurrentWidget(self.ui_controller.database_window)

    def play_again(self):
        self.ui_controller.reset_paradigm_mode_view()
        self.game_model.reset_game()
        self.start_verb_paradigm_mode()

    def connect_buttons(self):
        self.ui_controller.select_game_mode_window.connect_paradigm_mode_button(self.start_verb_paradigm_mode)

        self.ui_controller.verb_paradigm_window.connect_add_character_button(self.add_character)
        self.ui_controller.verb_paradigm_window.connect_check_button(self.check_answer)
        self.ui_controller.verb_paradigm_window.connect_go_to_summary_button(self.show_summary)
        self.ui_controller.verb_paradigm_window.connect_open_database_button(self.open_database)

        self.ui_controller.paradigm_summary_window.connect_play_again_button(self.play_again)
        self.ui_controller.paradigm_summary_window.connect_quit_button(self.ui_controller.quit_game)

