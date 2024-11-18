class Task:

    def __init__(self, taskId, taskname, priority,status, location):
        self.taskId = taskId
        self.taskname = taskname
        self.priority = priority 
        self.status = status
        self.location = location 

    def __str__(self):
        return(f"TaskID {self.taskId}, taskname{self.taskname}, priority{self.priority},status{self.status},location{self.location}")



    # def f3(self):
    #     print('f3 pass')
    # pass