from database import database, insert

# Run Database Setup
database()

response = input("Do you want to create an exercise?: ")

def start():
    exercise_name = input("Exercise Name?: ")
    target_area = input("What area of the body is this targeting?: ")
    difficulty = input("How difficult is this exercise?: ")

    valid = input(
        f"Is this correct? Exercise: {exercise_name}, Target Area: {target_area}, Difficulty, {difficulty}?"
    )
    if valid == "Y" or "y":
        print("Confirmed")
        insert(exercise_name, target_area, difficulty)
    elif valid == "N" or "n":
        start()
    


if response == "Y" or "y":
    start()




    




