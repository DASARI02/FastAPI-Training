class User:
    def __init__(self, name, age,email, Id):
        self.name = name 
        self.age = age 
        self.email = email 
        self.Id = id

    def __str__(self):
        return f"name is {self.name}, age is {self.age}, email is{self.email}, "
    
