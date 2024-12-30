from fastapi import FastAPI
from database import Base, engine
from routes import company

# Create tables
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Initialize FastAPI
app = FastAPI(on_startup=[create_tables])

# Include routers
app.include_router(company.router)
