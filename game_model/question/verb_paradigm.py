class VerbParadigm:
    def __init__(self, row):
        self.present = row["Present"]
        self.praeteritum = row["Praeteritum"]
        self.perfekt = row["Perfekt"]
        self.italian = row["Italian"]
        self.present_score = row["PresentScore"]
        self.praeteritum_score = row["PraeteritumScore"]
        self.perfekt_score = row["PerfektScore"]