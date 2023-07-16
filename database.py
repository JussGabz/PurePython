import psycopg2

def database():
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
            id INT PRIMARY KEY, target_area VARCHAR(50) NOT NULL, difficulty VARCHAR(50) NOT NULL);""")

    # Create Workout Plan
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS workoutplan(
            id INT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            exercises VARCHAR(50) NOT NULL,
            workout VARCHAR(50) NOT NULL,
            date_created DATE)
        """)
    
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            id INT PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL,
            date_created DATE)
        """
        )
    
database()