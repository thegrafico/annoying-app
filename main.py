"""
Raul Pichardo Avalo
raul022107@gmail.com
start the application
"""

import sys
sys.path.insert(1, './engine')
sys.path.insert(1, './db')
import project, validation
import sql_connection as sql
import re

#GET USER INPUT
def get_input():
    try:
        user_option = int(input("Select: "))
        # print(user_option, type(user_option))
    except:
        user_option = None
        print("Invalid option, Please enter a number available")

    return str(user_option) if user_option or user_option == 0 else get_input()

def create_user(conn):
    name = input("Name: ")
    name = validation.validate_name(name)
    while not name:
        print("Name should be more than 3 charcater and cannot contain any number")
        name = input("Name: ")
        name = validation.validate_name(name)

    #Email
    email = input("Email: ")
    email = validation.validate_email(email)
    while not email:
        print("Invalid email, enter again")
        email = input("Email: ")
        email = validation.validate_email(email)
    
    #NUMBER
    number = input("Format: (###.###.####) \nNumber: ") 
    number = validation.validate_number(number)
    while not number:        
        print("Invalid number, enter again")
        number = input("Format: (###.###.####)\nNumber: ") 
        number = validation.validate_number(number)

    user = (None,name, email, number)
    userid = sql.insert_user(conn, user)

    print("The user {}, with the ID: {}, has been created.\nUse your email to login".format(name, userid))


def open_project(conn, userid = None):
    return sql.get_project_data(conn, userid)

#==Init the program
if __name__ == "__main__": 

    tables = ['user', 'projects', 'task', 'TASK_USER', 'PROJECT_USER', 'PROJECT_TASK']

    conn = sql.create_connection('./db/project_data.db')
    
    if not conn:
        print("Can not connect to the database")
        exit()
        
    sql.init_db(conn)   
    
    print("""
        1. Create an user
        2. Login
        3. Exit""")
   
    user_option = get_input()

    option = {"1": True, "2": True, "3": create_user, "4":True}

    print(user_option)
    option[user_option](conn)

    # sql.insert_user(conn, 'user')

    

    