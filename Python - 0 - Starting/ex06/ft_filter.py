def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    try:
        iterator = iter(iterable)
    except TypeError:
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")

    if function is not None and not callable(function):
        raise TypeError(f"'{type(function).__name__}' object is not callable")

    if function is None:
        return (item for item in iterator if item)
    else:
        return (item for item in iterator if function(item))
