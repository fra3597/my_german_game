PRESENT = 1
PRAETERITUM = 2
PERFEKT = 3
ITALIAN = 4
PRESENT_SCORE = 5
PRAETERITUM_SCORE = 6
PERFEKT_SCORE = 7


class VerbParadigm:
    def __init__(self, row):
        self.present: str = row[PRESENT]
        self.praeteritum: str = row[PRAETERITUM]
        self.perfekt: str = row[PERFEKT]
        self.italian: str = row[ITALIAN]
        self.present_score: int = row[PRESENT_SCORE]
        self.praeteritum_score: int = row[PRAETERITUM_SCORE]
        self.perfekt_score: int = row[PERFEKT_SCORE]