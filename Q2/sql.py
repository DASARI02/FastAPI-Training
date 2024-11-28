from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from typing import List

# SQLAlchemy setup
DATABASE_URL = "sqlite:///./test.db"  # SQLite URL, change it based on your DB

Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the Employee table using SQLAlchemy
class EmployeeInDB(Base):
    __tablename__ = "employees"

    empno = Column(Integer, primary_key=True, index=True)
    empname = Column(String, index=True)
    deptid = Column(Integer)
    location = Column(String)

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# FastAPI setup
app = FastAPI()

# Pydantic model for Employee (request/response validation)
class Employee(BaseModel):
    empno: int
    empname: str
    deptid: int
    location: str

    class Config:
        orm_mode = True

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD operations using SQLAlchemy

def get_employee(db: Session, empno: int):
    return db.query(EmployeeInDB).filter(EmployeeInDB.empno == empno).first()

def get_all_employees(db: Session):
    return db.query(EmployeeInDB).all()

def update_employee(db: Session, empno: int, deptid: int, location: str):
    employee = db.query(EmployeeInDB).filter(EmployeeInDB.empno == empno).first()
    if employee:
        employee.deptid = deptid
        employee.location = location
        db.commit()
        db.refresh(employee)
        return True
    return False

def get_employees_by_location(db: Session, location: str):
    return db.query(EmployeeInDB).filter(EmployeeInDB.location == location).all()

# FastAPI routes

@app.get("/get")
def get_employee_route(empno: int, db: Session = Depends(get_db)):
    employee = get_employee(db, empno)
    if employee:
        return {"empno": employee.empno, "empname": employee.empname, "location": employee.location, "deptid": employee.deptid}
    raise HTTPException(status_code=404, detail=f"Employee with empno {empno} not found")

@app.put("/update")
def update_employee_route(empno: int, deptid: int, location: str, db: Session = Depends(get_db)):
    success = update_employee(db, empno, deptid, location)
    if success:
        return {"message": f"Employee with empno {empno} updated successfully"}
    raise HTTPException(status_code=404, detail=f"Failed to update employee with empno {empno}")

@app.get("/all")
def get_all_employees_route(db: Session = Depends(get_db)):
    employees = get_all_employees(db)
    if employees:
        return [{"empno": emp.empno, "empname": emp.empname, "location": emp.location, "deptid": emp.deptid} for emp in employees]
    return {"message": "No employees found"}

@app.get("/location")
def get_employees_by_location_route(location: str, db: Session = Depends(get_db)):
    employees = get_employees_by_location(db, location)
    if employees:
        return [{"empno": emp.empno, "empname": emp.empname, "location": emp.location, "deptid": emp.deptid} for emp in employees]
    return {"message": f"No employees found in location: {location}"}

@app.on_event("shutdown")
def shutdown_event():
    pass 
