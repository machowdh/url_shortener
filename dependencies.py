from motor.motor_asyncio import AsyncIOMotorClient

async def get_database() -> AsyncIOMotorClient:
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    try:
        yield client
    finally:
        client.close()