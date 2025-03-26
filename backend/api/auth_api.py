from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from auth.auth_service import create_user, authenticate_user
from auth.auth_handler import create_access_token

app = FastAPI()

# Models
class SignupModel(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str

class LoginModel(BaseModel):
    email: str
    password: str

# User sign-up endpoint
@app.post("/signup")
def signup(user: SignupModel):
    try:
        create_user(user.email, user.password, user.first_name, user.last_name)
        return {"msg": "User created successfully!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# User login endpoint
@app.post("/login")
def login(credentials: LoginModel):
    user = authenticate_user(credentials.email, credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(user['user_id'], user['email'])
    return {"access_token": token, "token_type": "bearer"}
