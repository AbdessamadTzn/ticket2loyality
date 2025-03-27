from fastapi import FastAPI
from api.routers import auth, ocr, user_tickets

app = FastAPI()

app.include_router(auth.router)
app.include_router(ocr.router)
app.include_router(user_tickets.router)
