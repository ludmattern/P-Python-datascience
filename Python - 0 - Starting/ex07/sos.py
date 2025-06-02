from sys import argv


def main():
    """
    Program that takes a string as an argument and encodes it into Morse Code.
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


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
