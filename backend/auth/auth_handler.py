import bcrypt
import jwt
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET", "your_secret_here")
JWT_ALGORITHM = "HS256"

# Hash password
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

# Verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

# Create JWT token
def create_access_token(user_id: int, email: str, expires_delta=None):
    if expires_delta is None:
        expires_delta = timedelta(days=1)

    payload = {
        "user_id": user_id,
        "email": email,
        "exp": datetime.utcnow() + expires_delta
    }

    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

# Decode JWT token
def decode_token(token: str):
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded
    except jwt.PyJWTError:
        return None
