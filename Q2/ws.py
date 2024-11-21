from fastapi import FastAPI
from logic import Logic
from pydantic import BaseModel
app = FastAPI()
logic = Logic()


class Employee(BaseModel):
    empno : int 
    empname : str 
    deptid : int 
    location : str 

@app.get("/get")
def get_employee(empno : Employee):
    employee = logic.get_employee(empno)
    if employee:
        return {
            "empno": employee[0],
            "empname": employee[1],
            "location": employee[2],
            "deptid": employee[3]
        }
    return {"message": f"Employee with empno {empno} not found"}

@app.put("/update")
def update_employee(empno: int, deptid: int, location: str):
    success = logic.update_employee(empno, deptid, location)
    if success:
        return {"message": f"Employee with empno {empno} updated successfully"}
    return {"message": f"Failed to update employee with empno {empno}"}

@app.get("/all")
def get_all_employees():
    employees = logic.get_all_employees()
    if employees:
        return [{"empno": emp[0], "empname": emp[1], "location": emp[2], "deptid": emp[3]} for emp in employees]
    return {"message": "No employees found"}

@app.get("/location")
def get_employees_by_location(location: str):
    employees = logic.get_employees_by_location(location)
    if employees:
        return [{"empno": emp[0], "empname": emp[1], "location": emp[2], "deptid": emp[3]} for emp in employees]
    return {"message": f"No employees found in location: {location}"}

@app.on_event("shutdown")
def shutdown_event():
    logic.clean_up()
