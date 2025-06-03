from numpy import array


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array, prints its shape, and returns a truncated version
    based on start and end arguments using slicing.

    Args:
        family: 2D list representing the array
        start: Starting index for slicing
        end: Ending index for slicing

    Returns:
        list: Truncated version of the input array

    Raises:
        TypeError: If input is not a list
        ValueError: If lists are not the same size or if array is not 2D
    """
    if not isinstance(family, list):
        raise TypeError("Input must be a list")

    if not family:
        raise ValueError("Input list cannot be empty")

    if not all(isinstance(row, list) for row in family):
        raise TypeError("All elements must be lists to form a 2D array")

    first_row_length = len(family[0])
    if not all(len(row) == first_row_length for row in family):
        raise ValueError("All sublists must have the same length")

    if not isinstance(start, int):
        raise TypeError("start must be an integer")
    if not isinstance(end, int):
        raise TypeError("end must be an integer")

    np_array = array(family)

    print(f"My shape is : {np_array.shape}")

    sliced_array = np_array[start:end]

    print(f"My new shape is : {sliced_array.shape}")

    return sliced_array.tolist()
