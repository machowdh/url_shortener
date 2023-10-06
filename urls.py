import strawberry
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from app.schema import URL
from .dependencies import get_database


@strawberry.mutation
async def shorten_url(
    self,
    original_url: str,
    custom_alias: str = None,
    expiry_date: str = None,
    db: AsyncIOMotorClient = Depends(get_database)
) -> URL:
    urls_collection = db["urls"]

    pass

@strawberry.mutation
async def update_url(
    self,
    url_key: str,
    new_long_url: str,
    db: AsyncIOMotorClient = Depends(get_database)  
) -> URL:
    pass

@strawberry.mutation
async def delete_url(
    self,
    url_key: str,
    db: AsyncIOMotorClient = Depends(get_database)  
) -> str:
    pass

@strawberry.field
async def get_url(
    self,
    url_key: str,
    db: AsyncIOMotorClient = Depends(get_database)  
) -> URL:
    pass
