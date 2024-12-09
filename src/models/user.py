from datetime import datetime
from typing import Optional
from pymongo import MongoClient
from bson import ObjectId
import bcrypt

from config.settings import MONGO_URI, DATABASE_NAME, BCRYPT_ROUNDS

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

class User:
    collection = db.users

    @classmethod
    async def create(cls, username: str, password: str, role: str = 'user') -> dict:
        # 檢查用戶是否存在
        if await cls.find_by_username(username):
            raise ValueError('用戶名已存在')

        # 密碼加密
        salt = bcrypt.gensalt(BCRYPT_ROUNDS)
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        
        user = {
            'username': username,
            'password': hashed_password,
            'role': role,
            'created_at': datetime.utcnow()
        }
        
        result = cls.collection.insert_one(user)
        user['_id'] = result.inserted_id
        return user

    @classmethod
    async def find_by_username(cls, username: str) -> Optional[dict]:
        return cls.collection.find_one({'username': username})

    @classmethod
    async def verify_password(cls, username: str, password: str) -> bool:
        user = await cls.find_by_username(username)
        if not user:
            return False
        return bcrypt.checkpw(password.encode(), user['password']) 