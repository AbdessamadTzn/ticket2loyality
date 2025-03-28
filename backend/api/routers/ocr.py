from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import numpy as np
import cv2
import paddleocr
from ocr.mistral_ai import ia_function
from db.insert_ocr_data import insert_ticket_data_user

router = APIRouter()
ocr = paddleocr.PaddleOCR(use_angle_cls=True, lang="fr")

@router.post("/ocr")
async def extract_text(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        return JSONResponse(content={"msg": "Erreur lors de la lecture du ticket."}, status_code=400)

    result = ocr.ocr(img, cls=True)

    if not result or not result[0]:
        return JSONResponse(content={"msg": "Aucun ticket détecté."}, status_code=400)

    text = [line[1][0] for line in result[0]]
    ticket_info = ia_function("\n".join(text))

    # Insert directly into DB with user_id as None for now
    insert_ticket_data_user(ticket_info, user_id=None)

    return JSONResponse(content={"msg": "OCR and DB insertion successful", "data": ticket_info})