def create_users_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        first_name TEXT,
        last_name TEXT,
        num_ticket TEXT REFERENCES tickets(num_ticket),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
