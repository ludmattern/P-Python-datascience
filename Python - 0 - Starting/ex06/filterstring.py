from sys import argv
from ft_filter import ft_filter


def filter_words():
    """
    Filters a list of words based on their length.
    Raises AssertionError if arguments are invalid.
    """
    if len(argv) != 3:
        raise AssertionError("the arguments are bad")

    string_arg = argv[1]
    length = int(argv[2])

    words = string_arg.split()

    filtered_words = ft_filter(lambda word: len(word) > length, words)

    result = [word for word in filtered_words]
    print(result)


def main():
    """
    Main function that handles exceptions from filter_words.
    """
    try:
        filter_words()
    except (AssertionError, ValueError, Exception):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
