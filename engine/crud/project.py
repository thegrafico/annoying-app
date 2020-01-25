"""
CRUD system for project
Create, Read, Update, Delete
"""

import engine.encryption as Encrypt
import engine.constans as constant
from engine.constans import conn
from engine.user import User
from engine.project import Project
import engine.helpers_functions as helpers
from typing import List


# CREATE A PROJECT
def create_project(user: User):
    """Create a project for user"""
    print("-- Creating a new Project --")

    # TODO: Validate name
    name = input("Insert Name: ")
    description = input("Insert Description: ")

    project_was_created = conn.create_project(name=name, description=description, user_id=user.user_id)

    if project_was_created:
        print("New project Added to the user!")
        return

    print("There was an error trying to create the project")


# REMOVE PROJECT
def remove_project(user: User):
    """
    Remove a project for user
    :param user: user with all projects
    """

    user.projects = get_projects_by_user_id(user.user_id)

    if not len(user.projects):
        return

    msg = "Insert the project id to remove: "
    user_input = helpers.get_int(msg)

    # get all project ids
    all_projects_id = user.get_projects_id()

    while user_input not in all_projects_id:
        print("invalid option, Try again. Type 0 for exit")
        user_input = helpers.get_int(msg)

        if user_input == 0:
            return

    # Remove project from db
    project_was_removed = conn.remove_project_by_id(user_input)

    if not project_was_removed:
        print("Cannot remove the project")
        return

    user.remove_project(user_input)

    print("Project is removed!")


# ======================================= READ PROJECT BY USER ID =========================================
def get_projects_by_user_id(user_id: int) -> List[Project]:
    """
    Get all projects from user
    :param user_id: id of the user
    :returns: list of projects
    """

    if user_id < 1:
        print("Invalid ID")
        return []

    projects = conn.get_projects_by_user_id(user_id=user_id)

    if not len(projects):
        print("\nYou don't have any project\n")
        return []

    # Create list of project
    all_projects: List[Project] = []

    # fill out the projects
    for project in projects:
        all_projects.append(Project(name=project["project_name"], project_id=project["id"],
                                    description=project["description"], user_id=user_id,))

    return all_projects


# SHOW All PROJECTS FROM USER
def show_projects_by_user(user: User):
    """
    Print all the projects for a user
    :param user: user object
    :return all user projects:
    """

    projects = get_projects_by_user_id(user.user_id)

    if not len(projects):
        return

    user.projects = projects

    print("\n========================PROJECTS================================")
    message = "ID: {}, Name: {}, Description: {}"

    for project in projects:
        print(message.format(project.project_id, project.name, project.description))
    print("==================================================================\n")
# ==========================================================================================


# START WORKING IN A PROJECT
def work_in_project(project: Project):
    """
    Start working in a project
    :param project: project to work in.
    :return :
    """

    if not project or type(project) != Project:
        return

    # working_in_project_options = " 1. Add user\n 2. Add Task\n 3. Assign Task\n 4. Remove user from Task\n" \
    #                              " 5. Remove Task\n 6. Information\n 7. Select another project"

    # options = {"1": add_user_for_project, "2": add_task,
    #            "3": set_task, "4": remove_user_from_task,
    #            "5": remove_task, "6": task_info, "7": user_is_login}

    while True:
        print("\n============== WORKING IN PROJECT ==============\n {}".format(project.name))
        print(constant.working_in_project_options)

        user_input = helpers.get_int("Insert # option: ")