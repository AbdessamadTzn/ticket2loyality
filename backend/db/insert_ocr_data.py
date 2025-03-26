import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from db.connection import execute_query
from datetime import datetime

def insert_ticket_data_user(ocr_data, user_id):
    marque = ocr_data['Marque']
    execute_query(
        "INSERT INTO marques (nom_marque) VALUES (%s) ON CONFLICT DO NOTHING;",
        (marque,)
    )

    num_ticket = ocr_data['numero_ticket']  # ✅ Corrected here!
    purchase_date = datetime.strptime(ocr_data['date_achat'], "%Y-%m-%d %H:%M:%S")
    mode_paiement = ocr_data.get('mode_paiement')

    execute_query("""
        INSERT INTO tickets (num_ticket, user_id, article_count, purchase_date, mode_paiement)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (num_ticket) DO NOTHING;
    """, (
        num_ticket,
        user_id,
        len(ocr_data['produits']),
        purchase_date,
        mode_paiement
    ))

    for produit in ocr_data['produits']:
        prix_total = float(produit['prix_total'])
        quantite = int(produit['quantité'])
        prix_unitaire = prix_total / quantite

        execute_query("""
            INSERT INTO articles (num_ticket, nom_article, prix, quantite, nom_marque)
            VALUES (%s, %s, %s, %s, %s);
        """, (
            num_ticket,
            produit['nom'],
            prix_unitaire,
            quantite,
            marque
        ))
