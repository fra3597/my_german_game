from numpy.random import choice
import pandas
from game_model.game_mode.game import Game
from game_model.score_system.paradigm_score import ParadigmScore
from game_model.question.verb_paradigm import VerbParadigm


QUESTIONS_PER_GAME = 10

paradigm_database = pandas.read_csv("database/verb_paradigm_database.csv")
paradigm_database_dict = paradigm_database.to_dict(orient="records")


class ParadigmGame(Game):
    def __init__(self):
        super().__init__()
        self.list_of_paradigms = []
        self.current_paradigm = []
        self.given_entry_index = 0
        self.score = ParadigmScore()

    def load_questions_paradigm(self):
        guessed_counter_list = []
        scores = ["PresentScore", "PräteritumScore", "PerfektScore"]

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
                QUESTIONS_PER_GAME,
                replace=False,
                p=normalized_guessed_counter_list
            )
        except ValueError:
            verbs_list = choice(
                paradigm_database_dict,
                QUESTIONS_PER_GAME,
                replace=True,
                p=normalized_guessed_counter_list
            )

        for row in verbs_list:
            verb_paradigm = VerbParadigm(row)
            self.list_of_paradigms.append(verb_paradigm)

    def check_entry(self, user_answer):
        is_correct = [False, False, False]

        for entry in user_answer:
            if entry == self.list_of_paradigms[self.current_word].present:
                self.score.present_partial_score += 1
                is_correct[0] = True
            elif entry == self.list_of_paradigms[self.current_word].präteritum:
                self.score.präteritum_partial_score += 1
                is_correct[1] = True
            elif entry == self.list_of_paradigms[self.current_word].perfekt:
                self.score.perfekt_partial_score += 1
                is_correct[2] = True
        self.score.present_counter += 1
        self.score.präteritum_counter += 1
        self.score.perfekt_counter += 1

        return is_correct

    def set_current_paradigm(self):
        current_paradigm = [self.list_of_paradigms[self.current_word].present,
                            self.list_of_paradigms[self.current_word].präteritum,
                            self.list_of_paradigms[self.current_word].perfekt,
                            self.list_of_paradigms[self.current_word].italian]

        self.current_paradigm = current_paradigm
