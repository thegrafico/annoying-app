""" 
Raul Pichardo
devpichardo@gmail.com

User class to give projects
"""

import validation


class User:
    user_id: int
    projects: list
    def __init__(self, name: str, email: str = None, number: str = None, user_id: int = None):
        self.name = name
        self.email = self.validate_email(email) if email else "None"
        self.number = self.validate_number(number) if number else "None"
        self.user_id = user_id
    # ==========================================
    def validate_email(self, email: str) -> str:
        isValid = validation.validate_email(email)

        while not isValid:
            print("Invalid email, enter again")
            email = input("Email: ")
            isValid = validation.validate_email(email)

        return email
    # ==========================================
    def validate_number(self, number):
        number = validation.validate_number(number)
        while not number:        
            print("Invalid number, enter again")
            print("The number can have the following formats:\n {},{}".format("###.###.####", "##########"))
            number = input("Number: ") 
            number = validation.validate_number(number)
        return number
    # ==========================================
    # def create_project(self, projectName):
        