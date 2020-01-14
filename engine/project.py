"""
Raul Pichardo
devpichardo@gmail.com
App to project managments the project of the CoRe Lab
"""

# TODO: improve task for users

import whastapp as ws
from send_email import sendEmail
from task import Task
from user import User


class Project:
    tasks: [Task]
    owner: User
    workers: [User]
    project_id: int

    def __init__(self, name: str, user_id: int, project_id: int, description=""):
        self.creator_id = user_id
        self.project_id = project_id
        self.name = name
        self.project_desc = description
        self.workers = []
        self.tasks = []

    # ==========================================
    def add_user(self, user: User):
        """Add just one user"""

        if len(self.workers) > 0:
            users_id = [temp.user_id for temp in self.workers]
        else:
            users_id = []

        if user.user_id not in users_id:
            self.workers.append(user)
            users_id.append(user.user_id)
        else:
            self.workers.append(user)

        self.show_users()
    # ==

    def remove_user_by_id(self, user_id: int):
        """
        Remove user by id
        param: user_id -> id of the user to remove
        """
        if not len(self.workers):
            return

        # get all user ids
        all_user_ids = [u.user_id for u in self.workers]

        # verify if user exits
        if user_id not in all_user_ids:
            return

        for elem, i in enumerate(self.workers):
            if user_id == elem.user_id:
                del self.workers[i]
                return
    # ==

    # ==========================================
    def set_task(self, user_id: int, task_id: int) -> bool:
        """
        Assign task to users. Task have to be created
        param: userid ->Id of the user to assign task
        task: task object to assign to user
        return: True if a least one task was added
        """
        # all unique id of user in the project
        allWorkersId = [u.user_id for u in self.workers]
        all_task_id = [t.task_id for t in self.tasks]

        # Verify user_id and verify if this id is for one of the workers in the project
        # TODO: verify is task exits
        if user_id < 1 or user_id not in allWorkersId or task_id not in all_task_id:
            print("User id not belong to anyone in the project")
            return False

        for i in range(len(self.tasks)):
            if task_id == self.tasks[i].task_id:
                self.tasks[i].assign_user(user_id)
                # print(self.tasks[i].users)
                # print("THE TASK WITH THE ID: {}, WAS ASSIGNED TO THE USER WITH THE ID: {}".format(
                #     self.tasks[i].task_id, user_id))
                return True

        return False

    # =================CRUD SYSTEM=========================
    def add_task(self, task: [Task]) -> bool:
        """Adding task"""

        wasAdded = False

        # is task is empty
        if not len(task):
            return wasAdded

        if not len(self.tasks):
            allTaskId = []
        else:
            allTaskId = [t.task_id for t in self.tasks]

        for t in task:
            if t.task_id not in allTaskId:
                t.project_id = self.project_id
                self.tasks.append(t)
                allTaskId.append(t.task_id)
                wasAdded = True
        return wasAdded
    # ==
    def remove_task(self, task_id: int) -> bool:
        """
        Remove a task for a project
        param: task_id -> task id to remove
        """
        all_task_id = [t.task_id for t in self.tasks]

        if task_id not in all_task_id:
            return False

        for i in range(len(self.tasks)):
            if self.tasks[i].task_id == task_id:
                del self.tasks[i]
                return True
        return False

    # ==
    def edit_task(self, task_id: int, new_values: {}):
        """
        Edit a task
        task_id: id of the task to edit
        new_values: dictionary of values {"owner":int, "status":Status, "description":str, "priority":int}
        not all values are needed.
        """

        if not len(new_values) or task_id < 1:
            return

        all_task_id = [t.task_id for t in self.tasks]

        if task_id not in all_task_id:
            return

        # find task to edit
        task_to_edit: Task = list(filter(lambda t: task_id == t.task_id, self.tasks))[0]

        # Edit the task
        task_to_edit.edit(new_values)

    # ==========================================
    def show_users(self):
        if len(self.workers) > 0:
            print("*************************")
            print("Users:")
            for n, user in enumerate(self.workers, start=1):
                print("{}. {}".format(n, user.name))
            print("*************************")
        else:
            print("Not users")

    # ==========================================
    def task_info(self):
        """Show all task in the project"""

        if not len(self.tasks):  # task is empty??
            print("Not tasks")
            return
        print("*************************")
        print("Task:")
        for task in self.tasks:
            msg = "ID: {}, creator_id: {}, Description: {}, "
            print(msg.format(task.task_id, task.creator_id, task.description), end="")
            print("Assigned task: ", task.users)
        print("*************************")

    # ==
    def get_task_by_user(self, user_id: int) -> [Task]:
        """Return all task assigned to a user using the user_id"""

        # Verify is task is empty
        if not len(self.tasks):
            return []

        # filter by userid
        return list(filter(lambda temp: (user_id in temp.assigned_ids), self.tasks))

    # ==
    def remove_user_from_task(self, user_id: int, task_id: int):
        """ Remove a task by user id """

        if not len(self.workers) or not len(self.tasks):
            return

        # all tasks id and user id
        all_task_id = [t.task_id for t in self.tasks]
        all_user_id = [u.user_id for u in self.workers]

        # verify is exist
        if task_id not in all_task_id or user_id not in all_user_id:
            return

        # Get the list of task task to remove the user
        list_task_to_remove = list(filter(lambda t: t.task_id == task_id, self.tasks))

        # get the task to remove
        task_to_remove: Task = list_task_to_remove[0] if len(list_task_to_remove) > 0 else None

        # if task is None
        if task_to_remove is None:
            return

        # remove the user from task
        task_to_remove.remove_user(user_id=user_id)
    # ==========================================
    def info(self):
        """Show project information"""
        if not len(self.workers):
            print("Not users")
            return
        self.show_users()
        self.task_info()
# ==========================================
# END


if __name__ == "__main__":
    # creation of user
    jose = User("Jose alfonzo", "jalfonzo7400@interbayamon.edu", "7874281308", 1)
    noah = User("Noah Almeda", "noahalmeda@gmail.com", "7874318538", 2)

    # Creation of task
    task1 = Task(task_id=1, project_id=1, creator_id=jose.user_id, description="Make API")
    task2 = Task(task_id=2, project_id=1, creator_id=jose.user_id, description="Make API FOR MOBILE")
    task3 = Task(task_id=3, project_id=1, creator_id=jose.user_id, description="Finish earthquakes analysis")

    # Create a project
    project = Project(name="CoRe", user_id=jose.user_id, project_id=1)

    # add user
    project.add_user(jose)
    project.add_user(noah)

    # add task to our project
    project.add_task([task1, task2, task3])

    # set the task to user
    project.set_task(jose.user_id, task1.task_id)
    project.set_task(jose.user_id, task2.task_id)
    project.set_task(noah.user_id, task2.task_id)
    project.task_info()

    project.remove_user_from_task(user_id=noah.user_id, task_id=task2.task_id)
    project.task_info()

    project.remove_task(task2.task_id)
    project.task_info()
    project.set_task(noah.user_id, task2.task_id)
    project.task_info()


