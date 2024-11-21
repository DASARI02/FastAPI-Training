# from logic import Logic

# if __name__ == "__main__":
#     a = Logic()
#     print(a.get_employee(1))


 
from logic import Logic

if __name__ == "__main__":
    a = Logic()


    emp = a.get_employee(1)
    print(emp)


    updated = a.update_employee(1, 103, "HYD")
    print(updated)


    all_employees = a.get_all_employees()
    print("\nAll Employees:")
    for emp in all_employees:
        print(emp)


    location = "Delhi"
    employees_in_location = a.get_employees_by_location(location)
    print(f"\nEmployees in {location}:")
    for emp in employees_in_location:
        print(emp)
