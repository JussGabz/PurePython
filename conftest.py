import pytest 
import psycopg2

@pytest.fixture(scope="session")
def postgresql_db():
    dbname = "test_gymapp"
    user = "postgres"
    password = "admin"
    host = "localhost"
    port = "5432"

    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port)
    
    yield conn

    # Clean up after the tests are done

    conn.close()