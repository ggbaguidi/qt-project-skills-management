"""Define the Controller"""

import re
from typing import List

from models.skill import Skill
from models.profil import Profil
from models.professional import Professional


class Controller:
    def __init__(self) -> None:
        """init the lists of skills, professionals and profils"""
        self.skills: List[Skill] = []
        self.profils: List[Profil] = []
        self.professionals: List[Professional] = []