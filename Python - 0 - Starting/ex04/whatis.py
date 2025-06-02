def main():
    """
    Script that takes a number as argument and checks whether itnis odd or even
    Prints an AssertionError if more than one argument is provided or if the
    argument is not an integer.
    """
    from sys import argv

    argc = len(argv)

    if argc == 1:
        return

    if argc > 2:
        print("AssertionError: more than one argument is provided")
        return

    arg = argv[1]

    try:
        number = int(arg)

        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except ValueError:
        print("AssertionError: argument is not an integer")


if __name__ == "__main__":
    main()
