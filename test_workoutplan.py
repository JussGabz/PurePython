from workoutplan import WorkoutPlan


new_wo_plan = WorkoutPlan(name="New Workout Plan", exercises=[], difficulty="Hard", date_created="Today")

def test_workoutplan_name():
    assert new_wo_plan.get_workoutplan_name() == "New Workout Plan"

def test_workoutplan_difficulty():
    assert new_wo_plan.get_difficulty() == "Hard"

def test_workoutplan_exercises():
    assert new_wo_plan.get_exercises() == []

def test_workoutplan_creation_date():
    assert new_wo_plan.get_date_created() == "Today"




              