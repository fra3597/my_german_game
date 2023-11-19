class VerbParadigm:
    def __init__(self, row):
        self.present = row["Present"]
        self.präteritum = row["Präteritum"]
        self.perfekt = row["Perfekt"]
        self.italian = row["Italian"]
        self.present_score = row["PresentScore"]
        self.präteritum_score = row["PräteritumScore"]
        self.perfekt_score = row["PerfektScore"]