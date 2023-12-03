from numpy.random import choice
import pandas
from game_model.game_mode.game import Game
from game_model.score_system.paradigm_score import ParadigmScore
from game_model.question.verb_paradigm import VerbParadigm

paradigm_database = pandas.read_csv("database/verb_paradigm_database.csv")
paradigm_database_dict = paradigm_database.to_dict(orient="records")


class ParadigmGame(Game):
    def __init__(self):
        super().__init__()
        self.list_of_paradigms = []
        self.current_paradigm = []
        self.given_entry_index = 0
        self.guessed_entries = []
        self.score = ParadigmScore()

    def load_questions_paradigm(self):
        guessed_counter_list = []
        scores = ["PresentScore", "PraeteritumScore", "PerfektScore"]

        total_score = 0

        for element in paradigm_database_dict:
            for key in element:
                if key in scores:
                    total_score += element[key]
            guessed_counter_list.append(total_score)
            total_score = 0

        sum_of_values = sum(guessed_counter_list)
        normalized_guessed_counter_list = [value / sum_of_values for value in guessed_counter_list]

        try:
            verbs_list = choice(
                paradigm_database_dict,
                self.QUESTIONS_PER_GAME,
                replace=False,
                p=normalized_guessed_counter_list
            )
        except ValueError:
            verbs_list = choice(
                paradigm_database_dict,
                self.QUESTIONS_PER_GAME,
                replace=True,
                p=normalized_guessed_counter_list
            )

        for row in verbs_list:
            verb_paradigm = VerbParadigm(row)
            self.list_of_paradigms.append(verb_paradigm)

    def check_entry(self, user_answer):
        is_correct = [False, False, False]

        for index, entry in enumerate(user_answer):
            # Da mettere a posto con una logica migliore
            if index != self.given_entry_index:
                if entry == self.list_of_paradigms[self.current_word].present:
                    self.score.present_partial_score += 1
                    is_correct[0] = True
                elif entry == self.list_of_paradigms[self.current_word].praeteritum :
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
                if self.guessed_entries[index][inner_index] and inner_index == 0:
                    mask = paradigm_database["Present"] == self.list_of_paradigms[index].present
                    paradigm_database.loc[mask, "PresentScore"] += 1
                elif self.guessed_entries[index][inner_index] and inner_index == 1:
                    mask = paradigm_database["Praeteritum"] == self.list_of_paradigms[index].praeteritum
                    paradigm_database.loc[mask, "PraeteritumScore"] += 1
                elif self.guessed_entries[index][inner_index] and inner_index == 2:
                    mask = paradigm_database["Perfekt"] == self.list_of_paradigms[index].perfekt
                    paradigm_database.loc[mask, "PerfektScore"] += 1

        paradigm_database.to_csv("database/verb_paradigm_database.csv", index=False)

    def reset_game(self):
        self.list_of_paradigms = []
        self.current_paradigm = []
        self.guessed_entries = []
        self.given_entry_index = 0
        self.update_number_of_matches()
        self.reset_current_word()
        self.score.reset_partial_score()
        self.score.reset_counter()


