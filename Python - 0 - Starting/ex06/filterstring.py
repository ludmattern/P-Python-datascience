from sys import argv
from ft_filter import ft_filter


def main():
    """
    Filters a list of words based on their length.
    Usage: python filterstring.py "string" number
    """
    if len(argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    try:
        string_arg = argv[1]
        length = int(argv[2])

        words = string_arg.split()

        filtered_words = ft_filter(lambda word: len(word) > length, words)

        result = list(filtered_words)
        print(result)

    except ValueError:
        print("AssertionError: the arguments are bad")
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
