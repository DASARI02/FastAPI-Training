from db import EmployeeDatabase

class Logic:
    def __init__(self):
        self.db = EmployeeDatabase()

    def get_employee(self, empno):
        self.db.cursor.execute("SELECT * FROM employees WHERE empno = ?", (empno,))
        return self.db.cursor.fetchone()

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
        self.db.close_connection()
