import sys


def main():
    """
    Script that takes a number as argument and checks whether it is odd or even.
    Prints an AssertionError if more than one argument is provided or if the argument is not an integer.
    """
    if len(sys.argv) == 1:
        return

    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    arg = sys.argv[1]

    try:
        number = int(arg)

        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except ValueError:
        print("AssertionError: argument is not an integer")


main()
