"""Define of Profil"""

from models.skills import Skills


class Profil:
    """
    The class Profil

    Attrs:
    _name_profil(str): the name of the profil
    _skill_number(int): the number of skills
    _list_of_name_skills(list): the list of skills name

    Returns:
    A object of type Profil
    """
    def __init__(self, 
                 _name_profil, 
                 _skill_number,
                 _list_of_name_skills) -> None:
        """
        init the name of the profil, the numbre of skills and the list
        of the skills
        """
        self.name_profil = _name_profil
        self.skill_number = _skill_number
        self.skills = Skills(_list_of_name_skills)

    def __str__(self) -> str:
        """Used in print."""
        return f"name_profil: {self.name_profil}"
    
    def __repr__(self) -> str:
        """Used in print."""
        return str(self)

    