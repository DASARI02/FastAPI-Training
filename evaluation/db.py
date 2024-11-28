from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.orm import sessionmaker #interacting with database
Base = declarative_base() #for table definations

DATABASE_URL = "sqlite:///employee_ev.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind=engine)
class Login(Base):
    __tablename__ = 'Logic'
    userid = Column( Integer, primary_key= True, autoincrement = True)
    username = Column(String,unique = True, nullable= False)  
    password = Column( String, nullable = False )

class Employer(Base):
    __tablename__ = 'Employer'
    employerid = Column(Integer, primary_key = True, autoincrement= True)
    first_name = Column(String, nullable= False )
    last_name = Column(String, nullable= False)
    date_of_birth = Column(Date, nullable= False)
    date_of_joining = Column(Date, nullable= False)
    grade = Column(String, nullable= False)
# engine = create_engine('sqlite:///employee.db', echo = True) #Prints all Sql statements
Base.metadata.create_all(engine)

Session = SessionLocal()
def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()