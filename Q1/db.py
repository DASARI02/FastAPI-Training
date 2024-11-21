from emp import Employee
import sqlite3

class EmployeeDatabase:
    def __init__(self,db_name = 'my_Datbase.db'):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)

        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                empno INTEGER PRIMARY KEY,
                empname TEXT NOT NULL,
                location TEXT NOT NULL,
                deptid INTEGER NOT NULL
            )
        ''')
        self.connection.commit()

if __name__ == "__main__":
    EmployeeDatabase()

#     def add_employee(self,emp):
#         insert_query = 'INSERT INTO users (empno, empname, location, deptid) VALUES (?,?,?,?)'
#         self.cursor.execute(insert_query, (emp.empno, emp.empname, emp.location, emp.deptid))

#         self.connection.commit()
    
#     def get_employee(self, empno):
#         self.cursor.execute("SELECT * FROM employees WHERE empno = ?",(empno))
#         return self.cursor.fetchone()
    
#     def update_employee(self, empno, deptid, location):
#         #Update an employee's department and location.
#         self.cursor.execute(
#             "UPDATE employees SET deptid = ?, location = ? WHERE empno = ?",
#             (deptid, location, empno)
#         )
#         self.connection.commit()
#         return self.cursor.rowcount > 0

#     def get_all_employees(self):
#         #Retrieve all employees.
#         self.cursor.execute("SELECT * FROM employees")
#         return self.cursor.fetchall()
    
#     def get_employee_location(self, location):
#         #Retrieve employees filtered by location.
#         self.cursor.execute("SELECT * FROM employees WHERE location = ?", (location,))
#         return self.cursor.fetchall()

#     def __del__(self):
#         #Close the database connection when the object is deleted.
#         self.connection.close()

    




    # def add_employee(self, empno, empname, location, deptid):
 
    #     emp = Employee(empno, empname, location, deptid)
    #     self.db.add_employee(emp)
    #     return f"Employee {empname} with ID {empno} added successfully."

    # def fetch_employee(self, empno):
  
    #     employee_data = self.db.get_employee(empno)
    #     if employee_data:
    #         return Employee(employee_data) 
    #     else:
    #         return f"Employee with ID {empno} not found."