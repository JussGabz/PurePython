from user import User

class WorkoutPlan:
    def __init__(self, name, exercises, difficulty, date_created):
        self.name = name
        self.exercises = exercises
        self.difficulty = difficulty
        self.date_created = date_created
    
    def get_workoutplan_name(self):
        return self.name
    
    def get_exercises(self):
        return self.exercises
    
    def get_difficulty(self):
        return self.difficulty
    
    def get_date_created(self):
        return self.date_created
    
    def add_exercise(self, exercise):
        if self.get_exercises is None:
            if isinstance(exercise, list):
                self.exercises = exercise
            else:
                self.exercises = [exercise]
        self.exercises.append(exercise)
        return self.exercises