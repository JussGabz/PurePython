from database import database
from exercise import Exercise, retrieve_exercise, delete_exercise, change_exercise



def mainmenu():
    response = input("Which option do you want to go for?\n1) Exercise\n2) Workout Plan\nOption: ")

    if response == '1':
        print("Exercise!")
        exercise_menu()
    elif response == '2':
        print("Workout Plan!")


def exercise_menu():
    print(
        """What do you want to do?
        1) Create
        2) View Exercise
        3) Remove Exercise
        4) Update Exercise""")
    exercise_opt = input("Option: ")

    if exercise_opt == "1":
        create_exercise()
    elif exercise_opt == "2":
        view_exercise()
    elif exercise_opt == "3":
        remove_exercise()
    elif exercise_opt == "4":
        update_exercise()



def workout_plan_menu():
    # TODO - Add functionality for WorkOut Plan
    pass


def create_exercise():
    exercise_name = input("Exercise Name?: ")
    target_area = input("What area of the body is this targeting?: ")
    difficulty = input("How difficult is this exercise?: ")

    valid = input(
        f"Is this correct? Exercise: {exercise_name}, Target Area: {target_area}, Difficulty, {difficulty}? "
    )
    if valid == "Y" or "y":
        print("Confirmed")
        exercise = Exercise(exercise_name, target_area, difficulty)
        exercise.save_exercise()
    elif valid == "N" or "n":
        mainmenu()

def view_exercise():
    exercise_name = input("What exercise do you request? ")
    exercises = retrieve_exercise(exercise_name)
    for exercise in exercises:
        id, name, target_area, difficulty = exercise
        print("___________________________")
        print("ID:", id)
        print("Name:", name)
        print("Target Area:", target_area)
        print("Difficulty:", difficulty)
        print("___________________________")

def remove_exercise():
    # search for exercise in database
    exercise_name = input("What exercise do you want to delete? ")
    exercise = retrieve_exercise(exercise_name)

    # If result found in database.. Delete from database
    if exercise:
        delete_exercise(exercise_name)
    else:
        print("No Exercise Found!")

def update_exercise():
    # Search Exercise in Database exists
    exercise_name = input("What exercise do you want to update?: ")
    new_exercise = input("What is the new exercise name you want?: ")
    exercise = retrieve_exercise(exercise_name)

    for ex in exercise:
        if ex:
            change_exercise(exercise_name, new_exercise)

# Run Database Setup
database()
mainmenu()









    




