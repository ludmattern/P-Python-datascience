"""
ft_package

A sample test package for learning Python packaging.
"""

__version__ = "0.0.1"
__author__ = "eagle"
__email__ = "eagle@42.fr"
__license__ = "MIT"


def count_in_list(lst, item):
    """
    Count the number of occurrences of an item in a list.

    Args:
        lst (list): The list to search in
        item: The item to count

    Returns:
        int: The number of occurrences of the item in the list

    Example:
        >>> count_in_list(["toto", "tata", "toto"], "toto")
        2
    """
    if not isinstance(lst, list):
        raise TypeError("First argument must be a list")

    return lst.count(item)


# Make the function available when importing the package
__all__ = ["count_in_list"]
