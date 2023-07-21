import pytest
from database import generate_exercise_insert_cmd

def test_insert_commands():
    command = generate_exercise_insert_cmd(name="Chest Press", target_area="Chest", difficulty="Hard")
    assert command ==  f"INSERT INTO exercise (name, target_area, difficulty) values ('Chest Press', 'Chest', 'Hard')"
