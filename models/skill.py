"""Define the Skill"""

class Skill:
    """
    The class Skill

    Attrs:
    _name_skill(str): the name of the skill

    Returns:
    A object of type Skill
    """
    def __init__(self, _name_skill) -> None:
        """init the name of skill."""
        self.name_skill = _name_skill

    def __str__(self) -> str:
        """Used in print."""
        return f"name_skill: {self.name_skill}"
    
    def __repr__(self) -> str:
        """Used in print."""
        return str(self)