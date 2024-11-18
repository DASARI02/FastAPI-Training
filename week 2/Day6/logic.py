class Logic:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        for i in self.tasks:
            if i.taskId == task.taskId:
                return False  
        self.tasks.append(task)
        return True

    def update_task(self, task):
        for i in range(len(self.tasks)):
            if self.tasks[i].taskId == task.taskId:
                self.tasks[i] = task 
                return True
        return False  

    def view_all_tasks(self):
        return self.tasks  

    def view_tasks_by_location(self, location):
        return [task for task in self.tasks if task.location == location]

    def view_tasks_by_status(self, status="running"):
        return [task for task in self.tasks if task.status == status]

    def delete_task(self, taskId):
        for i in range(len(self.tasks)):
            if self.tasks[i].taskId == taskId:
                del self.tasks[i]  
                return True
        return False 

