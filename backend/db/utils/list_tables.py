# Get db's tables name & columns

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connection import execute_query

def get_tables_and_columns():
    query_tables = """
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema='public' AND table_type='BASE TABLE';
    """
    tables = execute_query(query_tables)
    
    table_columns = {}
    for (table_name,) in tables:
        query_columns = """
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_name = %s;
        """
        columns = execute_query(query_columns, (table_name,))
        table_columns[table_name] = columns

    return table_columns

if __name__ == "__main__":
    tables_columns = get_tables_and_columns()
    for table, columns in tables_columns.items():
        print(f"\nTable: {table}")
        for column_name, data_type in columns:
            print(f"  - {column_name} ({data_type})")
