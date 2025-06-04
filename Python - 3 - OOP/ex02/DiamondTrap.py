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

    def get_eyes(self):
        """Get the eye color of the character."""
        return self._eyes

    def set_eyes(self, value: str):
        """Set the eye color of the character."""
        self._eyes = value

    def get_hairs(self):
        """Get the hair color of the character."""
        return self._hairs

    def set_hairs(self, value: str):
        """Set the hair color of the character."""
        self._hairs = value

    eyes = property(
        fget=get_eyes,
        fset=set_eyes,
        doc="The eye color property."
    )

    hairs = property(
        fget=get_hairs,
        fset=set_hairs,
        doc="The hair color property."
    )
