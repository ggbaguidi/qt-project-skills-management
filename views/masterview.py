"""Define the master view"""

class MasterView:
    def __init__(self) -> None:
        """no attribut to init"""
        pass

    def input_of_imported_file(self):
        """Demand to user to enter the path of file"""
        filename = input("Enter the path of file : ")
        if filename != None:
            return filename
        return None
    
    @staticmethod
    def decorator(function):
        def wrapper(*args,**kwargs):
            print("\n**************************************\n")
            func = function(*args, **kwargs)
            print("\n--------------------------------------\n")
            return func
        return wrapper
    
    def message_invalid_file_or_path(self,invalid_file_or_path):
        print("Your file isn't valid : {}".format(invalid_file_or_path))
    
    def message_for_valid_file_and_path(self):
        print("Bravo ...... \nYour path and your imported file is valid !!!")

    @decorator
    def display_all_professionnals(self, professionals):
        for professional in professionals:
            print(professional)

    @decorator
    def display_all_profils(self,profils):
        for profil in profils:
            print(profil)
    
    @decorator
    def display_all_skills(self,skills):
        for skill in skills:
            print(skill)

