"""
Raul Pichardo
devpichardo@gmail.com
App to project managments the project of the CoRe Lab
"""
from user import User
import whastapp as ws

from send_email import sendEmail
class Project:
    
    def __init__(self, userId, name, description = ""):
        self.owner = owner
        self.name = name
        self.users = []
        self.task = []
        self.user_in = ""
        self.project_desc = description
        self.run_once = True
    #==========================================
    def add_user(self, user=None):
        if not user:
            user = input("Enter user: ")
            user = User(user)
        if type(user) == list:
            for u in user:
                self.users.append(u)
        else:
            self.users.append(user)

        self.show_users()
    #==
    def remove_user(self, user_id=None):
        if len(self.users)>0:
            self.show_users()
            if not user_id:
                user_id = int(input("Enter user id: ")) - 1
            
            try:
                if self.users[user_id] in self.users:
                    print("User {} deleted".format(self.users[user_id].name))
                    del self.users[user_id]
                else:
                    print("Cannot find the user")
            except:
                print("User don't exits")
        else:
            print("Not users")
    #==========================================      
    def set_task(self, user = None, task = None):
        if len(self.users) > 0:
            self.show_users()
            self.show_task()
            if not user or not task:
                iuser = int(input("Enter user number: "))
                itask = int(input("Enter task number: "))
                if self.users[iuser-1] in self.users and self.task[itask-1] in self.task:
                    self.users[iuser-1].add_task(self.task[itask-1])
                    print("Added task to user")
                else:
                    print("user or task don't exits")
            else:
                print("User {}, task to add: {}".format(user.name, task))
                if user in self.users:
                    user.add_task(task)
                    print("Added user and task")
        else:
            print("Empty task or users")
    #=================CRUD SYSTEM=========================
    def add_task(self, task=None):

        if not task:
            task = input("Enter task: ")

        if type(task) == str:
            if task not in self.task:
                if len(task) > 4:
                    self.task.append(task)
                else:
                    print("Describe more the task")
        elif type(task) == list:
            for t in task:
                for n in t:
                    if n not in self.task and len(n) > 4:
                        self.task.append(n)
                    else:
                        print("Describe task more")

        self.show_task()
    #==
    def update_task(self):
        self.edit_task("update", "Update message: ")
    #==
    def remove_task(self):
        self.edit_task("remove")
    #==
    def edit_task(self, mode, msg=None):
        if len(self.task) > 0:
            self.show_task()
            itask = int(input("Please, enter the number of the task: "))-1
            if msg:
                ctask = input(msg)  
            try:
                if self.task[itask]:
                    for _user in self.users:
                        if self.task[itask] in _user.task:
                            ind = _user.task.index(self.task[itask])
                            if mode == "update":
                                _user.task[ind] = ctask
                            elif mode == "remove":
                                del _user.task[ind]
                    self.task[itask] = ctask
            except:
                print("Cannot find the task")
        else:
            print("Task empty")
    #==========================================        
    def show_users(self):
        if len(self.users) > 0:
            print("*************************")
            print("Users:")
            for n, user in enumerate(self.users, start=1):
                print("{}. {}".format(n, user.name))
            print("*************************")
        else:
            print("Not users")
    #==========================================        
    def show_task(self):
        if len(self.users) > 0:
            print("*************************")
            print("Task:")
            for n,task in enumerate(self.task, start=1):
                print("{}. {}".format(n, task))
            print("*************************")
        else:
            print("Not task")
    #==========================================
    def show_user_task(self):
        if len(self.users)> 0:
            print("User taks:")
            for _user in self.users:
                print("{} has the task: {}".format(_user.name, _user.show_task()) )
        else:
            print("There are not users")
    #==========================================
    def send_email_to_users(self, users_email= None):
        if len(self.users) > 0:
            for u in self.users:
                if u.email:
                    sendEmail(u.email, text_message=u.task_info())
        else:
            print("Users empty")
    
    #==========================================
    def add_number(self):
       self.add_user_date("number")

    def add_user_email(self, user=None):
        self.add_user_date("email")
    
    #==========================================
    def add_user_date(self, method, user=None):
        self.show_users()
        try:
            if not user:
                iuser = int (input("Select user: ")) - 1
                user = self.users[iuser]
            if user in self.users:
                data = input("Enter the {}: ".format(method))
                if method == "number":
                    user.number = data
                elif method == "email":
                    user.email = data
            else:
                print("Invalid user")
        except:
            print("Cannot find the user")
    #==========================================
    def send_ws_message(self):
        print(
            """
            1. Send message to all users
            2. Send message to one user
            """)
        ifunc = input("Select: ")
        self.show_users()

        if self.run_once:
            ws.init()
            self.run_once = False


        if ifunc == "2":
            iuser = int(input("Select user: ")) - 1
            try:
                user = self.users[iuser]
                ws.send_message(user.number, user.show_user_info())
            except:
                print("Invalid user")
        else:
            for u in self.users:
                ws.send_message(u.number, u.show_user_info())
    #==========================================
    def administrate_user(self):
        print(
            """
            1. Add user
            2. Remove user 
            3. Add user number
            4. Add user email
            5. Show users
            """)
        ifunc = input("Select: ")
        option = {
        "1":self.add_user,
        "2":self.remove_user,
        "3":self.add_number,
        "4":self.add_user_email,
        "5":self.show_users
        }
        try:
            option[ifunc]()
        except:
            print("Invalid option")
    #==========================================                    
    def administrate_task(self):
        print(
            """
            1. Add task
            2. Edit task
            3. Remove task
            4. Show Task
            """)
        ifunc = input("Select: ")
        option = {
        "1":self.add_task,
        "2":self.edit_task,
        "3":self.remove_task,
        "4":self.show_task
        }
        try:
            option[ifunc]()
        except:
            print("Invalid option")
    #==========================================                    
    def run(self):
        self.options = {
        "1":self.administrate_user,
        "2":self.administrate_task,
        "3":self.set_task,
        "4":self.show_user_task,
        "5":self.send_email_to_users,
        "6":self.send_ws_message,
        "7":True
        }
        print("\n================{}=================".format(self.name))
        print("""
        1. Administrate Users
        2. Administrate Task
        3. Set task to user
        4. Show project info
        5. Send remainder email
        6. Send whastapp message
        7. Exit
        """)
        print("=====================================\n")
        self.user_in = input("Select: ")
        if self.user_in != str(len(self.options)):
            try:
                self.options[self.user_in]()
            except:
                print("Option not available")
    #==========================================     
#== 
if __name__ == "__main__":

    # raul = User("Jose alfonzo", "jalfonzo7400@interbayamon.edu", "7874281308")
    # noah = User("Noah Almeda", "noahalmeda@gmail.com", "7874318538")

    rtask = ["Create API", "Finish git", "Finish project"]
    ntask = ["Create gmail API", "Learn git"]

    project = Project("Raul Pichardo", "CoRe")
    # project.add_user([raul, noah])
    project.add_task([rtask, ntask])
    # project.set_task(raul, rtask)
    # project.set_task(noah, ntask)

    while project.user_in != '7':
        project.run()
    
    print("Bye")