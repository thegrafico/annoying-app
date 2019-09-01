"""
Raul Pichardo
devpichardo@gmail.com
App to project managments the project of the CoRe Lab
"""
from user import User
from send_email import sendEmail
class Project:
    
    def __init__(self, name, description = ""):
        self.name = name
        self.users = []
        self.task = []
        self.user_in = ""
        self.project_desc = description
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

    def send_email_to_users(self, users_email= None):
        if len(self.users) > 0:
            for u in self.users:
                if u.email:
                    sendEmail(u.email, text_message=u.task_info())
        else:
            print("Users empty")
    #==========================================                    
    def run(self):
        self.options = {"1":self.add_user,
        "2":self.add_task,
        "3":self.set_task,
        "4":self.update_task,
        "5":self.remove_task,
        "6":self.show_user_task,
        "7":True,
        "8":self.remove_user,
        "9":self.send_email_to_users}
        print("\n================{}=================".format(self.name))
        print("1.Add user\n2.Add task\n3.Set task to user\n4.Update task\n5.Remove task\n6.Show project data\n7.Exit\n8.Remove user\n9.Send remainder email")
        print("=====================================\n")
        self.user_in = input("Select: ")
        if self.user_in != '7':
            self.options[self.user_in]()
    #==========================================     
#== 
if __name__ == "__main__":

    raul = User("Raul Pichardo", "raul022107@gmail.com", "7873776957")
    nicole = User("Nicole Santiago", "nicolesantiago0478@gmail.com", "9392321555")

    rtask = ["Create API", "Finish git", "Finish project"]
    ntask = ["Create gmail API", "Learn git"]

    project = Project("CoRe")
    project.add_user([raul, nicole])
    project.add_task([rtask, ntask])
    project.set_task(raul, rtask)
    project.set_task(nicole, ntask)

    while project.user_in != '7':
        project.run()
    
    print("Bye")