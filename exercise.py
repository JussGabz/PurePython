from database import insert

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
    
    def create_exercise(self):
        insert(
            name=self.name,
            target_area=self.target_area,
            difficulty=self.difficulty
        )
