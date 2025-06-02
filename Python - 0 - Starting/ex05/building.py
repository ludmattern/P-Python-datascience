"""
building.py - A program that analyzes text character composition
"""

from sys import argv, stdin


def analyze_text(text):
    """
    Analyze the text and count different types of characters

    Args:
        text (str): The text to analyze

    Returns:
        dict: Dictionary containing counts of different character types
    """
    counts = {"total": len(text),
              "upper": 0,
              "lower": 0,
              "punctuation": 0,
              "spaces": 0,
              "digits": 0
              }

    for char in text:
        if char.isupper():
            counts["upper"] += 1
        elif char.islower():
            counts["lower"] += 1
        elif char.isdigit():
            counts["digits"] += 1
        elif char.isspace():
            counts["spaces"] += 1
        elif not char.isalnum() and not char.isspace():
            counts["punctuation"] += 1

    return counts


def display_results(counts):
    """
    Display the analysis results in the required format

    Args:
        counts (dict): Dictionary containing character counts
    """
    print(f"The text contains {counts['total']} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


def main():
    """
    Main function that handles command line arguments and user input
    """

    argc = len(argv)

    if argc > 2:
        raise AssertionError("more than one argument is provided")

    if argc == 2:
        text = argv[1]
    else:
        print("What is the text to count?")
        try:
            text = stdin.readline()
        except EOFError:
            text = ""
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return

    counts = analyze_text(text)

    display_results(counts)


if __name__ == "__main__":
    main()
