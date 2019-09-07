"""
Connect python to slqlite
"""

import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
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
def main(path_db):
    database = r"{}".format(path_db)
 
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        userid integer,
                                        project_name text NOT NULL,
                                        description text,
                                        FOREIGN KEY (userid) REFERENCES user (id) ON DELETE CASCADE
                                    ); """
    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS task (
                                    id integer PRIMARY KEY,
                                    description text NOT NULL,
                                    priority integer,
                                    project_id integer NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE
                                );"""

    sql_create_users_table = """CREATE TABLE IF NOT EXISTS user (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                email text NOT NULL,
                                number text NOT NULL
                                );""" 
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
    # create a database connection
    conn = create_connection(database)
 
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

#==run
if __name__ == '__main__':
    main(r"./pythonsqlite.db")