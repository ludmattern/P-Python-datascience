from typing import Any


def callLimit(limit: int):
    """Decorator that limits the number of calls to a function."""
    count = 0

    def callLimiter(function):
        """Decorator function that wraps the original function"""
        def limit_function(*args: Any, **kwds: Any):
            """Function that checks the call limit and calls the
            original function."""
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return None
            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter
