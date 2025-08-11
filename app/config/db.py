import motor.motor_asyncio
from beanie import init_beanie
from dotenv import load_dotenv
import os

from app.models.users import User


# Load .env file
load_dotenv()

class Database:
    client: motor.motor_asyncio.AsyncIOMotorClient = None

    @staticmethod
    async def connect():
        print("Connecting to MongoDB...")
        Database.client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("DATABASE_URL"))
        await init_beanie(
            database=Database.client[os.getenv("DATABASE_NAME")],
            document_models=[User] 
        )
        print("Connected to MongoDB.")

    @staticmethod
    async def disconnect():
        print("Disconnecting MongoDB...")
        Database.client.close()
        print("Disconnected from MongoDB.")
