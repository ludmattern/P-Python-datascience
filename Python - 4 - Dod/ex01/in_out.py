def square(x: int | float) -> int | float:
    """ Return the square of the argument """
    return x * x


def pow(x: int | float) -> int | float:
    """ Return the exponentiation of the argument by itself (x^x) """
    return x ** x


def outer(x: int | float, function) -> object:
    """ Higher-order function that creates a closure.
    Returns a function that applies 'function' to the previous result.
    """
    count = 0

    def inner() -> float:
        """ Inner function that applies 'function' to 'x' """
        nonlocal x, count
        count += 1
        x = function(x)
        return x

    return inner
