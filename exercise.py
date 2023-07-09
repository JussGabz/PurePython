class Exercise:

    '''
    Class for Exercise Workout 
    '''

    def __init__(self, name: str, target_area: str):
        self.name = name
        self.target_area = target_area

    def get_exercise_name(self):
        return self.name

    def get_target_area(self):
        return self.target_area