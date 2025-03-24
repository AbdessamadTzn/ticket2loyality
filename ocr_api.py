from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import numpy as np
import cv2
import paddleocr
from mistral_ai import ia_function


app = FastAPI()

# Initialisation de l'OCR avec PaddleOCR
ocr = paddleocr.PaddleOCR(use_angle_cls=True, lang="fr")

@app.post("/ocr")
async def extract_text(file: UploadFile = File(...)):
    # Lire le fichier image en mémoire
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        return JSONResponse(content={"msg": "Erreur lors de la lecture de du ticket."}, status_code=400)

    # Exécuter OCR sur l'image
    result = ocr.ocr(img, cls=True)

    if not result or not result[0]:
        return JSONResponse(content={"msg": "Aucun ticket détecté."}, status_code=400)
    


    # Extraire le texte détecté
    text = [line[1][0] for line in result[0]]
    
    ticket_info = ia_function(text)

    return  ticket_info


# @app.post("/info")               
# async def