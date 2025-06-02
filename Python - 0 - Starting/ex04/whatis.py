def check_number():
    """
    Function that checks if a number is odd or even.
    Raises AssertionError if more than one argument is provided or if the
    argument is not an integer.
    """
    from sys import argv

    argc = len(argv)

    if argc == 1:
        return

    if argc > 2:
        raise AssertionError("more than one argument are provided")

    arg = argv[1]

    try:
        number = int(arg)

        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except ValueError:
        raise AssertionError("argument is not an integer")


def main():
    """
    Main function that handles exceptions from check_number.
    """
    try:
        check_number()
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
