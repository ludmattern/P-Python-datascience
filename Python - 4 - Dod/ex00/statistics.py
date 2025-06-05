from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate various statistics on provided data.
    Uses only Python built-in functions.
    """

    def validate_number(value):
        """Raise ValueError if number is inf or NaN"""
        if abs(value) == float("inf") or value != value:
            raise ValueError("Invalid number: inf or NaN")

    def validate_data():
        """Validate and convert input data"""
        if not args:
            return None
        data = [float(x) for x in args]
        for value in data:
            validate_number(value)
        return data

    def calculate_mean(data):
        """Calculate mean using sum() and len()"""
        total = sum(data)
        validate_number(total)
        result = total / len(data)
        validate_number(result)
        return result

    def calculate_median(data):
        """Calculate median using sorted()"""
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        return sorted_data[n // 2]

    def interpolate_quantile(sorted_data, index):
        """Linear interpolation for quantile calculation."""
        n = len(sorted_data)
        lower_index = int(index)
        upper_index = lower_index + 1

        if upper_index >= n:
            return sorted_data[lower_index]

        weight = index - lower_index
        val1 = sorted_data[lower_index] * (1 - weight)
        val2 = sorted_data[upper_index] * weight
        validate_number(val1)
        validate_number(val2)

        result = val1 + val2
        validate_number(result)
        return result

    def calculate_quartiles(data):
        """Calculate Q1 and Q3 with interpolation"""
        sorted_data = sorted(data)
        n = len(sorted_data)

        q1_index = (n - 1) * 0.25
        q3_index = (n - 1) * 0.75

        q1 = interpolate_quantile(sorted_data, q1_index)
        q3 = interpolate_quantile(sorted_data, q3_index)

        return [q1, q3]

    def calculate_variance(data):
        """Calculate variance using sum() and len()"""
        mean = calculate_mean(data)

        squared_diffs = []
        for x in data:
            diff = x - mean
            squared_diff = diff**2
            validate_number(squared_diff)
            squared_diffs.append(squared_diff)

        total_squared_diffs = sum(squared_diffs)
        validate_number(total_squared_diffs)

        result = total_squared_diffs / len(data)
        validate_number(result)
        return result

    def calculate_std(data):
        """Calculate standard deviation using ** 0.5 (square root)"""
        variance = calculate_variance(data)
        if variance < 0:
            raise ValueError("Negative variance")
        result = variance**0.5
        validate_number(result)
        return result

    stats_functions = {
        "mean": calculate_mean,
        "median": calculate_median,
        "quartile": calculate_quartiles,
        "var": calculate_variance,
        "std": calculate_std
        }

    for key, requested_stat in kwargs.items():
        if requested_stat in stats_functions:
            try:
                data = validate_data()
                if data is None:
                    print("ERROR")
                else:
                    result = stats_functions[requested_stat](data)
                    print(f"{requested_stat} : {result}")
            except (OverflowError, ZeroDivisionError,
                    ValueError, TypeError, IndexError):
                print("ERROR")
