# imports for the MongoDB database connection
import os
# import for fast api lifespan
from contextlib import asynccontextmanager

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient


# define a lifespan method for fastapi
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start the database connection
    await startup_db_client(app)
    yield
    # Close the database connection
    await shutdown_db_client(app)

# method for start the MongoDb Connection
async def startup_db_client(app):
    app.mongodb_client = AsyncIOMotorClient(os.environ["MONGO_DB_URL"])
    app.mongodb = app.mongodb_client.get_database("artisan")
    print("MongoDB connected.")

# method to close the database connection
async def shutdown_db_client(app):
    app.mongodb_client.close()
    print("Database disconnected.")