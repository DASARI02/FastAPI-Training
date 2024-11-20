from emp import Employee
import sqlite3

# connection = sqlite3.connect('my_Database.db')

# cursor = connection.cursor()
class EmployeeDatabase:
    def __init__(self,db_name = 'my_Datbase.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                empno INTEGER PRIMARY KEY,
                empname TEXT NOT NULL,
                location TEXT NOT NULL,
                deptid INTEGER NOT NULL
            )
        ''')
        # self.connection.commit()



    def add_employee(self,emp):
        insert_query = 'INSERT INTO users (empno, empname, location, deptid) VALUES (?,?,?,?)'
        self.cursor.execute(insert_query, (emp.empno, emp.empname, emp.location, emp.deptid))
    
        self.connection.commit()
    
    def get_employee(self, empno):
        self.cursor.execute("SELECT * FROM employees WHERE empno = ?",(empno))
        return self.cursor.fetchone()
    
    def update_employee(self, empno, deptid, location):
        #Update an employee's department and location.
        self.cursor.execute(
            "UPDATE employees SET deptid = ?, location = ? WHERE empno = ?",
            (deptid, location, empno)
        )
        self.connection.commit()
        return self.cursor.rowcount > 0

    def get_all_employees(self):
        #Retrieve all employees.
        self.cursor.execute("SELECT * FROM employees")
        return self.cursor.fetchall()
    
    def get_employee_location(self, location):
        #Retrieve employees filtered by location.
        self.cursor.execute("SELECT * FROM employees WHERE location = ?", (location,))
        return self.cursor.fetchall()

    def __del__(self):
        #Close the database connection when the object is deleted.
        self.connection.close()

    
if __name__ == "__main__":
    EmployeeDatabase()