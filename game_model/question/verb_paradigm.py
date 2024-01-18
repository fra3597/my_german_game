PRESENT = 1
PRÄTERITUM = 2
PERFEKT = 3
ITALIAN = 4
PRESENT_SCORE = 5
PRÄTERITUM_SCORE = 6
PERFEKT_SCORE = 7


class VerbParadigm:
    def __init__(self, row):
        self.present: str = row[PRESENT]
        self.präteritum: str = row[PRÄTERITUM]
        self.perfekt: str = row[PERFEKT]
        self.italian: str = row[ITALIAN]
        self.present_score: int = row[PRESENT_SCORE]
        self.präteritum_score: int = row[PRÄTERITUM_SCORE]
        self.perfekt_score: int = row[PERFEKT_SCORE]