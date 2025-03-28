from fastapi import APIRouter, HTTPException
from db.connection import execute_query
from decimal import Decimal

router = APIRouter()

@router.get("/user/{user_id}/brand-stats")
async def get_user_brand_stats(user_id: int):
    try:
        # Récupérer les statistiques par marque pour l'utilisateur
        query = """
        SELECT 
            m.nom_marque,
            COUNT(DISTINCT t.num_ticket) as total_tickets,
            SUM(a.prix * a.quantite) as total_spent,
            COUNT(a.id_article) as total_items
        FROM tickets t
        JOIN articles a ON t.num_ticket = a.num_ticket
        JOIN marques m ON a.nom_marque = m.nom_marque
        WHERE t.user_id = %s
        GROUP BY m.nom_marque
        """
        
        results = execute_query(query, (user_id,))
        
        brand_stats = []
        for row in results:
            # Convertir les Decimal en float pour la sérialisation JSON
            brand_stats.append({
                "nom_marque": row[0],
                "total_tickets": row[1],
                "total_spent": float(row[2]) if row[2] else 0,
                "total_items": row[3],
                # Calcul simple des points (1€ = 1 point)
                "points": int(float(row[2])) if row[2] else 0
            })
        
        return brand_stats
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
