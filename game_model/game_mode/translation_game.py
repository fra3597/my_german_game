from random import choices
from game_model.score_system.translation_score import TranslationScore
from game_model.game_mode.game import Game
from game_model.question.translate_word import TranslationWord
from database.database_handler import DatabaseHandler

OCCURRENCE_FACTOR = 5
SCORE_COLUMN = "Score"

CORRECT = True


class TranslationGame(Game):
    def __init__(self, database_handler) -> None:
        super().__init__()
        self.score: TranslationScore = TranslationScore()
        self.language_mode = None
        self.questions: list[str] = []
        self.answers: list[str] = []
        self.GERMAN_TO_ITALIAN = 1
        self.ITALIAN_TO_GERMAN = 2
        self.db_handler = database_handler

    def set_mode(self, mode_to_set):
        self.language_mode = mode_to_set

    def load_questions(self):
        weights_list = self.db_handler.get_weights_list()
        all_rows = self.db_handler.get_all_rows()

        words_list = choices(all_rows, weights=weights_list, k=self.QUESTIONS_PER_GAME)

        if self.language_mode == self.ITALIAN_TO_GERMAN:
            for row in words_list:
                word = TranslationWord(row)
                self.questions.append(word.italian_word)
                self.answers.append(word.german_word)
        else:
            for row in words_list:
                word = TranslationWord(row)
                self.questions.append(word.german_word)
                self.answers.append(word.italian_word)

    def update_score_in_database(self):
        german_word = ""

        for index, word in enumerate(self.guessed_entries):
            if self.guessed_entries[index]:
                if self.language_mode == self.ITALIAN_TO_GERMAN:
                    german_word = self.answers[index]
                elif self.language_mode == self.GERMAN_TO_ITALIAN:
                    german_word = self.questions[index]
                self.db_handler.update_score(word=german_word, score_to_update=SCORE_COLUMN)

    def reset_game(self):
        self.update_number_of_matches()
        self.score.reset_partial_score()
        self.reset_current_word()
        self.guessed_entries = []
        self.questions = []
        self.answers = []
