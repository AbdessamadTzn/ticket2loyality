import sys
import os

# Add parent directory to path to correctly import connection.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connection import execute_query

query = """
ALTER TABLE tickets 
RENAME COLUMN nbr_articl TO nbr_article;

"""

execute_query(query)
print("Migration completed successfully.")
