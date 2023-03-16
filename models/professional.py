"""Define of Professional"""

from skills import Skills


class Professional:
    """
    The class Professional

    Attrs:
    _firstname_professional(str): the firstname of the professional
    _surname_professional(str): the surname of the professional
    _skill_number(int): the number of skills
    _list_of_name_skills(list): the list of skills name

    Returns:
    A object of type Professional
    """
    def __init__(self, 
                 _firstname_professional, 
                 _surname_professional, 
                 _skill_number,
                 _list_of_name_skills) -> None:
        """
        init the firstname and surname of the professional, the number of
        skills, the list of the name of skills
        """
        self.firstname_professional = _firstname_professional
        self.surname_professional = _surname_professional
        self.skill_number = _skill_number
        self.skills = Skills(_list_of_name_skills)

    def __str__(self) -> str:
        """Used in print."""
        return f"{self.firstname_professional} {self.surname_professional}"
                
    def __repr__(self) -> str:
        """Used in print."""
        return str(self)