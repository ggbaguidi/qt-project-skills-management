"""Define the Controller"""

import os
from controllers.filemanager import FileManager
from views.masterview import MasterView


class Controller:
    """init base controller"""
    def __init__(self) -> None:
        self.view = MasterView()
        self.imported_file = self.view.input_of_imported_file().strip()
        self.is_not_valid_file = True
        self.filemanager = FileManager()
        
    def is_valid_file_path(self):
        if os.path.exists(self.imported_file):
            return True
        return False
    
    def is_valid_file_name(self):
        if self.imported_file.endswith(".cpt"):
            return True
        return False

    def run(self):
        while(self.is_not_valid_file):
            if (self.is_valid_file_name() and self.is_valid_file_path()):
                self.view.message_for_valid_file_and_path()
                self.filemanager = FileManager(self.imported_file)
                self.filemanager.extract_all_list_from_file()
                self.is_not_valid_file = False
            else:
                self.view.message_invalid_file_or_path(self.imported_file)
                self.imported_file = self.view.input_of_imported_file().strip()
        self.view.display_all_professionnals(self.filemanager.professionals)
        self.view.display_all_profils(self.filemanager.profils)
        self.view.display_all_skills(self.filemanager.skills)

        self.filemanager.professionals[0].skills.delete_existed_skill("Excel")
        for skill in self.filemanager.professionals[0].skills:
            print(skill)