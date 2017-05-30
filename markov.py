"""Generate markov text from text files."""


from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as text_file:
        return text_file.read().strip()


def make_chains(text_string):
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

    # tuple_list = []

    # This code doesn't account for the last tuple pair of ("I", "am?").

    for index in range(len(words) - 2):

        key = (words[index], words[index + 1])
        value = words[index + 2]

        # tuple_list.append(key)
        # if key in chains:
        #     chains[key].append(value)
        # else:
        #     chains[key] = [value]

        print chains.get(key, [])
        chains[key].append(value)

    return chains


def make_text(chains):
    """Returns text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
print chains
# Produce random text
random_text = make_text(chains)

print random_text
