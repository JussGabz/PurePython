from database import insert, select, delete

class Exercise:

    '''
    Class for Exercise Workout 
    '''

    def __init__(self, name: str, target_area: str, difficulty: str):
        self.name = name
        self.target_area = target_area
        self.difficulty = difficulty

    def get_exercise_name(self):
        return self.name

    def get_target_area(self):
        return self.target_area
    
    def save_exercise(self):
        insert(self.name, self.target_area, self.difficulty)
    

        

def retrieve_exercise(name):
    return select(name)

def delete_exercise(name):
    delete(name)
