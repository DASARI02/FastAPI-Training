from presentation import Presentation
from logic import Logic
from task import Task

# lol = Logic()
# pre = Presentation()
# tas = Task()

# def fate():
#     print(f"Hello")


   
if __name__ == "__main__":
    T1 = Task(1,"task 1", 2, "T^2", "Chennai")
    a = Logic()
    b = a.add(T1)
    b = a.add(T1)
    print(b)
    tasks = a.view_all()
    for task in tasks:
        print(task)

