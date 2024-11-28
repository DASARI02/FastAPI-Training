import db as DB
from db import Employer, Login
from db import Session, engine, get_db
from datetime import datetime 

DB.Base.metadata.create_all(bind=engine)


class Logic:
    def login(self, userid : int, username: str, password: str):
        employee = Session.query(Login).filter(Login.userid == userid).first()
        if employee and (employee.username == username) and (employee.password == password):
            print('Success')
            return employee 
        else:
            print("Invalid")
            return None
        
    def view_by_id(self, employerid : int ):
        return Session.query(Employer).filter(Employer.employerid == employerid).first()
    

    def update(self, employerid: int , updated_emp : Employer):
        employee = Session.query(Employer).filter(Employer.employerid == employerid).first()
        if employee:
            employee.first_name = updated_emp.first_name
            employee.last_name = updated_emp.last_name
            employee.date_of_birth = updated_emp.date_of_birth
            employee.date_of_joining = updated_emp.date_of_joining
            employee.grade = updated_emp.grade
            Session.commit()
            Session.refresh(employee)
            print("Updated successfully!")
            return employee
        else:
            print("Employer not found.")
            return None

    def first_name(self, first_name: str):
        return Session.query(Employer).filter(Employer.first_name == first_name).first()
    
    def last_name(self, last_name: str):
        return Session.query(Employer).filter(Employer.last_name == last_name).first()
    
    def dob(self,dob : str):
        return Session.query(Employer).filter(Employer.date_of_birth == dob).all()
    
    def doj(self, doj: datetime):
        return Session.query(Employer).filter(Employer.date_of_joining == doj).all()
    
    def grade(self, grade : str):
        return Session.query(Employer).filter(Employer.grade == grade).all()
    


    # # Search for employers by their first name
    # def search_by_first_name(self, first_name: str):
    #     return db_session.query(Employer).filter(Employer.first_name == first_name).all()

    # # Search for employers by their last name
    # def search_by_last_name(self, last_name: str):
    #     return db_session.query(Employer).filter(Employer.last_name == last_name).all()

    # # Search for employers by their date of birth
    # def search_by_dob(self, dob: datetime):
    #     return db_session.query(Employer).filter(Employer.date_of_birth == dob).all()

    # # Search for employers by their date of joining
    # def search_by_doj(self, doj: datetime):
    #     return db_session.query(Employer).filter(Employer.date_of_joining == doj).all()

    # # Search for employers by their grade
    # def search_by_grade(self, grade: str):
    #     return db_session.query(Employer).filter(Employer.grade == grade).all()
