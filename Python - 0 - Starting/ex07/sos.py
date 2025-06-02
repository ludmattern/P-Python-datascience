from sys import argv


def encode_to_morse():
    """
    Encodes a string argument into Morse Code.
    Raises AssertionError if arguments are invalid.
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }

    if len(argv) != 2:
        raise AssertionError("the arguments are bad")

    text = argv[1]

    if not isinstance(text, str):
        raise AssertionError("the arguments are bad")

    text = text.upper()

    for char in text:
        if char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")

    morse_code = ""
    for char in text:
        morse_code += NESTED_MORSE[char]

    print(morse_code.rstrip())


def main():
    """
    Main function that handles exceptions from encode_to_morse.
    """
    try:
        encode_to_morse()
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
