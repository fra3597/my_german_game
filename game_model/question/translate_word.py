GERMAN = 1
ITALIAN = 2
SCORE = 3


class TranslationWord:
    def __init__(self, row) -> None:
        self.german_word: str = row[GERMAN]
        self.italian_word: str = row[ITALIAN]
        self.num_of_correct_guesses: int = row[SCORE]
        
    def increase_num_of_correct_guesses(self):
        self.num_of_correct_guesses += 1
