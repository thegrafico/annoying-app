""" 
Raul Pichardo
devpichardo@gmail.com

User class to give projects
"""

import validation


class User:
    def __init__(self,name, email = None, number=None):
        self.name = name
        self.email = self.validate_email(email) if email else "None"
        self.number = self.validate_email(number) if number else "None"
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
    def task_info(self):
        return "{} has to completed the following task: {}".format(self.name, ", ".join(self.task))
    #==========================================     
    def show_user_info(self):
        if len(self.task) == 0:
            self.task = "None"
        info = """Name: {}, taks: {}
        """.format(self.name,  ",".join(self.task))
        return info 
    #==========================================                    
    def show_task(self):
        if len(self.task) > 0:
            return ", ".join(self.task)
        return "None"
    #==========================================                    
    def validate_email(self, email):
        email = validation.validate_email(email)
        while not email:
            print("Invalid email, enter again")
            email = input("Email: ")
            email = validation.validate_email(email)
        return email
    #==========================================                    
    def validate_number(self, number):
        print("The number can have the following formats:\n {},{}".format("###.###.####", "##########"))
        number = validation.validate_number(number)
        while not number:        
            print("Invalid number, enter again")
            number = input("Number: ") 
            number = validation.validate_number(number)
        return number