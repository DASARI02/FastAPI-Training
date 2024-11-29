from fastapi import FastAPI, HTTPException, status, Depends, File, UploadFile
from logic import Logic
from db import Employer, Login, get_db
from datetime import date 
from pydantic import BaseModel
from sqlalchemy.orm import Session
import csv 

app = FastAPI()
main = Logic()

class Employee(BaseModel):
    emp_id : int
    first_name : str
    last_name : str
    date_of_birth:date
    date_of_joining:date
    grade:str
 
class Login(BaseModel):
    userid:int 
    username : str  
    password:str

@app.post("/import_employers", status_code=status.HTTP_201_CREATED)
async def import_employers(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only CSV files are allowed.",
        )

    try:
        content = await file.read()  # Read the file
        csv_data = content.decode("utf-8").splitlines()  # Decode and split into lines
        reader = csv.DictReader(csv_data)

        new_employers = []
        for row in reader:
            # Parse CSV row into Employer fields
            new_employer = Employer(
                employerid=int(row["employerid"]),
                first_name=row["first_name"],
                last_name=row["last_name"],
                date_of_birth=date.fromisoformat(row["date_of_birth"]),  # Use date parsing
                date_of_joining=date.fromisoformat(row["date_of_joining"]),  # Use date parsing
                grade=row["grade"],
            )
            new_employers.append(new_employer)

        # Bulk insert all rows
        db.bulk_save_objects(new_employers)
        db.commit()
        return {"message": f"{len(new_employers)} employees imported successfully."}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while importing data: {str(e)}",
        )
@app.post("/login", status_code=status.HTTP_200_OK)
async def login(login_data: Login):
    employee = main.login(login_data.userid,login_data.username, login_data.password)
    if employee:
        return {"message": "Login successful"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user ID or password"
        )


@app.get("/view_employee/{emp_id}", status_code=status.HTTP_200_OK)
async def view_employee(emp_id:int):
    employee = main.view_by_id(emp_id)
    if employee:
        return employee 
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
@app.put("/updated/{emp_id}", status_code=status.HTTP_200_OK)
async def update(emp_id:int, updated_employee: Employee):
    update = main.update(emp_id, updated_employee)
    if update:
        return {"message": "Employee is Updated"}
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
    

@app.get("/search_by_first_name/{first_name}", status_code= status.HTTP_200_OK)
async def search_by_first_name(first_name: str):
    employee = main.first_name(first_name)
    if employee:
        return employee
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    

@app.get("/search_by_last_name/{last_name}",status_code= status.HTTP_200_OK)
async def search_last_name(last_name : str):
    employee = main.last_name(last_name)
    if employee:
        return employee 
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
@app.get("/search_by_dob/{date_of_birth}", status_code=status.HTTP_200_OK)
async def search_dob(date_of_birth: date):
    try:
        employee = main.dob(date_of_birth)  # Pass the date directly
        if employee:
            return employee
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No employees found with this date of birth")

    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid date format. Use YYYY-MM-DD.",
        )

    
@app.get("/search_by_doj/{date_of_joining}", status_code= status.HTTP_200_OK)
async def search_doj(date_of_joining : date):
    try:
        employee = main.doj(date_of_joining)
        if employee:
            return employee 
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    

    
@app.get("/search_by_grade/{grade}", status_code=status.HTTP_200_OK)
async def search_grade(grade: str):
    employees = main.grade(grade)
    if employees:
        return employees
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No employees found with this grade"
        )
    
 