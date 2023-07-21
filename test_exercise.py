from exercise import Exercise

new_exercise = Exercise(name="New Exercise", target_area="Upper Body", difficulty="Hard")

def test_get_exercise_name():
    assert new_exercise.name

def test_get_target_area():
    assert new_exercise.target_area

def test_create_exercise():
    # TODO: Test SQL INSERT 
    pass

