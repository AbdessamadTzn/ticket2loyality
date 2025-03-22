import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables
load_dotenv()

def test_db_connection():
    """Test connection to PostgreSQL database and return status message."""
    try:
        # Attempt to establish connection
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        
        # Get server version to verify connection
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        
        # Close connection
        cur.close()
        conn.close()
        
        return f"Connection successful! PostgreSQL version: {db_version[0]}"
        
    except Exception as e:
        return f"Connection failed: {str(e)}"

if __name__ == "__main__":
    print(test_db_connection())