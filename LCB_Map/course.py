from game_data import COURSE_DATA, UNIVERSITY_PARTNERS
from random import choice

class Course:
    def __init__(self, name):
        self.name = name
        
        # Get course data
        course_info = COURSE_DATA[name]
        self.university = course_info['university']
        self.duration = course_info['duration']
        self.element = course_info['element']
        self.description = course_info['description']
        self.modules = course_info['modules']
        self.entry_requirements = course_info['entry_requirements']
        self.career_prospects = course_info['career_prospects']
        
        # Random enrollment data for display
        self.current_students = choice([150, 200, 180, 220, 175, 190])
        self.satisfaction_rating = choice([4.2, 4.5, 4.3, 4.7, 4.1, 4.4])
    
    def get_modules_list(self):
        # Return all modules as a list
        all_modules = []
        for year, modules in self.modules.items():
            all_modules.extend([f"{year}: {module}" for module in modules])
        return all_modules
    
    def get_requirements_list(self):
        # Return entry requirements as a list
        return [f"{key}: {value}" for key, value in self.entry_requirements.items()]