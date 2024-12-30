from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from models import Company

router = APIRouter(prefix="/companies", tags=["Companies"])

@router.get("/")
async def read_companies(db: AsyncSession = Depends(get_db)):
    result = await db.execute("SELECT * FROM companies")
    return result.fetchall()
