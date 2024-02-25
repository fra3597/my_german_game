class Game:
    def __init__(self):
        self.number_of_matches: int = 1
        self.current_word: int = 0
        self.guessed_entries: list[bool] = []
        self.QUESTIONS_PER_GAME: int = 10

    def update_number_of_matches(self):
        self.number_of_matches += 1

    def update_current_word(self):
        self.current_word += 1

    def reset_current_word(self):
        self.current_word = 0
