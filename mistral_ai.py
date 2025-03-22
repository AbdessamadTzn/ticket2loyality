import requests
import json

# Configuration API Mistral
api_key = "oue93klhrJfR41W4vHGCtMP7g2v3WYQj"
url = "https://api.mistral.ai/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {api_key}",
}

def ia_function(text):
    """Analyse un ticket de caisse et renvoie un JSON structuré avec les informations essentielles."""
    
    # Construction du prompt
    prompt = f"""
    Tu es un assistant spécialisé en extraction d'informations de tickets de caisse.
    Analyse le texte ci-dessous et retourne les informations sous forme d'un JSON structuré.
    si une information manque tu mets NaN devant la clé
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

    # Requête à l'API de Mistral
    payload = {
        "model": "mistral-medium",
        "messages": [{"role": "user", "content": prompt.strip()}],
        "temperature": 0.2,
        "max_tokens": 300,
    }

    response = requests.post(url, headers=headers, json=payload)

    # Vérification et affichage de la réponse
    if response.status_code == 200:
        try:
            result = response.json()
            structured_data = result["choices"][0]["message"]["content"]
            parsed_json = json.loads(structured_data)
            return json.dumps(parsed_json, indent=4, ensure_ascii=False)
        except (json.JSONDecodeError, KeyError):
            print("Erreur : Impossible de parser la réponse de Mistral.")
    else:
        return f"Erreur API Mistral ({response.status_code}): {response.text}"

# Exemple d'utilisation
text = """"Vente",
    "04/01/202511:57:52",
    "Ticket N4-00001090",
    "ClientClient Caisse",
    "CaissierResp",
    "Qté",
    "Total",
    "PU",
    "Article",
    "1",
    "95,99(1)",
    "95,99",
    "Plaid en laine",
    "CARPATHIAN-",
    "marron",
    "TVA",
    "TTC",
    "Taux",
    "Base",
    "TVA",
    "79,99",
    "16,00",
    "95,99",
    "TVA20%1",
    "20,00",
    "16,00",
    "Nb Articles",
    "TVA",
    "Total HT79.99",
    "Nb Lignes",
    "1",
    "TTC(E)",
    "66'96",
    "Payépar",
    "95,99",
    "CB",
    "Merci de votre visite",
    "XX-Capital0,00€",
    "SIRETX-NAFX-TVAX",
    "ClientN1.V.B02-2024.5.3.0-37745ISDg-Imp.N1",
    "aisse4-Caiss.Resp.1"""

if __name__ =="__main__":   
     reponse =ia_function(text)
     print(reponse)
