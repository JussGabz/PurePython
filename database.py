import psycopg2
from psycopg2 import OperationalError

def database():

    print("Set Up GymApp Database..")
    try:
        # Connect to Postgres DB
        conn = psycopg2.connect(
            database="postgres", user="postgres", password="admin")
        
        conn.autocommit = True
        
        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Check If Database exists
        cur.execute("""
                    SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'gymapp'
                    """)
        
        exists = cur.fetchone()

        if not exists:
            # Create initial GYM APP Database
            cur.execute("CREATE DATABASE gymapp")

        # Connect to Postgres DB
        conn = psycopg2.connect(
            database="gymapp", user="postgres", password="admin")
        
        # Open a cursor to perform database operations
        cur = conn.cursor()
        conn.autocommit = True

        # Create Exercise Table
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS exercise(
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                target_area VARCHAR(50) NOT NULL,
                difficulty VARCHAR(50) NOT NULL);""")

        # Create Workout Plan
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS workoutplan(
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                exercises VARCHAR(50) NOT NULL,
                workout VARCHAR(50) NOT NULL,
                date_created DATE)
            """)
        
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                username VARCHAR(50) NOT NULL,
                password VARCHAR(50) NOT NULL,
                date_created DATE)
            """
            )
        print("GymApp Database Set up Successfully..")
    except OperationalError as e:
        print(f"Error: {e}")


def generate_exercise_insert_cmd(name:str, target_area:str, difficulty:str):
    sql_command = f"INSERT INTO exercise (name, target_area, difficulty) values ('{name}', '{target_area}', '{difficulty}')"
    return sql_command
    
def generate_exercise_select_cmd(name):
    if name != "":
        sql_command = f"SELECT * FROM exercise WHERE name = '{name}'"
    else:
        sql_command = f"SELECT * FROM exercise" 
    return sql_command

def generate_exercise_delete_cmd(name):
    sql_command = f"DELETE FROM exercise WHERE name = '{name}'"
    return sql_command

def generate_exercise_update_cmd(name, new_name):
    sql_command = f"UPDATE exercise SET name = '{new_name}' WHERE name = '{name}'"
    return sql_command

def insert(name:str , target_area:str, difficulty:str):

    sql_command = generate_exercise_insert_cmd(name, target_area, difficulty)

    # Connect Database
    try:
        conn = psycopg2.connect(
        database="gymapp", user="postgres", password="admin")

        cur = conn.cursor()

        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        print("Data Inserted")
    except OperationalError as e:
        print(f"Error: {e}")

def select(name):
    sql_command = generate_exercise_select_cmd(name)

    # Connect Database
    try:
        conn = psycopg2.connect(
        database="gymapp", user="postgres", password="admin")

        cur = conn.cursor()

        cur.execute(sql_command)
        selected_exercise = cur.fetchall()

        cur.close()
        conn.close()
        print("Data Selected")
    except OperationalError as e:
        print(f"Error: {e}")
    
    return selected_exercise

def delete(name):
    sql_command = generate_exercise_delete_cmd(name)

    # Connect Database
    try:
        conn = psycopg2.connect(
        database="gymapp", user="postgres", password="admin")

        cur = conn.cursor()

        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        print("Data Deleted")
    except OperationalError as e:
        print(f"Error: {e}")

def update(name, new_name):

    sql_command = generate_exercise_update_cmd(name, new_name)

    # Connect Database
    try:
        conn = psycopg2.connect(
        database="gymapp", user="postgres", password="admin")

        cur = conn.cursor()

        cur.execute(sql_command)
        conn.commit()

        cur.close()
        conn.close()
        print("Data Updated")
    except OperationalError as e:
        print(f"Error: {e}")






