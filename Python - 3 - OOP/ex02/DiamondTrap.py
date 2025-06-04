from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A King character inheriting from both Baratheon and Lannister."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a King character.

        Args:
            first_name (str): The first name of the character
            is_alive (bool): Whether the character is alive (default: True)
        """
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes: str):
        """Set the eye color of the character."""
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        """Set the hair color of the character."""
        self.hairs = hairs

    def get_eyes(self):
        """Return the eye color of the character."""
        return self.eyes

    def get_hairs(self):
        """Return the hair color of the character."""
        return self.hairs
