class TranslationWord:
    def __init__(self, row) -> None:
        self.german_word = row["German"]
        self.italian_word = row["Italian"]
        self.num_of_correct_guesses = row["Score"]
        
    def increase_num_of_correct_guesses(self):
        self.num_of_correct_guesses += 1
