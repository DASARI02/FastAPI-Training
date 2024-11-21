# from db import EmployeeDatabase
# from emp import Employee




# class Logic:
#     def __init__(self):
#         self.db = EmployeeDatabase()

    
#     def get_employee(self, empno):
#         self.db.cursor.execute("SELECT * FROM employees WHERE empno = ?", (empno,))
#         return self.db.cursor.fetchone()
       
    
#     def update_employee(self, new_deptid, new_location):

#         self.db.cursor.execute(
#             "UPDATE employees SET deptid = ?, location = ?",
#             (new_deptid, new_location)
#         )

#         # self.db.connection.commit()
#         # return self.db.cursor.rowcount > 0

#     def get_all_employees(self):
#         #Retrieve all employees.
#         self.cursor.execute("SELECT * FROM employees")
#         return self.cursor.fetchall()
    
#     def get_employee_location(self, location):
#         #Retrieve employees filtered by location.
#         self.cursor.execute("SELECT * FROM employees WHERE location = ?", (location,))
#         return self.cursor.fetchall()



    
# if __name__ == "__main__":
#     EmployeeDatabase()
    

from db import EmployeeDatabase
from emp import Employee


class Logic:
    def __init__(self):
        self.db = EmployeeDatabase()

    def get_employee(self, empno):
        print(f"Running query for empno: {empno}")
        self.db.cursor.execute("SELECT * FROM employees WHERE empno = ?", (empno,))
        result = self.db.cursor.fetchone()
        print(f"Query result: {result}")
        return result


    def update_employee(self, empno, deptid, location):

        self.db.cursor.execute(
            "UPDATE employees SET deptid = ?, location = ? WHERE empno = ?",
            (deptid, location, empno)
        )
        self.db.connection.commit()
        return self.db.cursor.rowcount > 0

    def get_all_employees(self):

        self.db.cursor.execute("SELECT * FROM employees")
        return self.db.cursor.fetchall()

    def get_employees_by_location(self, location):

        self.db.cursor.execute("SELECT * FROM employees WHERE location = ?", (location,))
        return self.db.cursor.fetchall()

    def clean_up(self):
        self.db.connection.close()
        self.db.cursor.close()

            
