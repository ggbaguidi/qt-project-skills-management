"""Define of Skills"""

from skill import Skill


class Skills(list):
    """
    The class Skills

    Attrs:
    _skill_number(int): the number of skills
    _list_of_name_skills(list): the list of skill names

    Returns:
    A object of type Skills 
    """
    def __init__(self, _list_of_name_skills) -> None:
        """create the list of skills"""
        super().__init__()
        for _name_skill in _list_of_name_skills:
            self.append(Skill(_name_skill=_name_skill))