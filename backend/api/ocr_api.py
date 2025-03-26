from fastapi import Depends, UploadFile, File, HTTPException
from fastapi.security import OAuth2PasswordBearer
from auth.auth_handler import decode_token
from db.insert_ocr_data import insert_ticket_data_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@app.post("/ocr")
async def extract_text(
    file: UploadFile = File(...),
    token: str = Depends(oauth2_scheme)
):
    user = decode_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    user_id = user["user_id"]

    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        raise HTTPException(status_code=400, detail="Erreur lors de la lecture du ticket.")

    result = ocr.ocr(img, cls=True)

    if not result or not result[0]:
        raise HTTPException(status_code=400, detail="Aucun ticket détecté.")

    text = [line[1][0] for line in result[0]]
    ticket_info = ia_function("\n".join(text))

    # Insert clearly with user_id
    insert_ticket_data_user(ticket_info, user_id)

    return {"msg": "OCR and DB insertion successful", "data": ticket_info}
