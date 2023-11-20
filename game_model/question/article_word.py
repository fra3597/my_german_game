class ArticleWord:
    def __init__(self, row) -> None:
        self.article = row["Article"]
        self.german_word = row["German"]
        self.italian_word = row["Italian"]
        self.num_of_correct_guesses = row["Score"]