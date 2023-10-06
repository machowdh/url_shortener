import strawberry
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient

class URLModel:

    def __init__(self, db: AsyncIOMotorClient):
        self.collection = db.urls
    
    async def create_url(self, data):
        return await self.collection.insert_one(data)
    
    async def find_url(self, query):
        return await self.collection.find_one(query)
    
    async def delete_url(self, query):
        return await self.collection.delete_one(query)
    