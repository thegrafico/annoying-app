"""
Raul Pichardo
devpichardo@gmail.com

App to project managments the project of the CoRe Lab
"""
from user import User

class Project:
    
    def __init__(self, name):
        self.name = name
        self.users = []
        self.task = []
        self.user_in = ""
    #==========================================
    def add_user(self, user=None):
        if not user:
            user = input("Enter user: ")
            user = User(user)
        self.users.append(user)

        self.show_users()

    #==========================================    
    def add_task(self, task=None):
        if not task:
            task = input("Enter task: ")

        self.task.append(task)

    #==========================================    
    def set_task(self, user = None, task = None):

        self.show_users()
        self.show_task()
        iuser = int(input("Enter user number: "))
        itask = int(input("Enter task number: "))
        if self.users[iuser-1] in self.users and self.task[itask-1] in self.task:
            self.users[iuser-1].add_task(self.task[itask-1])
        else:
            print("user or task don't exits")
    #==========================================        
    def update_task(self, task=None):
        self.show_task()
        itask = int(input("Please, enter the number of the task: "))-1
        ctast = input("Update message: ")
        
        if self.task[itask]:

            for _user in self.users:
                if self.task[itask] in _user.task:
                    ind = _user.task.index(self.task[itask])
                    _user.task[ind] = ctast
            self.task[itask] = ctast
    #==========================================        
    def show_users(self):
        print("Users:")
        for n, user in enumerate(self.users, start=1):
            print("{}. {}".format(n, user.name))
    #==========================================        
    def show_task(self):
        print("Taks:")
        for n,task in enumerate(self.task, start=1):
            print("{}. {}".format(n, task))        
    #==========================================
    def show_user_task(self):
        print("User taks:")

        if len(self.users)> 0:

            for _user in self.users:
                print("{} has the task: {}".format(_user.name, _user.show_task()) )
        else:
            print("There are not users")
    #==========================================                    
    def run(self):
        self.options = {"1":self.add_user,"2":self.add_task,"3":self.set_task,"4":self.update_task,"5":self.show_user_task,"6:":True}
        print("\n================{}=================".format(self.name))
        print("1.Add user\n2.Add task\n3.Set task to user\n4.Update task\n5.Show project data\n6.Exit")
        print("=====================================\n")
        self.user_in = input("Select: ")
        if self.user_in != '6':
            self.options[self.user_in]()
#== 
if __name__ == "__main__":
    project = Project("CoRe")

    while project.user_in != '6':
        project.run()
    
    print("Bye")