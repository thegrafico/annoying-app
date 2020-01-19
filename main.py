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
from engine.status import Status
from typing import List

# Connect to the database
conn = Sql("./pythonsqlite.db")
conn.init_db()

# # Create a new User in the database
# raul = User("Raul Pichardo", "raul022107@gmail.com", "7873776957")
# nicole = User("Nicole Santiago", "nicole@gmail.com", "9392321555")
#
# raul.user_id = conn.create_user(raul)
# nicole.user_id = conn.create_user(nicole)

users: List[User] = []

users_from_db = conn.get_table("user")

for u in users_from_db:
    users.append(User(name=u[1], email=u[2], number=u[3], user_id=u[0]))

for temp_user in users:
    # print(temp_user.name, temp_user.email, temp_user.number, temp_user.user_id)
    temp_user.info()
