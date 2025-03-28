from connection import execute_query
from datetime import datetime

def insert_demo_data():
    # 1. Insérer l'utilisateur de test
    execute_query("""
    INSERT INTO users (email, password) 
    VALUES ('tickethub@gmail.com', 'Test123')
    ON CONFLICT (email) DO UPDATE 
    SET password = EXCLUDED.password
    RETURNING id;
    """)

    # 2. Insérer les marques
    marques = ['Pringles', 'Mango', 'Puma', 'Samsung', 'Sodebo', 'Candia']
    for marque in marques:
        execute_query("""
        INSERT INTO marques (nom_marque) 
        VALUES (%s)
        ON CONFLICT (nom_marque) DO NOTHING;
        """, (marque,))

    # 3. Insérer quelques tickets avec leurs articles
    tickets_data = [
        {
            "num_ticket": "DEMO001",
            "date": datetime.now(),
            "marque": "Pringles",
            "articles": [
                {"nom": "Pringles Original", "prix": 2.99, "quantite": 2},
                {"nom": "Pringles Paprika", "prix": 2.99, "quantite": 1}
            ]
        },
        {
            "num_ticket": "DEMO002",
            "date": datetime.now(),
            "marque": "Sodebo",
            "articles": [
                {"nom": "Pizza Sodebo", "prix": 3.99, "quantite": 2},
                {"nom": "Salade César", "prix": 4.50, "quantite": 1}
            ]
        },
        {
            "num_ticket": "DEMO003",
            "date": datetime.now(),
            "marque": "Candia",
            "articles": [
                {"nom": "Lait Candia", "prix": 1.29, "quantite": 3},
                {"nom": "Crème Candia", "prix": 2.19, "quantite": 1}
            ]
        }
    ]

    # Récupérer l'ID de l'utilisateur
    user_result = execute_query("""
    SELECT id FROM users WHERE email = 'tickethub@gmail.com';
    """)
    user_id = user_result[0][0] if user_result else None

    # Insérer les tickets et leurs articles
    for ticket in tickets_data:
        execute_query("""
        INSERT INTO tickets (num_ticket, user_id, purchase_date)
        VALUES (%s, %s, %s)
        ON CONFLICT (num_ticket) DO NOTHING;
        """, (ticket["num_ticket"], user_id, ticket["date"]))

        for article in ticket["articles"]:
            execute_query("""
            INSERT INTO articles (num_ticket, nom_article, prix, quantite, nom_marque)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING;
            """, (
                ticket["num_ticket"],
                article["nom"],
                article["prix"],
                article["quantite"],
                ticket["marque"]
            ))

    print("✅ Données de démonstration insérées avec succès!")

if __name__ == "__main__":
    insert_demo_data() 