import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15-character string of lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Class representing a student with a unique
    ID and login based on name and surname."""
    name: str
    surname: str
    active: bool = field(default=True, init=False)
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Post-initialization to set the login attribute."""
        self.login = (self.name[0] + self.surname).capitalize()
