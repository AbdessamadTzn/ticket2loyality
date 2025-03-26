from db.connection import execute_query
from auth.auth_handler import hash_password, verify_password

# Sign up logic
def create_user(email: str, password: str, first_name: str, last_name: str):
    hashed_pw = hash_password(password)
    execute_query("""
        INSERT INTO users (email, password, first_name, last_name)
        VALUES (%s, %s, %s, %s);
    """, (email, hashed_pw, first_name, last_name))

# Verify user credentials clearly
def authenticate_user(email: str, password: str):
    user = execute_query("SELECT id, password FROM users WHERE email = %s", (email,))
    
    if not user:
        return None

    user_id, hashed_password = user[0]
    if verify_password(password, hashed_password):
        return {"user_id": user_id, "email": email}
    return None
