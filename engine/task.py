import datetime
from status import Status


class Task:
    taskId:int
    description:str
    priority:int
    status:Status
    creating_date:str
    end_date:str
    project_id:int
    task_ownerId:int
    def __init__(self):
        self.creating_date = datetime.datetime.today()
        self.status = Status.INCOMPLETE
    #--
    def change_status(self, status:Status):
        """Change the status of the task"""
        if self.status != status:
            if status == Status.COMPLETED:
                self.end_date = datetime.datetime.today()
            self.status = status
        #TODO: update the database