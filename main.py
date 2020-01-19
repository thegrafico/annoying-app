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

# ============================== END SETUP =====================================
login_options = """ 1. Create Account\n 2. Login\n 3. Forgot password"""


def create_user():
    name = input("Insert username: ")

    # TODO: verify password len, number, lower and upper
    password = Encrypt.encrypt_data(key=KEY, data=input("Insert Password: "))

    email = input("Insert email: ")

    number = input("Insert phone number: ")

    new_user = User(name=name, email=email, number=number)
    Sql.create_user(user=new_user, password=password)