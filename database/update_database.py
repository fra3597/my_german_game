import sqlite3
import pandas


def update_questions_database():
    db = sqlite3.connect("questions.db")
    cursor = db.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS Questions (id INTEGER PRIMARY KEY, German varchar(250) NOT NULL UNIQUE, Italian varchar(250) NOT NULL, Score INTEGER NOT NULL)")

    csv_file_path = 'questions.csv'
    data = pandas.read_csv(csv_file_path)

    for index, row in data.iterrows():
        try:
            cursor.execute("INSERT INTO Questions (German, Italian, Score) VALUES (?, ?, ?)", (row['German'], row['Italian'], row['Score']))
        except sqlite3.IntegrityError:
            # print(f"Skipping duplicate entry for German: {row['German']}")
            pass

    db.commit()
    db.close()


def update_paradigms_database():
    db = sqlite3.connect("verb_paradigms.db")
    cursor = db.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS VerbParadigms "
                   "("
                       "id INTEGER PRIMARY KEY,"
                       "Present varchar(250) NOT NULL UNIQUE,"
                       "Präteritum varchar(250) NOT NULL,"
                       "Perfekt varchar(250) NOT NULL,"
                       "Italian varchar(250) NOT NULL,"
                       "PresentScore INTEGER NOT NULL,"
                       "PräteritumScore INTEGER NOT NULL,"
                        "PerfektScore INTEGER NOT NULL"
                   ")"
                   )

    csv_file_path = 'Verbs_Paradigms.csv'
    data = pandas.read_csv(csv_file_path)

    for index, row in data.iterrows():
        try:
            cursor.execute("INSERT INTO VerbParadigms (Present, Präteritum, Perfekt, Italian, PresentScore, PräteritumScore, PerfektScore) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (row['Present'], row['Präteritum'], row['Perfekt'], row['Italian'], row['PresentScore'], row['PräteritumScore'], row['PerfektScore']))
        except sqlite3.IntegrityError:
            #print(f"Skipping duplicate entry for Present: {row['Present']}")
            pass

    db.commit()
    db.close()


def update_words_with_article_database():
    db = sqlite3.connect("words_with_articles.db")
    cursor = db.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS WordsWithArticles (id INTEGER PRIMARY KEY, Article varchar(250) NOT NULL, German varchar(250) NOT NULL UNIQUE, Italian varchar(250) NOT NULL, Score INTEGER NOT NULL)")

    csv_file_path = 'words_with_article_database.csv'
    data = pandas.read_csv(csv_file_path)

    for index, row in data.iterrows():
        try:
            cursor.execute("INSERT INTO WordsWithArticles (Article, German, Italian, Score) VALUES (?, ?, ?, ?)", (row['Article'], row['German'], row['Italian'], row['Score']))
        except sqlite3.IntegrityError:
            # print(f"Skipping duplicate entry for German: {row['German']}")
            pass

    db.commit()
    db.close()


# Call the function to update the database
update_questions_database()
update_paradigms_database()
update_words_with_article_database()