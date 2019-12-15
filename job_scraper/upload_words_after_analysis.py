import os
import re
from job_scraper.common import DBCursor


WORD_REGEX = r"[a-zA-Z\#\+]{2,}"

class WordAfterAnalysis:
    def __init__(self, line):
        self.value = self.extract_value(line)
        self.class_ = self.extract_class(line)
        # self.root_word = self.extract_root_word(line)

    def __str__(self):
        return f"{self.value} WITH class == {self.class_}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @staticmethod
    def extract_value(line):
        return re.findall(r"\<\>(" + WORD_REGEX + r")[ ]*\<\>", line)[0]


    @staticmethod
    def extract_class(line):
        match = re.findall(r"\<class\>([\d]*)\<\>", line)[0]
        if not match:
            return 0
        return int(match)


def get_list_of_files():
    path_to_stages = os.path.join(os.getcwd(), 'stage')
    list_of_basenames = os.listdir(path_to_stages)
    list_of_paths = [os.path.join(path_to_stages, basename) for basename in list_of_basenames]
    return list_of_paths

def reduce_words(words):
    words_reduced = []
    values = set([word.value for word in words])
    for value in values:
        words_with_same_values = list(filter(lambda word: word.value == value, words))
        representative = words_with_same_values[0]
        representative.class_ = max([word.class_ for word in words_with_same_values])
        words_reduced.append(representative)
    return words_reduced



if __name__ == '__main__':
    list_of_paths = get_list_of_files()
    path_ = list_of_paths[0]
    with open(path_, "r") as file:
        lines = file.readlines()

    words = [WordAfterAnalysis(line) for line in lines]
    words_reduced = reduce_words(words)

    database = "first_db"
    creds = {
        "user": "devoted",
        "password": "Janina123"
    }

    with DBCursor(creds, database) as (cur, con):
        for word in words_reduced:
            cur.execute(f"INSERT INTO title_words VALUES (\'{word.value}\', {word.class_})")
            # cur.execute("SELECT id, name FROM public.offers WHERE status='WAITS_FOR_FILTER'")
            # rows = cur.fetchall()
            con.commit()




