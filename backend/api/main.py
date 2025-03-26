from fastapi import FastAPI
from api.routers import auth, ocr, user_tickets

app = FastAPI()

# Include your auth endpoints
app.include_router(auth.router)

# Include your OCR endpoints
app.include_router(ocr.router)

# Include user ticket

app.include_router(user_tickets.router) 
