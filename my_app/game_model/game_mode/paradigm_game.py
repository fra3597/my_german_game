from random import choices
from game_model.game_mode.game import Game
from game_model.score_system.paradigm_score import ParadigmScore
from game_model.question.verb_paradigm import VerbParadigm
from database.database_handler import DatabaseHandler

OCCURRENCE_FACTOR = 5

CORRECT = True
PRESENT = 0
PRÄTERITUM = 1
PERFEKT = 2


class ParadigmGame(Game):
    def __init__(self, database_handler: DatabaseHandler):
        super().__init__()
        self.list_of_paradigms: list[VerbParadigm] = []
        self.current_paradigm: list[str] = []
        self.given_entry_index: int = 0
        self.guessed_entries: list[list[bool]] = []
        self.score: ParadigmScore = ParadigmScore()
        self.db_handler: DatabaseHandler = database_handler

    def load_questions_paradigm(self):
        weights_list = self.db_handler.get_weights_list()
        all_rows = self.db_handler.get_all_rows()

        words_list = choices(all_rows, weights=weights_list, k=self.QUESTIONS_PER_GAME)

        for row in words_list:
            paradigm = VerbParadigm(row)
            self.list_of_paradigms.append(paradigm)

    def check_entry(self, user_answer: str):
        is_correct = [False, False, False]

        for index, entry in enumerate(user_answer):
            # Da mettere a posto con una logica migliore
            if index != self.given_entry_index:
                if entry == self.list_of_paradigms[self.current_word].present:
                    self.score.present_partial_score += 1
                    is_correct[0] = True
                elif entry == self.list_of_paradigms[self.current_word].praeteritum:
                    self.score.praeteritum_partial_score += 1
                    is_correct[1] = True
                elif entry == self.list_of_paradigms[self.current_word].perfekt:
                    self.score.perfekt_partial_score += 1
                    is_correct[2] = True

        if self.given_entry_index != 0:
            self.score.present_partial_counter += 1
        if self.given_entry_index != 1:
            self.score.praeteritum_partial_counter += 1
        if self.given_entry_index != 2:
            self.score.perfekt_partial_counter += 1

        return is_correct

    def set_current_paradigm(self):
        current_paradigm = [self.list_of_paradigms[self.current_word].present,
                            self.list_of_paradigms[self.current_word].praeteritum,
                            self.list_of_paradigms[self.current_word].perfekt,
                            self.list_of_paradigms[self.current_word].italian]

        self.current_paradigm = current_paradigm

    def update_score_in_database(self):
        for index, paradigm in enumerate(self.guessed_entries):
            for inner_index, verb in enumerate(paradigm):
                if self.guessed_entries[index][inner_index] == CORRECT and inner_index == PRESENT:
                    self.db_handler.update_score(
                        word=self.list_of_paradigms[index].present,
                        score_to_update="PresentScore"
                    )
                elif self.guessed_entries[index][inner_index] and inner_index == PRÄTERITUM:
                    self.db_handler.update_score(
                        word=self.list_of_paradigms[index].present,
                        score_to_update="PräteritumScore"
                    )
                elif self.guessed_entries[index][inner_index] and inner_index == PERFEKT:
                    self.db_handler.update_score(
                        word=self.list_of_paradigms[index].present,
                        score_to_update="PerfektScore"
                    )

    def reset_game(self):
        self.list_of_paradigms = []
        self.current_paradigm = []
        self.guessed_entries = []
        self.given_entry_index = 0
        self.update_number_of_matches()
        self.reset_current_word()
        self.score.reset_partial_score()
        self.score.reset_counter()


