from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy.ext.asyncio import AsyncSession
from database import engine, Base, get_db  # Import from database.py
from models import Company, CommunicationMethod  # Import your models
from routers import admin_router, user_router, reports_router

models.Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI()

# Initialize the database
@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        # Ensure all tables are created
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def shutdown_event():
    await engine.dispose()

# Include routers
app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(reports_router, prefix="/reports", tags=["Reports and Analytics"])

# Admin - Company Management
@app.post("/admin/companies/", response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    db_company = models.Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

@app.get("/admin/companies/", response_model=list[schemas.Company])
def get_companies(db: Session = Depends(get_db)):
    companies = db.query(models.Company).all()
    return companies

@app.put("/admin/companies/{company_id}", response_model=schemas.Company)
def update_company(company_id: int, company: schemas.CompanyUpdate, db: Session = Depends(get_db)):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if not db_company:
        raise HTTPException(status_code=404, detail="Company not found")
    for key, value in company.dict(exclude_unset=True).items():
        setattr(db_company, key, value)
    db.commit()
    db.refresh(db_company)
    return db_company

@app.delete("/admin/companies/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db)):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if not db_company:
        raise HTTPException(status_code=404, detail="Company not found")
    db.delete(db_company)
    db.commit()
    return {"detail": "Company deleted successfully"}

# Admin - Communication Methods
@app.post("/admin/communication-methods/", response_model=schemas.CommunicationMethod)
def create_communication_method(method: schemas.CommunicationMethodCreate, db: Session = Depends(get_db)):
    db_method = models.CommunicationMethod(**method.dict())
    db.add(db_method)
    db.commit()
    db.refresh(db_method)
    return db_method

@app.get("/admin/communication-methods/", response_model=list[schemas.CommunicationMethod])
def get_communication_methods(db: Session = Depends(get_db)):
    methods = db.query(models.CommunicationMethod).all()
    return methods

@app.put("/admin/communication-methods/{method_id}", response_model=schemas.CommunicationMethod)
def update_communication_method(method_id: int, method: schemas.CommunicationMethodUpdate, db: Session = Depends(get_db)):
    db_method = db.query(models.CommunicationMethod).filter(models.CommunicationMethod.id == method_id).first()
    if not db_method:
        raise HTTPException(status_code=404, detail="Method not found")
    for key, value in method.dict(exclude_unset=True).items():
        setattr(db_method, key, value)
    db.commit()
    db.refresh(db_method)
    return db_method

@app.delete("/admin/communication-methods/{method_id}")
def delete_communication_method(method_id: int, db: Session = Depends(get_db)):
    db_method = db.query(models.CommunicationMethod).filter(models.CommunicationMethod.id == method_id).first()
    if not db_method:
        raise HTTPException(status_code=404, detail="Method not found")
    db.delete(db_method)
    db.commit()
    return {"detail": "Method deleted successfully"}

# Admin - Dashboard Overview
@app.get("/admin/overview/")
def get_overview(db: Session = Depends(get_db)):
    total_companies = db.query(models.Company).count()
    total_methods = db.query(models.CommunicationMethod).count()
    return {
        "total_companies": total_companies,
        "total_methods": total_methods
    }
