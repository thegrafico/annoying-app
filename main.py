"""
author: Raul Pichardo
Description: main application
"""

# Dependencies
from engine.user import User
from engine.project import Project
from engine.task import Task
from db.sql_connection import SQLiteConnection as Sql
import engine.send_email as Email
import engine.encryption as Encrypt
from engine.status import Status
from typing import List

# ============================== SETUP =====================================
# Connect to the database
conn = Sql("./pythonsqlite.db")
conn.init_db()

# key for encryption
KEY = Encrypt.read_key_from_file(file_path="./key.key")  # use default parameter path

# options when application startup
login_options = " 1. Create Account\n 2. Login\n 3. Forgot password"
project_options = " 1. Create Project\n 2. Show Projects\n 3. Select a Project"
invalid_option_message = "Invalid option, Please try again. Type 0 to end the program"

# ============================== END SETUP =====================================


def create_user() -> bool:
    """
    Create a new user and insert into the Database
    :returns: True if user was created
    """

    # TODO: verify len, number, lower and upper

    name = input("Insert username: ")
    password = Encrypt.encrypt_data(key=KEY, data=input("Insert Password: "))
    email = input("Insert email: ")
    number = input("Insert phone number: ")

    # Creating user
    new_user = User(name=name, email=email, number=number)

    # Insert the user into the database
    user_id = conn.create_user(user=new_user, password=password)

    if user_id == -1:
        return False

    return True


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
    decrypted_password = Encrypt.decrypt_data(key=KEY, data=user_data["password"])

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
            print(login_options)

            # Prompt
            user_input = input("Insert Number Option: ")

            # if invalid input
            if user_input not in options.keys():
                print(invalid_option_message)
                continue

            if user_input == "1":
                if create_user():
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
    """
    options = {"1": create_project, "2": show_projects_by_user_id, "3": select_project}

    while True:
        print(project_options)

        user_input = input("Select # Option: ")

        if user_input not in options.keys():
            print(invalid_option_message)
            continue

        # Run the function
        options[user_input](user.user_id)


# ========================================== PROJECTS FUNCTIONS ====================================
# --
def create_project(user_id: int):
    """Create a project for user"""
    print("-- Creating a new Project --")

    name = input("Insert Name: ")
    description = input("Insert Description: ")

    if not conn.create_project(name=name, description=description, user_id=user_id):
        print("There was an error trying to create the project")
        return

    print("New project Added to the user!")


# --
def show_projects_by_user_id(user_id: int):
    """
    Print all the projects for a user
    :param user_id: id of the user
    :return:
    """
    if user_id < 1:
        print("Invalid ID")
        return

    projects = conn.get_projects_by_user_id(user_id=user_id)

    if not len(projects):
        print("You don't have any project")
        return

    print(projects)


# --
def select_project(user_id: int):
    pass

# ========================================================================================================


if __name__ == "__main__":

    # First step
    user = user_is_not_login()

    while not user:
        print("Login failed")
        user = user_is_not_login()

    # Second step
    user_is_login(user)
