from workoutplan import WorkoutPlan
from exercise import Exercise
import pytest

@pytest.fixture
def new_exercise():
    new_exercise = Exercise(name="New Exercise", target_area="New Target Area", difficulty="Hard")
    return new_exercise

@pytest.fixture
def new_workout_plan(new_exercise):
    new_workout_plan = WorkoutPlan(name="New Workout Plan", exercises=[new_exercise], difficulty="Hard", date_created="Today")
    return new_workout_plan


def test_workoutplan_name(new_workout_plan):
    assert new_workout_plan.get_workoutplan_name() == "New Workout Plan"

def test_workoutplan_difficulty(new_workout_plan):
    assert new_workout_plan.get_difficulty() == "Hard"

def test_workoutplan_exercises(new_workout_plan, new_exercise):
    assert new_workout_plan.get_exercises() == [new_exercise]

def test_workoutplan_creation_date(new_workout_plan):
    assert new_workout_plan.get_date_created() == "Today"

def test_add_exercise(new_workout_plan, new_exercise):
    new_workout_plan.add_exercise(new_exercise)
    assert new_workout_plan.exercises == [new_exercise, new_exercise]
