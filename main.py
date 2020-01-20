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
login_options = """ 1. Create Account\n 2. Login\n 3. Forgot password"""

# ============================== END SETUP =====================================


def create_user():
    """
    Create a new user and insert into the Database
    :returns: new User if user was created, otherwise return None
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
        return None

    new_user.user_id = user_id

    return new_user


# --
def login(email: str, password: str):
    """
    Login user into the application
    :param email: user email
    :param password: password of the user
    :returns: User object if user was found, otherwise return None
    """

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

    if not temp_user:
        return None

    # Decrypt user password to compare
    decrypted_password = Encrypt.decrypt_data(key=KEY, data=user_data["password"])

    # Compare
    if decrypted_password == password:
        print("Login successfully")
        return temp_user

    print("Failed to login")
    return None

# --
def forgot_password():
    email = input("Insert email: ")
    pass


if __name__ == "__main__":

    options = {"1": create_user, "2": login, "3": forgot_password}

    # conn.delete_user(1)
    # conn.delete_user(2)

    while True:
        try:
            print(login_options)

            user_input = input("Insert Number Option: ")

            if user_input == '2':
                email = input("Insert email: ")
                password = input("Insert password: ")
                options[user_input](email, password)
            else:
                # Call the function
                options[user_input]()

        except Exception as e:
            print("Error: ", e)
            break


