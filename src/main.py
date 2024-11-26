import re

# TODO add file handling to main, so file can be
#   specified as an argument.
# def main(a, b):
#     c = add(a, b)
#     print(c)

# if __name__ == '__main__':
#     main(2, 4)


# TODO take filepath, not string
def word_count(text):
    counts = {}

    # strip leading/trailing whitespace
    text = text.strip()

    # force lowercase
    text = text.lower()

    # replace any whitespace with single spaces
    text = re.sub(r"\s+", " ", text)

    # split text on spaces
    words = text.split(" ")

    for word in words:
        # strip non-alphanumeric chars
        # TODO strip underscores
        word = re.sub(r"\W", "", word)

        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    return counts
