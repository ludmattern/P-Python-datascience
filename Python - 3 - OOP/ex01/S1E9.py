from abc import ABC, abstractmethod


class Character(ABC):
    """A character from Game of Thrones."""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a character with a first name and life status.

        Args:
            first_name (str): The first name of the character
            is_alive (bool): Whether the character is alive (default: True)
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Change the health state of the character from alive to dead."""
        self.is_alive = False


class Stark(Character):
    """A member of House Stark."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Stark character.

        Args:
            first_name (str): The first name of the character
            is_alive (bool): Whether the character is alive (default: True)
        """
        super().__init__(first_name, is_alive)
