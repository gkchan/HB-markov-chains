"""Generate markov text from text files."""
from sys import argv

from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as text_file:
        return text_file.read().strip()


def make_chains(text_string, n = 2):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    """

    chains = {}

    words = text_string.split()

    # This code doesn't create a key for last words.

    for index in range(len(words) - n):
        # key = (words[index], words[index + 1])
        # value = words[index + 2]
        key = tuple(words[index:index + n])
        value = words[index + n]

        chains[key] = chains.get(key, [])
        chains[key].append(value)

    return chains


def make_text(chains, n = 2):
    """Returns text from chains."""

    # picks a random consecutive pair of words to start our string
    words = list(choice(chains.keys()))

    while True:
        try:

            key = tuple(words[-n:])
            value = chains[key]
            words.append(choice(value))

        except KeyError:
            break

    return " ".join(words)


input_path = argv[1]
n = int(argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains, n)

print random_text
