def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """Calculates the Body Mass Index (BMI) for given heights and weights.
    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.
    Returns:
        list[int | float]: List of calculated BMI values.
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length.")

    if not all(isinstance(h, (int, float)) and
               not isinstance(h, bool) for h in height):
        raise TypeError("All heights must be numbers.")
    if not all(isinstance(w, (int, float)) and
               not isinstance(w, bool) for w in weight):
        raise TypeError("All weights must be numbers.")

    if any(h == float("inf") or h == float("-inf") or h != h for h in height):
        raise ValueError("Heights cannot be infinite or NaN.")
    if any(w == float("inf") or w == float("-inf") or w != w for w in weight):
        raise ValueError("Weights cannot be infinite or NaN.")

    bmi = []
    for h, w in zip(height, weight):
        if h <= 0:
            raise ValueError("Height must be greater than zero.")
        if w <= 0:
            raise ValueError("Weight must be greater than zero.")
        bmi_value = w / (h**2)
        bmi.append(bmi_value)

    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Applies a limit to the BMI values.
    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): The limit to apply.
    Returns:
        list[bool]: List indicating whether each BMI value is above the limit.
    """
    if not isinstance(limit, int) or isinstance(limit, bool):
        raise TypeError("Limit must be an integer.")
    if limit <= 0:
        raise ValueError("Limit must be greater than zero.")
    if not all(isinstance(value, (int, float)) and
               not isinstance(value, bool) for value in bmi):
        raise TypeError("All BMI values must be numbers.")

    if any(value == float("inf") or value == float("-inf") or
           value != value for value in bmi):
        raise ValueError("BMI values cannot be infinite or NaN.")
    return [value > limit for value in bmi]
