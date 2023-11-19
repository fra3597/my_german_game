from game_controller.controller import Controller
from game_model.game_mode.paradigm_game import ParadigmGame

QUESTIONS_PER_GAME = 10

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

    def check_answer(self):
        is_correct = []
        tenses = ["Present", "Präteritum", "Perfekt"]
        text_to_show = ""

        user_answer = self.ui_controller.verb_paradigm_window.read_entries_in_table()
        is_correct = self.game_model.check_entry(user_answer)

        if self.game_model.current_word < QUESTIONS_PER_GAME:
            for index, entry in enumerate(user_answer):
                if is_correct[index] and index != self.game_model.given_entry_index:
                    text_to_show += f"<html>{tenses[index]}: <font color='green'>Genau!</font><br></html>"
                elif index == self.game_model.given_entry_index:
                    text_to_show += f"<html>{tenses[index]}: Given Entry<br></html>"
                else:
                    text_to_show += f"<html>{tenses[index]}: <font color='red'>Wrong!</font> The correct answer was <font color='green'>{self.game_model.current_paradigm[index]}</font><br></html>"

            self.ui_controller.verb_paradigm_window.comparison_result_label.setText(text_to_show)
            self.ui_controller.paradigm_summary_window.append_row_to_summary_table(user_answer,
                                                                                   self.game_model.current_paradigm,
                                                                                   is_correct,
                                                                                   self.game_model.given_entry_index)

        self.update_question()
        if self.game_model.current_word == QUESTIONS_PER_GAME:
            self.ui_controller.verb_paradigm_window.enable_go_to_summary_button()

    def update_question(self):
        self.game_model.update_current_word()
        if self.game_model.current_word < QUESTIONS_PER_GAME:
            self.game_model.set_current_paradigm()
            self.game_model.given_entry_index = self.ui_controller.verb_paradigm_window.set_row_in_table(
                self.game_model.current_paradigm)

    def show_summary(self):
        self.ui_controller.stacked_widget.setCurrentWidget(self.ui_controller.paradigm_summary_window)
        self.ui_controller.paradigm_summary_window.update_columns_width()

    def connect_buttons(self):
        self.ui_controller.select_game_mode_window.connect_paradigm_mode_button(self.start_verb_paradigm_mode)
        self.ui_controller.verb_paradigm_window.connect_check_button(self.check_answer)
        self.ui_controller.verb_paradigm_window.connect_go_to_summary_button(self.show_summary)
        self.ui_controller.paradigm_summary_window.connect_play_again_button(self.show_summary)
        self.ui_controller.paradigm_summary_window.connect_quit_button(self.ui_controller.paradigm_summary_window.quit_game)

