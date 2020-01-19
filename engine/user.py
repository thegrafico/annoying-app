""" 
Raul Pichardo
devpichardo@gmail.com

User class to give projects
"""
from engine.project import Project
import engine.validation_for_project as Validation
from engine.task import Task
from typing import List


# Class User
class User:
    user_id: int
    projects: List[Project]
    def __init__(self, name: str, email: str, number: str = "", user_id: int = -1):
        """
        :param name: name of the user
        :param email: email
        :param number: phone number
        :param user_id: id of the user
        """
        self.name = name
        self.email = self.validate_email(email)
        self.number = self.validate_number(number)
        self.user_id = user_id
        self.projects = []
    # ==========================================

    # ==
    def add_project(self, project: Project):
        """
        Add project to user
        :param project: project object
        """
        # get all projects ids
        all_project_id = self.get_projects_id()

        # if the new project is not created, add it to project list
        if project.project_id not in all_project_id:
            self.projects.append(project)
    # ==
    def add_multiple_project(self, projects: List[Project]):
        """
        Add multiple project to the user
        :param projects: list of project to add
        """

        # if the parameter is empty
        if not len(projects):
            return

        # get projects id from user
        all_project_id = self.get_projects_id()

        # Iter all over the projects
        for project in projects:

            # add the project is not exits
            if project.project_id not in all_project_id:

                self.projects.append(project)

                # to avoid duplicates
                all_project_id.append(project.project_id)
    # ==
    def remove_project(self, project_id: int):
        """
        Remove a project by id
        :param project_id: id of the project
        """

        if project_id < 1:
            return

        # projects ids
        all_projects_id = self.get_projects_id()

        # Verify is the project id belong to a project
        if project_id not in all_projects_id:
            return

        # remove the project
        for i in range(len(self.projects)):
            if self.projects[i].project_id == project_id:
                del self.projects[i]
                return
    # ==
    def get_projects_id(self) -> List[int]:
        """
        Return all project id
        :returns: list with all projects id
        """
        # return list with project id
        return [project.project_id for project in self.projects] if len(self.projects) > 0 else []
    # ==
    def get_project_by_id(self, project_id: int) -> Project:
        """
        Return project by id
        :param project_id: id of the project
        :returns Project: Object project
        """
        if project_id < 1:
            return None

        project = list(filter(lambda temp_project: (temp_project.project_id == project_id), self.projects))

        return project[0] if len(project) > 0 else None

    def validate_email(self, email: str) -> str:

        isValid = Validation.validate_email(email)

        return email if isValid else ""
    # ==========================================
    def validate_number(self, number):
        isNumber = Validation.validate_number(number)

        return number if isNumber else ""
    # ==========================================
    def show_projects(self):
        """Show user projects"""
        if not len(self.projects):
            return

        desc = "ID: {}, Name: {}, Description: {}"
        workers = "Workers ID: "
        task = "Task: "
        for p in self.projects:
            print(desc.format(p.project_id, p.name, p.description), end=', ')
            print(workers, p.workers, end=", ")
            print(task, p.tasks)
    # --
    def info(self):
        data = "Name: {}, email: {}, Number: {}, ID: {}"
        print(data.format(self.name, self.email, self.number, self.user_id))

if __name__ == "__main__":

    # Users
    raul = User("Raul Pichardo", "raul022107@gmail.com", "7873776957", user_id=1)
    noah = User("Noah Almeda", "noah@gmail.com", "9392321555", user_id=2)

    # Projects
    p1 = Project(name="CoRe", user_id=raul.user_id, project_id=1)
    p2 = Project("CoRe 2", noah.user_id, 2)

    # Adding projects
    raul.add_project(p1)
    noah.add_project(p2)

    # show projects
    raul.show_projects()

    # get project by user
    raul_p1 = raul.get_project_by_id(p1.project_id)
    raul_p1.add_user(noah.user_id)

    # Task
    task1 = Task(task_id=1, project_id=raul_p1.project_id, creator_id=raul.user_id, description="Create API")
    task2 = Task(task_id=2, project_id=raul_p1.project_id, creator_id=raul.user_id, description="Create Documentation")
    task3 = Task(task_id=3, project_id=raul_p1.project_id, creator_id=raul.user_id, description="Wave people")

    raul_p1.add_task([task1, task2, task3])
    raul_p1.set_task(user_id=noah.user_id, tasks_id=[task2.task_id])
    raul_p1.set_task(user_id=raul.user_id, tasks_id=[task1.task_id, task2.task_id, task2.task_id, 3])

    raul.show_projects()
    raul_p1.task_info()
