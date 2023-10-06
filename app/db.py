import asyncio
import motor.motor_asyncio

from decouple import Config


# Create a Config instance and specify the location of your .env file
config = Config(".env")

# Retrieve MongoDB-related environment variables

MONGO_URI = "mongodb://{}:{}@mongo:{}/".format(
    config.get("MONGO_USERNAME", default="username"),
    config.get("MONGO_PASSWORD", default="password"),
    config.get("MONGO_PORT", default="27017"),
)

MONGO_DATABASE = config.get("MONGO_DATABASE", default="url_shortener")

# Define a function to create and return an AsyncIOMotorClient
async def create_mongodb_connection():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
    return client[MONGO_DATABASE]

# Usage example
async def main():
    # Create the MongoDB client and get the database
    db = await create_mongodb_connection()
    # Use 'db' to interact with the database

# Run the event loop to execute asynchronous code
if __name__ == "__main__":
    asyncio.run(main())