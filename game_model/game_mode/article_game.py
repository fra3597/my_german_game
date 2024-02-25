from random import choices
from game_model.game_mode.game import Game
from game_model.score_system.article_score import ArticleScore
from game_model.question.article_word import ArticleWord
from database.database_handler import DatabaseHandler

OCCURRENCE_FACTOR = 5
TABLE_NAME = "WordsWithArticles"
FILENAME_DB = "database/words_with_articles.db"
SCORE_COLUMN = "Score"

CORRECT = True


class ArticleGame(Game):
    def __init__(self):
        super().__init__()
        self.score: ArticleScore = ArticleScore()
        self.list_of_words: list[ArticleWord] = []
        self.db_handler = DatabaseHandler(db_path=FILENAME_DB, table_name=TABLE_NAME)

    def load_questions(self):
        weights_list = self.db_handler.get_weights_list()
        all_rows = self.db_handler.get_all_rows()

        words_list = choices(all_rows, weights=weights_list, k=self.QUESTIONS_PER_GAME)

        for row in words_list:
            article_word = ArticleWord(row)
            self.list_of_words.append(article_word)

    def update_score_in_database(self):
        for index, guess in enumerate(self.guessed_entries):
            if guess == CORRECT:
                german_word = self.list_of_words[index].german_word
                self.db_handler.update_score(word=german_word, score_to_update=SCORE_COLUMN)

    def reset_game(self):
        self.update_number_of_matches()
        self.score.reset_partial_score()
        self.reset_current_word()
        self.guessed_entries = []
        self.list_of_words = []
