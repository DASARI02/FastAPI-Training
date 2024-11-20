from db import EmployeeDatabase
from emp import Employee


class Logic:
    def __init__(self):
        self.db = EmployeeDatabase()

    def add_employee(self, empno, empname, location, deptid):
 
        emp = Employee(empno, empname, location, deptid)
        self.db.add_employee(emp)
        return f"Employee {empname} with ID {empno} added successfully."

    def fetch_employee(self, empno):
  
        employee_data = self.db.get_employee(empno)
        if employee_data:
            return Employee(employee_data) 
        else:
            return f"Employee with ID {empno} not found."





            
