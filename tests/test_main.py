from src import main


SAMPLE_TEXT = """
Hello world!
This is a sample text file.
Hello Python world.
"""


def test_word_count():
    counts = main.word_count(SAMPLE_TEXT)
    assert counts == {
        'hello': 2,
        'world': 2,
        'this': 1,
        'is': 1,
        'a': 1,
        'sample': 1,
        'text': 1,
        'file': 1,
        'python': 1
    }


# TODO break cleaning operations into small helper functions
#   and test them all here.