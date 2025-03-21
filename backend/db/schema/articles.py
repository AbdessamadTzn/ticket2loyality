def create_articles_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id_article SERIAL PRIMARY KEY,
        num_ticket TEXT REFERENCES tickets(num_ticket) ON DELETE CASCADE,
        nom_article TEXT NOT NULL,
        prix DECIMAL(10, 2),
        quantite INTEGER DEFAULT 1,
        nom_marque TEXT REFERENCES marques(nom_marque)
    );
    """)
