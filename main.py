"""
Raul Pichardo Avalo
raul022107@gmail.com
start the application
"""

import sys
sys.path.insert(1, './engine')
sys.path.insert(1, './db')


import project
import sql_connection as sql

#GET USER INPUT
def get_input():
    try:
        user_option = int(input("Select: "))
        print(user_option, type(user_option))
    except:
        user_option = None
        print("Invalid option, Please enter a number available")

    return user_option if user_option or user_option == 0 else get_input()

def create_user():
    name = input("Name: ")
    email = input("Email: ")
    number = input("Number: ")
    
#==Init the program
if __name__ == "__main__":        
    print("""
        1. Start a new project
        2. Continue with a project
        3. Create a user
        3. Exit""")
    conn = sql.create_connection('./db/project_data.db')
    sql.init_db(conn)
    option = get_input()
    

    