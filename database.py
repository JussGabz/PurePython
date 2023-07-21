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


def insert_command(name, target_area, difficulty):
    sql_command = f"INSERT INTO exercise (name, target_area, difficulty) values ('{name}', '{target_area}', '{difficulty}')"
    return sql_command
    
def insert(name:str , target_area:str, difficulty:str):

    sql_command = f"INSERT INTO exercise (name, target_area, difficulty) values ('{name}', '{target_area}', '{difficulty}')"

    # Connect Database
    try:
        conn = psycopg2.connect(
        database="gymapp", user="postgres", password="admin")

        cur = conn.cursor()

        cur.execute(sql_command)
        conn.commit()
        conn.close()
        print("Data Inserted")
    except OperationalError as e:
        print(f"Error: {e}")