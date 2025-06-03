def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    """ Calculates the Body Mass Index (BMI) for given heights and weights.
    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.
    Returns:
        list[int | float]: List of calculated BMI values.
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length.")

    if not all(isinstance(h, (int, float)) for h in height):
        raise TypeError("All heights must be numbers.")
    if not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("All weights must be numbers.")

    bmi = []
    for h, w in zip(height, weight):
        if h <= 0:
            raise ValueError("Height must be greater than zero.")
        bmi_value = w / (h ** 2)
        bmi.append(bmi_value)

    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ Applies a limit to the BMI values.
    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): The limit to apply.
    Returns:
        list[bool]: List indicating whether each BMI value is above the limit.
    """
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")
    if limit <= 0:
        raise ValueError("Limit must be greater than zero.")
    if not all(isinstance(value, (int, float)) for value in bmi):
        raise TypeError("All BMI values must be numbers.")
    return [value > limit for value in bmi]
