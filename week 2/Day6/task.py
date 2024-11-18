class Task:
    def __init__(self, taskId, location, status):
        self.taskId = taskId
        self.location = location
        self.status = status

    def __str__(self):
        return f"Task ID: {self.taskId}, Location: {self.location}, Status: {self.status}"