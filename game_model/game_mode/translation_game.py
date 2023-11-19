from numpy.random import choice
import pandas
from game_model.score_system.translation_score import TranslationScore
from game_model.game_mode.game import Game
from game_model.question.translate_word import TranslationWord


ITALIAN_TO_GERMAN = 1
GERMAN_TO_ITALIAN = 2

QUESTIONS_PER_GAME = 10

database = pandas.read_csv("database/questions.csv")
database_dict = database.to_dict(orient="records")


class TranslationGame(Game):
    def __init__(self) -> None:
        super().__init__()
        self.score = TranslationScore()
        self.language_mode = None
        self.questions = []
        self.answers = []

    def set_mode(self, mode_to_set):
        self.language_mode = mode_to_set

    def load_questions(self):
        guessed_counter_list = [inner_dict.get("Score", None) for inner_dict in database_dict]
        sum_of_values = sum(guessed_counter_list)
        normalized_guessed_counter_list = [value / sum_of_values for value in guessed_counter_list]

        try:
            words_list = choice(database_dict, QUESTIONS_PER_GAME, replace=False, p=normalized_guessed_counter_list)
        except ValueError:
            words_list = choice(database_dict, QUESTIONS_PER_GAME, replace=True, p=normalized_guessed_counter_list)

        if self.language_mode == ITALIAN_TO_GERMAN:
            for row in words_list:
                word = TranslationWord(row)
                self.questions.append(word.italian_word)
                self.answers.append(word.german_word)
        else:
            for row in words_list:
                word = TranslationWord(row)
                self.questions.append(word.german_word)
                self.answers.append(word.italian_word)

    def reset_game(self):
        self.update_number_of_matches()
        self.score.reset_partial_score()
        self.reset_current_word()
        self.questions = []
        self.answers = []
