class ParadigmScore:
    def __init__(self):
        super().__init__()

        self.present_partial_counter = 0
        self.präteritum_partial_counter = 0
        self.perfekt_partial_counter = 0

        self.present_total_counter = 0
        self.präteritum_total_counter = 0
        self.perfekt_total_counter = 0

        self.present_partial_score = 0
        self.präteritum_partial_score = 0
        self.perfekt_partial_score = 0

        self.present_total_score = 0
        self.präteritum_total_score = 0
        self.perfekt_total_score = 0

    def update_total_score(self):
        self.present_total_score += self.present_partial_score
        self.präteritum_total_score += self.präteritum_partial_score
        self.perfekt_total_score += self.perfekt_partial_score

    def update_total_counter(self):
        self.present_total_counter += self.present_partial_counter
        self.präteritum_total_counter += self.präteritum_partial_counter
        self.perfekt_total_counter += self.perfekt_partial_counter

    def reset_partial_score(self):
        self.present_partial_score = 0
        self.präteritum_partial_score = 0
        self.perfekt_partial_score = 0

    def reset_counter(self):
        self.present_partial_counter = 0
        self.präteritum_partial_counter = 0
        self.perfekt_partial_counter = 0
