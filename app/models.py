import strawberry
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient

@strawberry.type
class URL:
    id: str
    original_url : str
    short_url : str
    expiry_date : datetime


@strawberry.type
class Query:
    @strawberry.field
    async def get_url(self, url_key: str, db: AsyncIOMotorClient) -> URL:
        pass

@strawberry.type
class Mutation:
    
    @strawberry.mutation
    async def shorten_url(
        self,
        original_url: str,
        custom_alias: str = None,
        expiry_date: str = None,
        db: AsyncIOMotorClient,
    ) -> URL:
        pass

    @strawberry.mutation
    async def delete_url(
        self,
        url_key: str,
        db: AsyncIOMotorClient
    ) -> str:
        pass
