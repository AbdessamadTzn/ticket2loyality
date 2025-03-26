import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {MISTRAL_API_KEY}",
}

def ia_function(text):
    prompt = f"""
    Tu es un assistant spécialisé en extraction d'informations de tickets de caisse.
    Analyse le texte ci-dessous et retourne les informations sous forme d'un JSON structuré.
    si une information manque tu mets NaN devant la clé.

    Ticket de caisse :
    {text}

    Format attendu :
    {{
        "ID_ticket": "date_achat+numero de ticket",
        "client": "Nom du client ",
        "Marque": "marque du produit ",
        "numero de ticket": "numero de ticket",
        "produits": [
            {{"nom": "Nom du produit", "quantité": X, "prix_total": Y}}
        ],
        "date_achat": "YYYY-MM-DD HH:MM:SS",
        "mode_paiement": "Carte bancaire / Espèces / Autre"
    }}

    Réponds uniquement avec le JSON.
    """

    payload = {
        "model": "mistral-medium",
        "messages": [{"role": "user", "content": prompt.strip()}],
        "temperature": 0.2,
        "max_tokens": 300,
    }

    response = requests.post(MISTRAL_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            structured_data = response.json()["choices"][0]["message"]["content"]
            return json.loads(structured_data)
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Erreur lors du parsing JSON : {e}")
    else:
        raise ConnectionError(f"Erreur API Mistral ({response.status_code}): {response.text}")
