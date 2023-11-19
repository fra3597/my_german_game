class TranslationScore:
    def __init__(self) -> None:
        self.total_score = 0
        self.partial_score = 0

    def update_partial_score(self):
        self.partial_score += 1

    def update_total_score(self):
        self.total_score += self.partial_score

    def reset_partial_score(self):
        self.partial_score = 0

    