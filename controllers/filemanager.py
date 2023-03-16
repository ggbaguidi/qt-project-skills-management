"""Define the file manager"""

import re
from typing import List

from models.skill import Skill
from models.profil import Profil
from models.professional import Professional

SPLIT_CHARATERS = '\t|:|\n'
SURNAME_PROFESSIONAL_POSITION = 1
FIRSTNAME_PROFESSIONAL_POSITION = 2
SKILL_NUMBER_POSITION_PROFESSIONAL = 3
NAME_PROFIL_POSITION = 1
SKILL_NUMBER_POSITION_PROFIL = 2 
SKILL_NUMBER_POSITION_SKILL = 1

class FileManager:
    def __init__(self,_imported_file_name="data/sample.cpt") -> None:
        """
        init the imported file name,
        the lists of skills, professionals and profils
        """
        self.imported_file_name = _imported_file_name
        self.skills: List[Skill] = []
        self.profils: List[Profil] = []
        self.professionals: List[Professional] = []
    
    def add_profil(self, new_profil):
        """add a new profil at profils"""
        self.profils.append(new_profil)
    
    def add_professional(self, new_professional):
        """add new professional at professionals"""
        self.professionals.append(new_professional)
    
    def add_skill(self,new_skill):
        """add new skill at skills"""
        self.skills.append(new_skill)

    def extract_all_list_from_file(self):
        """open the file in mode read"""
        with open(self.imported_file_name, "r") as opened_file:
            ind = 0
            rows = opened_file.readlines()
            all_skill_names = []
            while(ind<len(rows)):
                """
                extract the profils (PFL)
                extract the professionals (PRO)
                extract the skills (CPT)[all skills]
                
                """
                if (rows[ind].splitlines()[0].strip(SPLIT_CHARATERS) == "PFL"):
                    is_name_profil = str(rows[ind+NAME_PROFIL_POSITION]
                                         .splitlines()[0]
                                         .strip(SPLIT_CHARATERS))
                    is_skill_number = int(rows[ind+SKILL_NUMBER_POSITION_PROFIL]
                                          .splitlines()[0]
                                          .strip(SPLIT_CHARATERS)
                                        )
                    ind += 3
                    is_skills = [
                        rows[ind+cpt].splitlines()[0].strip(SPLIT_CHARATERS)
                        for cpt in range(is_skill_number)
                    ]
                    self.add_profil(Profil(
                        is_name_profil,
                        is_skill_number,
                        sorted(is_skills)
                    ))
                    all_skill_names.extend(is_skills)
                    del is_skills
                    ind += is_skill_number
  
                elif(rows[ind].splitlines()[0].strip(SPLIT_CHARATERS) == "PRO"):
                    is_surname_professional = str(rows[ind
                                                       +SURNAME_PROFESSIONAL_POSITION
                                                    ]
                                                    .splitlines()[0]
                                                    .strip(SPLIT_CHARATERS))
                    is_firstname_professional = str(rows[ind
                                                        +FIRSTNAME_PROFESSIONAL_POSITION
                                                    ]
                                                    .splitlines()[0]
                                                    .strip(SPLIT_CHARATERS))
                    is_skill_number = int(rows[ind
                                               +SKILL_NUMBER_POSITION_PROFESSIONAL
                                            ]
                                          .splitlines()[0]
                                          .strip(SPLIT_CHARATERS)
                                        )
                    ind += 4
                    is_skills = [
                        rows[ind+cpt].splitlines()[0].strip(SPLIT_CHARATERS)
                        for cpt in range(is_skill_number)
                    ]
                    self.add_professional(Professional(
                        is_firstname_professional,
                        is_surname_professional,
                        is_skill_number,
                        is_skills
                    ))
                    #all_skill_names.extend(is_skills)
                    del is_skills
                    ind += is_skill_number

                elif(rows[ind].splitlines()[0].strip(SPLIT_CHARATERS) == "CPT"):
                    is_skill_number = int(rows[ind
                                               +SKILL_NUMBER_POSITION_SKILL
                                            ]
                                          .splitlines()[0]
                                          .strip(SPLIT_CHARATERS)
                                        )
                    ind += 2
                    for cpt in range(is_skill_number):
                        all_skill_names.append(
                            rows[ind+cpt].splitlines()[0].strip(SPLIT_CHARATERS)
                        )
                    ind += is_skill_number

                else:
                    ind += 1
            for skill_name in set(all_skill_names):
                self.add_skill(Skill(
                    skill_name
                ))
            del all_skill_names