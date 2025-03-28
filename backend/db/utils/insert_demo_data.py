import sys
import os
from datetime import datetime
import hashlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from db.connection import execute_query

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def create_demo_user():
    email = "tickethub@gmail.com"
    password = hash_password("Test123")
    first_name = "Ticket"
    last_name = "Hub"

    # Check if user exists
    user = execute_query("SELECT id FROM users WHERE email = %s", (email,))
    if user:
        print("✅ Utilisateur déjà existant.")
        return user[0][0]

    # Insert new user
    execute_query("""
        INSERT INTO users (email, password, first_name, last_name)
        VALUES (%s, %s, %s, %s)
    """, (email, password, first_name, last_name))

    user_id = execute_query("SELECT id FROM users WHERE email = %s", (email,))[0][0]
    print(f"✅ Utilisateur 'tickethub@gmail.com' créé avec ID: {user_id}")
    return user_id

def insert_demo_ticket(user_id):
    ticket = {
        "numero_ticket": "TICKETDEMO001",
        "date_achat": "2025-03-27 16:45:00",
        "Marque": "DemoBrand",
        "mode_paiement": "CARTE BANCAIRE",
        "produits": [
            {"nom": "Pain complet bio", "quantité": "1", "prix_total": "2.50"},
            {"nom": "Lait d'amande", "quantité": "2", "prix_total": "4.00"},
            {"nom": "Chips artisanales", "quantité": "1", "prix_total": "1.80"}
        ]
    }

    marque = ticket["Marque"]
    execute_query("INSERT INTO marques (nom_marque) VALUES (%s) ON CONFLICT DO NOTHING;", (marque,))

    execute_query("""
        INSERT INTO tickets (num_ticket, user_id, article_count, purchase_date, mode_paiement)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (num_ticket) DO NOTHING;
    """, (
        ticket["numero_ticket"],
        user_id,
        len(ticket["produits"]),
        datetime.strptime(ticket["date_achat"], "%Y-%m-%d %H:%M:%S"),
        ticket["mode_paiement"]
    ))

    for produit in ticket["produits"]:
        prix_total = float(produit["prix_total"])
        quantite = int(produit["quantité"])
        prix_unitaire = prix_total / quantite

        execute_query("""
            INSERT INTO articles (num_ticket, nom_article, prix, quantite, nom_marque)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            ticket["numero_ticket"],
            produit["nom"],
            prix_unitaire,
            quantite,
            marque
        ))

    print("✅ Ticket de démo et produits insérés avec succès.")

if __name__ == "__main__":
    user_id = create_demo_user()
    insert_demo_ticket(user_id)
