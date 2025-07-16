from game_data import COURSE_DATA
from random import randint

class Course:
    def __init__(self, name):
        self.name = name

        # Stats and Modules
        self.department = COURSE_DATA[name]['stats']['department']
        self.modules = COURSE_DATA[name]['modules']
        self.entry_req = COURSE_DATA[name]['entry_req']

    def get_stat(self, module):
        return self.modules[module]

    def get_stats(self):
        return{
            'modules_list': self.get_stat('list')
        }
    
