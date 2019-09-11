"""
Connect python to slqlite
"""

import sqlite3
from sqlite3 import Error
 

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    print("Connecting to the database")
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn
#==================================================
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
#==================================================
def init_db(conn):
    #PROJECT table
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        userid integer,
                                        project_name text NOT NULL,
                                        description text,
                                        FOREIGN KEY (userid) REFERENCES user (id) ON DELETE CASCADE
                                    ); """
    #TASK table
    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS task (
                                    id integer PRIMARY KEY,
                                    description text NOT NULL,
                                    priority integer,
                                    project_id integer NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE
                                );"""

    #USERS TABLE
    sql_create_users_table = """CREATE TABLE IF NOT EXISTS user (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                email text NOT NULL UNIQUE,
                                number text NOT NULL
                                );""" 
    #task users
    sql_create_task_user_table = """CREATE TABLE IF NOT EXISTS TASK_USER (
                                userid integer,
                                taskid integer,
                                status_id integer NOT NULL,
                                begin_date text NOT NULL,
                                end_date text NOT NULL,
                                FOREIGN KEY (userid) REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE,
                                FOREIGN KEY (taskid) REFERENCES task (id) ON DELETE CASCADE ON UPDATE CASCADE
                                );"""

    sql_create_project_user_table = """CREATE TABLE IF NOT EXISTS PROJECT_USER (
                                userid integer,
                                projectid integer,
                                FOREIGN KEY (userid) REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE,
                                FOREIGN KEY (projectid) REFERENCES projects (id) ON DELETE CASCADE ON UPDATE CASCADE
                                );"""

    sql_create_project_task_table = """CREATE TABLE IF NOT EXISTS PROJECT_TASK (
                            taskid integer,
                            projectid integer,
                            FOREIGN KEY (taskid) REFERENCES task (id) ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (projectid) REFERENCES projects (id) ON DELETE CASCADE ON UPDATE CASCADE
                            );"""

    # create tables
    if conn is not None:

        # create users table
        create_table(conn, sql_create_users_table)

        # create projects table
        create_table(conn, sql_create_projects_table)
 
        # create tasks table
        create_table(conn, sql_create_tasks_table)
        
        # create task_user table
        create_table(conn, sql_create_task_user_table)
        
        # create project-users tables
        create_table(conn, sql_create_project_user_table)
        
        # create project-task tables
        create_table(conn, sql_create_project_task_table)
    else:
        print("Error! cannot create the database connection.")


def create_user(conn, user):
    """
    Create a new task
    :conn: connection to database
    :user project: tuple of element
    :return: id inserted
    """
 
    sql = '''INSERT INTO user (id, name, email, number) VALUES(?,?,?,?);'''
    cur = conn.cursor()
    cur.execute(sql, user)

    conn.commit()
    return cur.lastrowid

def get_table(conn, table):
    
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM {}".format(table))
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
#==run
if __name__ == '__main__':

    tables = ['user', 'projects', 'task', 'TASK_USER', 'PROJECT_USER', 'PROJECT_TASK']
    
    raul = [None, "Raul Pichardo", "raul022107@gmail.com","7873776957"]
    
    conn = create_connection("./pythonsqlite.db")
    
    init_db(conn)    
    
    owner_id = create_user(conn, raul)
 
    get_table(conn, "user")

    conn.commit()