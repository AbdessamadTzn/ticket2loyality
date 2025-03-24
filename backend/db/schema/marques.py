def create_marques_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS marques (
        nom_marque TEXT PRIMARY KEY,
        secteur TEXT,
        pays TEXT
    );
    """)