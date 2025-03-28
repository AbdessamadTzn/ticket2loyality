import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_connection():
    """Create and return a connection to the PostgreSQL database."""
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return conn

def execute_query(query, params=None):
    """Execute a query and return results if it's a SELECT or contains RETURNING."""
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            # Check if query is SELECT or contains RETURNING
            query_upper = query.strip().upper()
            if query_upper.startswith('SELECT') or 'RETURNING' in query_upper:
                return cur.fetchall()
            conn.commit()
            return None
    finally:
        conn.close()