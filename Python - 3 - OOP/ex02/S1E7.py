from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Baratheon character.

        Args:
            first_name (str): The first name of the character
            is_alive (bool): Whether the character is alive (default: True)
        """
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return string representation of the character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return string representation of the character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Lannister character.

        Args:
            first_name (str): The first name of the character
            is_alive (bool): Whether the character is alive (default: True)
        """
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Return string representation of the character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return string representation of the character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Create a Lannister character using class method.

        Args:
            first_name (str): The first name of the character
            is_alive (bool): Whether the character is alive (default: True)

        Returns:
            Lannister: A new Lannister instance
        """
        return cls(first_name, is_alive)
