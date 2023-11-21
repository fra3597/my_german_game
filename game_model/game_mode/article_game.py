from numpy.random import choice
import pandas
from game_model.game_mode.game import Game
from game_model.score_system.article_score import ArticleScore
from game_model.question.article_word import ArticleWord

filename = "database/words_with_article_database.csv"
database = pandas.read_csv(filename)
database_dict = database.to_dict(orient="records")


class ArticleGame(Game):
    def __init__(self):
        super().__init__()
        self.score = ArticleScore()
        self.list_of_words = []

    def load_questions(self):
        guessed_counter_list = [inner_dict.get("Score", None) for inner_dict in database_dict]
        sum_of_values = sum(guessed_counter_list)
        normalized_guessed_counter_list = [value / sum_of_values for value in guessed_counter_list]

        try:
            words_list = choice(database_dict, self.QUESTIONS_PER_GAME, replace=False, p=normalized_guessed_counter_list)
        except ValueError:
            words_list = choice(database_dict, self.QUESTIONS_PER_GAME, replace=True, p=normalized_guessed_counter_list)

        for row in words_list:
            article_word = ArticleWord(row)
            self.list_of_words.append(article_word)

    def update_score_in_database(self):
        for index, word in enumerate(self.guessed_entries):
            if self.guessed_entries[index]:
                mask = database["German"] == self.list_of_words[index].german_word
                database.loc[mask, "Score"] += 1

        database.to_csv(filename, index=False)

    def reset_game(self):
        self.update_number_of_matches()
        self.score.reset_partial_score()
        self.reset_current_word()
        self.guessed_entries = []
        self.list_of_words = []
