import pytest
import psycopg2
from database import generate_exercise_insert_cmd, insert, database

def test_insert_commands():
    command = generate_exercise_insert_cmd(name="Chest Press", target_area="Chest", difficulty="Hard")
    assert command ==  f"INSERT INTO exercise (name, target_area, difficulty) values ('Chest Press', 'Chest', 'Hard')"

def test_example_postgres(postgresql_db):
    """ Check Postgres Fixture """
    cur = postgresql_db.cursor()
    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    cur.close()

def test_create_exercise_table(mocker):
    
    mock_cursor = mocker.Mock()
    mock_connect = mocker.patch('psycopg2.connect')

    mock_connect.return_value.__enter__value = mock_cursor

    database()

    mock_connect.assert_called_once_with(database="gymapp", user="postgres", password="postgres", host="loclhost")




