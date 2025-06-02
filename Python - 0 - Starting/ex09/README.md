# ft_package

A sample test package for learning Python package creation.

## Installation

You can install this package using pip:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

or

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

```python
from ft_package import count_in_list

# Count occurrences of an item in a list
result = count_in_list(["toto", "tata", "toto"], "toto")
print(result)  # Output: 2

result = count_in_list(["toto", "tata", "toto"], "tutu")
print(result)  # Output: 0
```

## Functions

### count_in_list(lst, item)

Count the number of occurrences of an item in a list.

**Parameters:**
- `lst` (list): The list to search in
- `item`: The item to count

**Returns:**
- `int`: The number of occurrences of the item in the list

**Examples:**
```python
count_in_list(["apple", "banana", "apple"], "apple")  # Returns: 2
count_in_list([1, 2, 3, 1, 1], 1)  # Returns: 3
count_in_list(["hello", "world"], "goodbye")  # Returns: 0
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- **eagle** - eagle@42.fr
