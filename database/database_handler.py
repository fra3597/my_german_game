import pandas
import sqlite3

OCCURRENCE_FACTOR = 5
PRESENT_SCORE = 0
PRÄTERITUM_SCORE = 1
PERFEKT_SCORE = 2


class DatabaseHandler:
    def __init__(self, db_path, table_name):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.table_name = table_name

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

    def update_score(self, word, score_to_update):
        if self.table_name == "VerbParadigms":
            update_query = f"UPDATE {self.table_name} SET {score_to_update} = {score_to_update} + 1 WHERE Present = '{word}'"
        else:
            update_query = f"UPDATE {self.table_name} SET {score_to_update} = {score_to_update} + 1 WHERE German = '{word}'"
        self.cursor.execute(update_query)
        self.conn.commit()

    def get_all_rows(self):
        query = f'SELECT * FROM {self.table_name}'
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def get_weights_list(self):
        weights_list = []
        total_weights = 0

        if self.table_name == "VerbParadigms":
            query = f'SELECT PresentScore, PräteritumScore, PerfektScore FROM {self.table_name}'
            all_scores = self.cursor.execute(query)
            for score in all_scores:
                total_row_score = score[PRESENT_SCORE] + score[PRÄTERITUM_SCORE] + score[PERFEKT_SCORE]
                weight = 1 / (OCCURRENCE_FACTOR ** total_row_score)
                weights_list.append(weight)
                total_weights += weight
        else:
            query = f'SELECT Score FROM {self.table_name}'
            all_scores = self.cursor.execute(query)
            for score in all_scores:
                row_score = score[0]
                weight = 1/(OCCURRENCE_FACTOR ** row_score)
                weights_list.append(weight)
                total_weights += weight

            normalized_weights_list = [value / total_weights for value in weights_list]

            return normalized_weights_list
