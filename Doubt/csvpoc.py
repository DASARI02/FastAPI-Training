import csv
class Emp:
    def __init__(self, empno, deptid):
        self.empno = empno
        self.deptid = deptid
#converting emp object into a list of individual values because csv writer function needs list of values.
    def to_csv_row(self):
        return [self.empno, self.deptid]

    # Class method to create a Product from a CSV row (to read from CSV)
    @classmethod
    def from_csv_row(cls, row): #while reading csv read function returns us a list which contains emp number and dept id as strings.
        x,y = row #the row is a list where first element is emp number and the second element is dept id. both are strings
        bnoof = Emp(int(x),int(y))
        return bnoof 
    
    def __str__(self):
        return f"{self.empno},{self.deptid}"

def write_to_csv(emp, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file) #  we want the write function with respect to csv
        writer.writerow(emp.to_csv_row())  #writes the csv content you gave into the file
        print("written successfully")

def read_from_csv(filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file) #  we want the write function with respect to csv
        for row in reader:
            emp_object = Emp.from_csv_row(row)
        return emp_object

# emp_object_file = read_from_csv("poc.csv")
# print(emp_object_file)
emp_object = Emp(1,100)
write_to_csv(emp_object,"poc.csv")


