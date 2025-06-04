from pandas import read_csv, errors as p_errors, DataFrame


def load(path: str) -> DataFrame | None:
    """
    Load a CSV dataset from the given path.

    Args:
        path (str): Path to the CSV file

    Returns:
        DataFrame: The loaded dataset if successful, None if error
    """
    try:
        if not path:
            print("Error: The path cannot be empty.")
            return None
        if not path.lower().endswith(".csv"):
            print(f"Error: File '{path}' is not a CSV file.")
            return None

        dataset = read_csv(path)

        if dataset.empty:
            print(f"Error: The dataset '{path}' is empty.")
            return None

        rows, cols = dataset.shape
        print(f"Loading dataset of dimensions ({rows}, {cols})")

        return dataset

    except p_errors.EmptyDataError:
        print(f"Error: The file '{path}' is empty or has no data.")
        return None
    except p_errors.ParserError as e:
        print(f"Error: Unable to parse the CSV file '{path}'. {str(e)}")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read file '{path}'.")
        return None
    except FileNotFoundError:
        print(f"Error: The file '{path}' does not exist.")
        return None
    except Exception as e:
        print(f"Error: Unexpected error occurred '{path}'. {str(e)}")
        return None
