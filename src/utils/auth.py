import jwt
from datetime import datetime
from typing import Optional
from config.settings import JWT_SECRET_KEY, JWT_ACCESS_TOKEN_EXPIRES

def create_token(user_data: dict) -> str:
    """創建 JWT token"""
    return jwt.encode(user_data, JWT_SECRET_KEY, algorithm='HS256')

def verify_token(token: str) -> dict:
    """驗證 JWT token"""
    try:
        return jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
    except jwt.InvalidTokenError:
        return None 