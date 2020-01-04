from job_scraper.upload_words_after_analysis import WordAfterAnalysis, reduce_words
from pytest import mark


@mark.parametrize("line, expected", [
    (r"<>word              <>id=1 FROM \"Some Name With Word\" <class><> <phrase><>", "word"),
    (r"<>word              <>id=1 FROM \"Some Name With Word\" <class>1<> <phrase><>", "word"),
    (r"<>word              <>id=1 FROM \"Some Name With Word\" <class><> <phrase>wor<>", "word"),
    (r"<>word              <>id=1 FROM \"Some Name With Word\" <class>1<> <phrase>wor<>", "word"),
    ])
def test_extract_value(line, expected):
    actual = WordAfterAnalysis.extract_value(line)
    assert actual == expected


@mark.parametrize("line, expected", [
    (r"<>word              <>id=1 FROM \"Some Name With Word\" <class>1<> <phrase><>", 1),
    (r"<>word              <>id=1 FROM \"Some Name With Word\" <class><> <phrase><>", 0),
    ])
def test_extract_class(line, expected):
    actual = WordAfterAnalysis.extract_class(line)
    assert actual == expected


def convert_tuples_to_objects(words_as_tuples):
    words = []
    for tuple_ in words_as_tuples:
        new_word = WordAfterAnalysis("<>word              <>id=1 FROM \"Some Name With Word\" <class><> <phrase><>")
        new_word.value = tuple_[0]
        new_word.class_ = tuple_[1]
        words.append(new_word)
    return words

@mark.parametrize("words_as_tuples, expected_as_tuples", [
    ([("word1", 1), ("word1", 0), ("word2", 1), ("word2", 0)],[("word1", 1), ("word2", 1)]),
    ([("word1", 0), ("word1", 1), ("word2", 0), ("word2", 0)],[("word1", 1), ("word2", 0)]),
    ([("word1", 0), ("word1", 1)], [("word1", 1)]),
    ])
def test_reduce_words(words_as_tuples, expected_as_tuples):
    words = convert_tuples_to_objects(words_as_tuples)
    actual = reduce_words(words)
    expected = convert_tuples_to_objects(expected_as_tuples)
    assert sorted(actual, key=lambda word: (word.value)) == expected