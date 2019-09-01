""" 
Raul Pichardo
devpichardo@gmail.com

User class to give projects
"""

class User:
    def __init__(self,name, email = None, number=None):
        self.name = name
        self.email = email if email else "None"
        self.number = number if number else "None"
        self.task = []
    #==========================================                        
    def set_email(self, email):
        self.email  = email
    #==========================================                    
    def set_number(self, number):
        self.number = number
    #==========================================                        
    def add_task(self, task):
        if type(task) == str:
            if task not in self.task:
                self.task.append(task)
        elif type(task) == list:
            for _ in task:
                if task not in self.task:
                    self.task.append(_)            
    #==========================================                    
    def show_user_info(self):
        if len(self.task) == 0:
            self.task = "None"
        info = """
        Name: {}
        Email: {}
        Number: {}
        taks: {}
        """.format(self.name, self.email, self.number, ",".join(self.task))
        print(info)  
    #==========================================                    
    def show_task(self):
        if len(self.task) > 0:
            return ", ".join(self.task)
        return "None"