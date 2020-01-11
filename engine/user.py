""" 
Raul Pichardo
devpichardo@gmail.com

User class to give projects
"""

import validation


class User:
    userId: str #id of the user
    projects: list
    def __init__(self, name, email = None, number=None):
        self.name = name
        self.email = self.validate_email(email) if email else "None"
        self.number = self.validate_number(number) if number else "None"
        self.task = []
        self.userId = None
    #==========================================                        
    def add_task(self, task):
        """param: task -> can be str or list of str"""
        if type(task) == str:
            if task not in self.task:
                self.task.append(task)
        elif type(task) == list:
            for t in task:
                if task not in self.task:
                    self.task.append(t)            
    #==========================================     
    def task_info(self):
        if len(self.task) > 0:
            print("{} has to completed the following task: {}".format(self.name, ", ".join(self.task)))
        else:
            print("{} has any task to complete".format(self.name))
        
    #==========================================                      
    def show_task(self):
        if len(self.task) > 0:
            print(", ".join(self.task))
        else:
            print("No task to complete")
    #==========================================                    
    def validate_email(self, email):
        isValid = validation.validate_email(email)

        while not isValid:
            print("Invalid email, enter again")
            email = input("Email: ")
            isValid = validation.validate_email(email)
            
        return email
    #==========================================                    
    def validate_number(self, number):
        number = validation.validate_number(number)
        while not number:        
            print("Invalid number, enter again")
            print("The number can have the following formats:\n {},{}".format("###.###.####", "##########"))
            number = input("Number: ") 
            number = validation.validate_number(number)
        return number
    #==========================================                    
    # def create_project(self, projectName):
        