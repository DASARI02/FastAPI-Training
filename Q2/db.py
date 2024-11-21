import sqlite3

class EmployeeDatabase:
    def __init__(self, db_name='my_Database.db'):

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

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

if __name__ == "__main__":
    db = EmployeeDatabase()
    