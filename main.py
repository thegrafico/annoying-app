"""
author: Raul Pichardo
Description: main application
"""

# Dependencies
from engine.user import User
from engine.project import Project
from engine.task import Task
import engine.send_email as Email
from engine.helpers_functions import get_int
import engine.encryption as Encrypt
import engine.constans as constant
from engine.constans import conn
import engine.crud.user as user_crud
import engine.crud.project as project_crud

from typing import List


# --
def login(email: str, password: str, attempts: int = 3):
    """
    Login user into the application
    :param email: user email
    :param password: password of the user
    :param attempts: how many time the user try the password
    :returns: User object if user was found, otherwise return None
    """

    if not len(email) or not len(password):
        return None

    user_data = conn.get_user_by_email(email=email)

    if not len(user_data):
        print("User not found")
        return None

    temp_user = None

    try:
        temp_user = User(user_id=user_data["id"], name=user_data["name"],
                         email=user_data["email"], number=user_data["number"])
    except Exception as e:
        print("Error: ", e)
        return None

    if not temp_user:
        return None

    # Decrypt user password to compare
    decrypted_password = Encrypt.decrypt_data(key=constant.KEY, data=user_data["password"])

    counter = 1

    while counter < attempts:
        # Compare
        if decrypted_password == password:
            print("Login successfully")
            return temp_user

        password = input("Wrong Password, Insert Password again: ")
        counter += 1

    print("Failed to login")
    return None


# --
def forgot_password():
    email = input("Insert email: ")
    pass


# --
def user_is_not_login():
    """
    First prompt when user is not login
    :return: User object is user can login, otherwise None
    """

    options = {"1": "Create User", "2": "login", "3": "forgot_password"}

    while True:
        try:

            # message to the user
            print("\n==========================Options==============================")
            print(constant.login_options)

            # Prompt
            user_input = input("Insert Number Option: ")

            # if invalid input
            if user_input not in options.keys():
                print(constant.invalid_option_message)
                continue

            if user_input == "1":
                if user_crud.create_user(conn):
                    print("User created successfully")
                else:
                    print("Error creating the user, please try again.")

            elif user_input == "2":
                return login(input("Insert Email: "), input("Insert password: "))

            else:
                break
        except Exception as e:
            print("Error: ", e)

    return None


# --
def user_is_login(user: User):
    """
    Second Prompt - where user just login. Here the user select the project to work
    :param user: User Object
    :return :
    """
    options = {"1": project_crud.create_project, "2": project_crud.show_projects_by_user,
               "3": select_project_by_id, "4": project_crud.remove_project}

    project_id: int = 0

    while True:
        print(constant.project_options)

        user_input = input("Select # Option: ")

        if user_input == "0":
            break

        # If the user_input is not in the dict, start again.
        if user_input not in options.keys():
            print(constant.invalid_option_message)
            continue

        # Run the function
        options[user_input](user)


# --
def select_project_by_id(user: User) -> int:
    """
    Select a project for work
    :param user: user object to select the project
    :return : project_id
    """

    user.projects = project_crud.get_projects_by_user_id(user.user_id)

    if not len(user.projects):
        return 0

    user_input = get_int("Select the project id: ")

    all_projects_id = user.get_projects_id()

    while user_input not in all_projects_id:
        user_input = get_int("Select the project id: ")

    project = user.get_project_by_id(user_input)

    print("===== PROJECT INFO =====")
    project.info()

    project_crud.work_in_project(project)
# ========================================================================================================


# Test Running
if __name__ == "__main__":

    # First step
    user = user_is_not_login()
    print("===============================================================")

    while not user:
        print("Login failed, Try again or type 0 to end the program")
        user = user_is_not_login()

    user_is_login(user)

    conn.close_connection()
    # Third Step - user is working in a project

