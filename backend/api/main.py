from fastapi import FastAPI
from api.routers.ocr import router as ocr_router
from api.routers.user_tickets import router as user_tickets_router

app = FastAPI()

app.include_router(ocr_router)
app.include_router(user_tickets_router, prefix="/api")
