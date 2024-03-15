from math import floor
from game_controller.controller import Controller
from database.database_handler import DatabaseHandler
from game_model.game_mode.paradigm_game import ParadigmGame
from game_view.backend.mode_views.paradigm_mode_view import VerbParadigmMode
from game_view.backend.summary_views.paradigm_summary_view import ParadigmSummary
from game_view.backend.database_view import DatabaseView

FILENAME_DB = "database/verb_paradigms.db"
TABLE_NAME = "VerbParadigms"

GIVEN = 0
CORRECT = 1
WRONG = 2


class ParadigmController(Controller):
    def __init__(self, ui_controller):
        super().__init__(ui_controller)

        self.db_handler = DatabaseHandler(db_path=FILENAME_DB, table_name=TABLE_NAME)

        self.game_model: ParadigmGame = ParadigmGame(self.db_handler)

        self.verb_paradigm_window = VerbParadigmMode()
        self.paradigm_summary_window = ParadigmSummary()
        self.database_window = DatabaseView(self.db_handler)
        self.ui_controller.stacked_widget.addWidget(self.verb_paradigm_window)
        self.ui_controller.stacked_widget.addWidget(self.paradigm_summary_window)
        self.ui_controller.stacked_widget.addWidget(self.database_window)
        
        self.connect_buttons()

    def set_verb_paradigm_window(self):
        self.ui_controller.stacked_widget.setCurrentWidget(self.verb_paradigm_window)
     
    def start_verb_paradigm_mode(self):
        EXTRA_WIDTH = 5

        self.set_verb_paradigm_window()
        self.verb_paradigm_window.widget.stacked_buttons.setCurrentWidget(self.verb_paradigm_window.widget.check_page)

        #Add a function to do this and also another that connects the event of chanfing the size of the window
        total_width = self.verb_paradigm_window.widget.paradigm_table.width()
        header_width = floor(total_width / 4) - EXTRA_WIDTH
        self.verb_paradigm_window.widget.paradigm_table.horizontalHeader().setDefaultSectionSize(header_width)

        self.game_model.load_questions_paradigm()
        self.game_model.set_current_paradigm()

        self.game_model.given_entry_index = self.verb_paradigm_window.set_row_in_table(
            self.game_model.current_paradigm)

    def add_character(self):
        self.verb_paradigm_window.add_character()

    def check_answer(self):
        is_correct = []
        tenses = ["Present", "Präteritum", "Perfekt"]
        text_to_show = ""

        user_answer = self.verb_paradigm_window.read_entries_in_table()
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
        self.verb_paradigm_window.widget.comparison_result_label.setText(text_to_show)
        self.paradigm_summary_window.append_row_to_summary_table(user_answer,
                                                                 self.game_model.current_paradigm,
                                                                 is_correct,
                                                                 self.game_model.given_entry_index)

        self.update_question()
        if self.game_model.current_word == self.game_model.QUESTIONS_PER_GAME:
            self.verb_paradigm_window.enable_go_to_summary_button()
            self.update_final_score()
            self.game_model.update_score_in_database()

    def update_question(self):
        self.game_model.update_current_word()
        if self.game_model.current_word < self.game_model.QUESTIONS_PER_GAME:
            self.game_model.set_current_paradigm()
            self.game_model.given_entry_index = self.verb_paradigm_window.set_row_in_table(
                self.game_model.current_paradigm)

    def show_summary(self):
        self.ui_controller.stacked_widget.setCurrentWidget(self.paradigm_summary_window)
        self.paradigm_summary_window.update_columns_width()
        self.paradigm_summary_window.adjust_table_height()

    def update_final_score(self):
        self.game_model.score.update_total_score()
        self.game_model.score.update_total_counter()
        present_partial_score = f"Present: Partial Score: {self.game_model.score.present_partial_score}/{self.game_model.score.present_partial_counter}\n"
        praeteritum_partial_score = f"Präteritum: Partial Score: {self.game_model.score.praeteritum_partial_score}/{self.game_model.score.praeteritum_partial_counter}\n"
        perfekt_partial_score = f"Perfekt: Partial Score: {self.game_model.score.perfekt_partial_score}/{self.game_model.score.perfekt_partial_counter}\n"

        text_to_show = present_partial_score + praeteritum_partial_score + perfekt_partial_score
        self.paradigm_summary_window.widget.partial_score_label.setText(text_to_show)

        present_total_score = f"Total Score: {self.game_model.score.present_total_score}/{self.game_model.score.present_total_counter}\n"
        praeteritum_total_score = f"Total Score: {self.game_model.score.praeteritum_total_score}/{self.game_model.score.praeteritum_total_counter}\n"
        perfekt_total_score = f"Total Score: {self.game_model.score.perfekt_total_score}/{self.game_model.score.perfekt_total_counter}\n"

        text_to_show = present_total_score + praeteritum_total_score + perfekt_total_score
        self.paradigm_summary_window.total_score_label.setText(text_to_show)

    def open_database(self):
        self.ui_controller.set_previous_index(self.ui_controller.stacked_widget.currentIndex())
        self.database_window.show_paradigm_database()
        self.ui_controller.stacked_widget.setCurrentWidget(self.database_window)

    def reset_paradigm_mode_view(self):
        self.ui_controller.stacked_widget.setCurrentWidget(self.verb_paradigm_window)
        self.verb_paradigm_window.widget.stacked_buttons.setCurrentWidget(self.verb_paradigm_window.widget.check_page)
        self.verb_paradigm_window.widget.comparison_result_label.setText("")
        self.verb_paradigm_window.clear_entry_row()
        self.paradigm_summary_window.model.removeRows(0, self.paradigm_summary_window.model.rowCount())

    def play_again(self):
        self.reset_paradigm_mode_view()
        self.game_model.reset_game()
        self.start_verb_paradigm_mode()

    def connect_buttons(self):
        self.ui_controller.select_game_mode_window.connect_paradigm_mode_button(self.start_verb_paradigm_mode)

        self.verb_paradigm_window.connect_add_character_button(self.add_character)
        self.verb_paradigm_window.connect_check_button(self.check_answer)
        self.verb_paradigm_window.connect_go_to_summary_button(self.show_summary)
        self.verb_paradigm_window.connect_open_database_button(self.open_database)

        self.paradigm_summary_window.connect_play_again_button(self.play_again)
        self.paradigm_summary_window.connect_quit_button(self.ui_controller.quit_game)

        self.database_window.connect_go_back_button(self.ui_controller.set_previous_window)

