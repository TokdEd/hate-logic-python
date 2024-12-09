from datetime import datetime
from typing import List, Optional
from pymongo import MongoClient
from bson import ObjectId

from config.settings import MONGO_URI, DATABASE_NAME
#mongodb here
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

class Submission:
    collection = db.submissions

    @classmethod
    async def create(cls, user_id: str, content: str) -> dict:
        submission = {
            'user_id': user_id,
            'content': content,
            'status': 'pending',
            'created_at': datetime.utcnow(),
            'reviewed_by': None,
            'reviewed_at': None
        }
        
        result = cls.collection.insert_one(submission)
        submission['_id'] = result.inserted_id
        return submission

    @classmethod
    async def update_status(cls, submission_id: str, status: str, admin_id: str) -> Optional[dict]:
        update_data = {
            'status': status,
            'reviewed_by': admin_id,
            'reviewed_at': datetime.utcnow()
        }
        
        result = cls.collection.find_one_and_update(
            {'_id': ObjectId(submission_id)},
            {'$set': update_data},
            return_document=True
        )
        return result

    @classmethod
    async def get_submissions(cls, status: Optional[str] = None) -> List[dict]:
        query = {}
        if status:
            query['status'] = status
        return list(cls.collection.find(query)) 