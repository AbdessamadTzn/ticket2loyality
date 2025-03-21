def create_tickets_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        num_ticket TEXT PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        nbr_articl TEXT,
        purchase_date TIMESTAMP,                     -- la date sur le ticket
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- date d’enregistrement dans la BDD
    );
    """)
