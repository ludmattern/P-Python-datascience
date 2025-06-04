class calculator:
    """Calculator class for vector-vector operations.

    This class performs mathematical operations between two vectors
    (lists of numbers) of identical sizes.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors.

        Args:
            V1: First vector (list of floats).
            V2: Second vector (list of floats).
        """
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors element-wise.

        Args:
            V1: First vector (list of floats).
            V2: Second vector (list of floats).
        """
        result = [x + y for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract the second vector from the first vector element-wise.

        Args:
            V1: First vector (list of floats).
            V2: Second vector (list of floats).
        """
        result = [x - y for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
