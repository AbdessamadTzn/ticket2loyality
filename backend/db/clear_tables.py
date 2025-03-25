import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connection import execute_query

def clear_all_tables():
    query = """
    TRUNCATE TABLE articles RESTART IDENTITY CASCADE;
    TRUNCATE TABLE tickets RESTART IDENTITY CASCADE;
    TRUNCATE TABLE marques RESTART IDENTITY CASCADE;
    TRUNCATE TABLE users RESTART IDENTITY CASCADE;
    """
    execute_query(query)
    print("Tables cleared successfully!")

if __name__ == "__main__":
    clear_all_tables()
