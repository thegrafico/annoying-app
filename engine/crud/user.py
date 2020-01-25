"""
CRUD system for user
Create, Read, Update, Delete
"""

import engine.encryption as Encrypt
import engine.constans as constant
from engine.constans import conn
from engine.user import User


# CREATE USER
def create_user() -> bool:
    """
    Create a new user and insert into the Database
    :returns: True if user was created
    """

    # TODO: verify len, number, lower and upper

    name = input("Insert username: ")
    password = Encrypt.encrypt_data(key=constant.KEY, data=input("Insert Password: "))
    email = input("Insert email: ")
    number = input("Insert phone number: ")

    # Creating user
    new_user = User(name=name, email=email, number=number)

    try:
        # Insert the user into the database
        user_id = conn.create_user(user=new_user, password=password)
    except Exception as e:
        print("Error in the Database, ", e)
        return False

    if user_id == -1:
        return False

    return True

# READ USERS

