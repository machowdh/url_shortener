import typing
import strawberry
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient
from .models import URLModel
from .shortener import generate_unique_short_url
from .db import create_mongodb_connection
from fastapi import Depends


@strawberry.type
class URL:
    long_url: str
    short_url: str
    expiry_date: datetime
    custom_alias: str = None


@strawberry.type
class Query:
    @strawberry.field
    async def get_long_url(self, short_url: str, db: AsyncIOMotorClient = Depends(create_mongodb_connection)) -> URL:
        try:
            query = {"short_url": short_url}
            result = await URLModel.find_url(query, db)
            return result
        except Exception as e:
            raise Exception(f"Error retrieving URL: {str(e)}")

    @strawberry.field
    async def get_short_url(self, long_url: str, db: AsyncIOMotorClient = Depends(create_mongodb_connection)) -> URL:
        try:
            query = {"long_url": long_url}
            result = await URLModel.find_url(query, db)
            return result
        except Exception as e:
            raise Exception(f"Error retrieving URL: {str(e)}")

@strawberry.type
class Mutation:
    
    @strawberry.mutation
    async def shorten_url(
        self,
        long_url: str,
        db: AsyncIOMotorClient= Depends(create_mongodb_connection),
        custom_alias: str = None,
        expiry_date: str = None,
    ) -> URL:
        shortened_url = await generate_unique_short_url()
        url = URL(long_url=long_url, short_url=await shortened_url,expiry_date=expiry_date,custom_alias=custom_alias)
        URLModel.create_url(url, db)
        return url

    @strawberry.mutation
    async def delete_url(
        self,
        url_key: str,
        db: AsyncIOMotorClient = Depends(create_mongodb_connection)
    ) -> str:
        try:
            query = {'short_url': url_key}
            deleted_count = await URLModel.delete_url(query, db)

            if deleted_count == 1:
                return "URL Deleted Successfully"
            else:
                return "URL Not Found"
        except Exception as e:
            raise Exception(f"Error deleting URL: {str(e)}")