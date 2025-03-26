from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from auth.auth_handler import decode_token
from db.connection import execute_query

router = APIRouter()
security = HTTPBearer()

@router.get("/mytickets")
def get_user_tickets(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    user = decode_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    user_id = user["user_id"]

    tickets = execute_query("""
        SELECT num_ticket, article_count, purchase_date, mode_paiement, created_at
        FROM tickets
        WHERE user_id = %s
        ORDER BY created_at DESC;
    """, (user_id,))

    result = []
    for t in tickets:
        ticket_data = {
            "num_ticket": t[0],
            "article_count": t[1],
            "purchase_date": t[2].strftime("%Y-%m-%d %H:%M:%S"),
            "mode_paiement": t[3],
            "created_at": t[4].strftime("%Y-%m-%d %H:%M:%S")
        }
        result.append(ticket_data)

    return {"user_id": user_id, "tickets": result}
