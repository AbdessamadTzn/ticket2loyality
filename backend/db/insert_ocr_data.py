import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.connection import execute_query  # clearly indicate the correct relative import
from datetime import datetime

def insert_ticket_data(ocr_data):
    # Insert marque if not exists
    marque = ocr_data['Marque']
    execute_query(
        "INSERT INTO marques (nom_marque) VALUES (%s) ON CONFLICT DO NOTHING;",
        (marque,)
    )

    # Insert ticket data
    num_ticket = ocr_data['numero_ticket']
    purchase_date = datetime.strptime(ocr_data['date_achat'], "%Y-%m-%d %H:%M:%S")
    mode_paiement = ocr_data.get('mode_paiement', None)

    execute_query("""
        INSERT INTO tickets (num_ticket, user_id, article_count, purchase_date, mode_paiement)
        VALUES (%s, NULL, %s, %s, %s)
        ON CONFLICT (num_ticket) DO NOTHING;
    """, (
        num_ticket,
        len(ocr_data['produits']),
        purchase_date,
        mode_paiement
    ))

    # Insert each product (article)
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

    print("✅ OCR Data inserted successfully!")

# For direct testing clearly:
if __name__ == "__main__":
    sample_ocr_output = {
      "ID_ticket": "22.03.2518:30:20001",
      "client": "NaN",
      "Marque": "LIDL",
      "numero_ticket": "001",
      "produits": [
        {"nom": "Lait 1/2écrème UHT", "quantité": "1", "prix_total": "1.00"},
        {"nom": "Cacahuetes grillées", "quantité": "1", "prix_total": "0.99"},
        {"nom": "Penne Rigate", "quantité": "2", "prix_total": "3.98"},
        {"nom": "Dattes ravier", "quantité": "1", "prix_total": "0.59"}
      ],
      "date_achat": "2025-03-22 18:30:20",
      "mode_paiement": "CARTE BANCAIRE"
    }

    insert_ticket_data(sample_ocr_output)
