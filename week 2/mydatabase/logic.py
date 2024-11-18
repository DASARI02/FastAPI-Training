import db 
from user import User 

class Logic:
    def __init__(self):
        self.db = db 

    def insert_query(self,name, age, email):
        user_object = User(name,age,email)
        return self.db.insert_query(user_object)

    def get_query(self):
        return self.db.recieve_data()
    
    def close_up(self):
        return self.db.close()
    

