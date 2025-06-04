class calculator:
    """Calculator class for vector-scalar operations.

    This class performs mathematical operations between a vector
    (list of numbers) and a scalar (single number).
    """

    def __init__(self, object) -> None:
        """Initialize the calculator with a vector.

        Args:
            object: A list of numbers representing the vector.
        """
        self.object = object

    def __add__(self, object) -> None:
        """Add a scalar to each element of the vector.

        Args:
            object: The scalar value to add to each vector element.
        """
        self.object = [x + object for x in self.object]
        print(self.object)

    def __mul__(self, object) -> None:
        """Multiply each element of the vector by a scalar.

        Args:
            object: The scalar value to multiply with each vector element.
        """
        self.object = [x * object for x in self.object]
        print(self.object)

    def __sub__(self, object) -> None:
        """Subtract a scalar from each element of the vector.

        Args:
            object: The scalar value to subtract from each vector element.
        """
        self.object = [x - object for x in self.object]
        print(self.object)

    def __truediv__(self, object) -> None:
        """Divide each element of the vector by a scalar.

        Args:
            object: The scalar value to divide each vector element by.

        Raises:
            ZeroDivisionError: If the scalar is zero.
        """
        if object == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self.object = [x / object for x in self.object]
        print(self.object)
