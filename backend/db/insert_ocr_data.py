import sys
import os
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from db.connection import execute_query

def insert_ticket_data_user(ocr_data, user_id):
    # 1. Marque
    marque = ocr_data.get('Marque')
    if marque:
        execute_query(
            "INSERT INTO marques (nom_marque) VALUES (%s) ON CONFLICT DO NOTHING;",
            (marque,)
        )

    # 2. Ticket principal
    num_ticket = ocr_data.get('numero_ticket')
    purchase_date = datetime.strptime(ocr_data['date_achat'], "%Y-%m-%d %H:%M:%S")
    article_count = len(ocr_data['produits'])
    mode_paiement = ocr_data.get('mode_paiement')

    execute_query("""
        INSERT INTO tickets (num_ticket, user_id, article_count, purchase_date, mode_paiement)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (num_ticket) DO NOTHING;
    """, (
        num_ticket,
        user_id,
        article_count,
        purchase_date,
        mode_paiement
    ))

    # 3. Articles
    for produit in ocr_data['produits']:
        try:
            prix_total = float(produit['prix_total'])
            quantite = int(produit['quantité'])
            prix_unitaire = prix_total / quantite
            nom_article = produit['nom']
        except Exception as e:
            print(f"[Erreur produit] {produit} : {e}")
            continue

        execute_query("""
            INSERT INTO articles (num_ticket, nom_article, prix, quantite, nom_marque)
            VALUES (%s, %s, %s, %s, %s);
        """, (
            num_ticket,
            nom_article,
            prix_unitaire,
            quantite,
            marque
        ))

    print(f"✅ Ticket {num_ticket} inséré pour user_id {user_id}")
