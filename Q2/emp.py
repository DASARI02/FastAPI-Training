class Employee:
    def __init__(self, empno, empname, location, deptid):
        self.empno = empno
        self.empname = empname
        self.location = location
        self.deptid = deptid

    def __str__(self):
        return f"EmpNo: {self.empno}, Name: {self.empname}, Location: {self.location}, DeptID: {self.deptid}"
