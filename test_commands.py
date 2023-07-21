import pytest
from database import insert_command

def test_insert_commands():
    command = insert_command(name="Chest Press", target_area="Chest", difficulty="Hard")
    assert command ==  f"INSERT INTO exercise (name, target_area, difficulty) values ('Chest Press', 'Chest', 'Hard')"
