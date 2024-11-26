import re

# def main(a, b):
#     c = add(a, b)
#     print(c)

# if __name__ == '__main__':
#     main(2, 4)


# TODO take filepath, not string
def word_count(text):
    counts = {}

    # TODO strip punctuation/special chars

    # force lowercase
    text = text.lower()

    # strip leading/trailing whitespace
    text = text.strip()

    # replace any whitespace with single spaces
    text = re.sub(r"\s+", " ", text)

    # split text on spaces
    words = text.split(" ")

    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    return counts
