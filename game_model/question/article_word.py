ARTICLE = 1
GERMAN = 2
ITALIAN = 3
SCORE = 4


class ArticleWord:
    def __init__(self, row) -> None:
        self.article: str = row[ARTICLE]
        self.german_word: str = row[GERMAN]
        self.italian_word: str = row[ITALIAN]
        self.num_of_correct_guesses: str = row[SCORE]