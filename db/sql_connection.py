"""
    Connect python to slqlite
    TODO: sanitaze the queries
    TODO: Create a new relational model of the database
"""
import sqlite3
from sqlite3 import Error
from engine.user import User


# Class
class SQLiteConnection:

    _conn = None
    
    def __init__(self, filename:str):
        """Connect to the sqlite filename is exits, if not exits then create a new file"""
        try:
            self._conn = sqlite3.connect(filename)
            print("Connected to the database '{}'".format(filename))
        except Error as e:
            print(e)
    # --
    def create_table(self, sql_query: str) -> bool:
        """
        Create a table in the database
        :param:sql_query: query statement for creation of table
        return: true if table was created, otherwise return false
        """
        try:
            c = self._conn.cursor()
            c.execute(sql_query)
            self._conn.commit()
            return True
        except Error as e:
            print(e)
            return False
    # --
    def init_db(self):
        """Create all the tables for the project"""
    
        if self._conn is None:
            print("ERROR: Can't connect to the database")

        # USERS TABLE
        sql_create_users_table = """CREATE TABLE IF NOT EXISTS USER (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    email text NOT NULL UNIQUE,
                                    number text NOT NULL
                                    );""" 
                                    
        # project table
        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS PROJECTS (
                                            id integer PRIMARY KEY,
                                            project_name text NOT NULL,
                                            description text DEFAULT ""
                                        ); """                                
        # TASK table
        sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS TASK (
                                        id integer PRIMARY KEY,
                                        description text NOT NULL,
                                        priority integer DEFAULT NULL,
                                        status text DEFAULT "Incompleted",
                                        creation_date text NOT NULL,
                                        end_date text DEFAULT NULL, 
                                        project_id integer NOT NULL,
                                        ownerId integer NOT NULL, 
                                        FOREIGN KEY (ownerId) REFERENCES user (id) ON UPDATE CASCADE ON DELETE CASCADE
                                        FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE ON UPDATE CASCADE
                                    );"""

        sql_create_task_assignation_table = """CREATE TABLE IF NOT EXISTS TASK_ASSIGNATION (
                                    userid integer,
                                    taskid integer,
                                    FOREIGN KEY (userid) REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE,
                                    FOREIGN KEY (taskid) REFERENCES task (id) ON DELETE CASCADE ON UPDATE CASCADE
                                    );"""

        sql_create_project_user_table = """CREATE TABLE IF NOT EXISTS PROJECT_USER (
                                    user_id integer,
                                    project_id integer,
                                    FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE,
                                    FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE ON UPDATE CASCADE
                                    );"""

        # sql_create_project_task_table = """CREATE TABLE IF NOT EXISTS PROJECT_TASK (
        #                         taskId integer NOT NULL,
        #                         project_id integer NOT NULL,
        #                         FOREIGN KEY (taskId) REFERENCES task (id) ON DELETE CASCADE ON UPDATE CASCADE,
        #                         FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE ON UPDATE CASCADE
        #                         );"""

        # list of queries to create in the database
        db_tables = [sql_create_projects_table, sql_create_tasks_table, sql_create_users_table,
                      sql_create_project_user_table, sql_create_task_assignation_table]
        
        # create all the tables if not exits
        for query in db_tables:
            self.create_table(query)

    # -- 
    def create_user(self, user: User) -> int:
        """
            Create a new user
            :param user: user object
            :return: id of the user inserted
        """
    
        # query for insert
        sql = '''INSERT INTO user (id, name, email, number) VALUES(?,?,?,?);'''
        
        cur = self._conn.cursor()
        
        cur.execute(sql, [None, user.name, user.email, user.number])

        self._conn.commit()

        return cur.lastrowid
    # --
    def delete_user(self, user_id: int) -> bool:
        """
        Remove a user
        :param user_id: id of the user to remove
        """

        query = "DELETE * FROM user WHERE userid = ?"

        cur = self._conn.cursor()
        try:
            cur.execute(query, [user_id])
            self._conn.commit()
        except Exception as e:
            print(e)
            return False

        return True
    # --
    def get_table(self, table: str) -> list:
        """
        Show the information of the table
        :param table: -> table name
        :return: list of tuples of all data
        """
        cur = self._conn.cursor()
        
        cur.execute("SELECT * FROM {}".format(table))
        
        rows = cur.fetchall()
        
        # return the data is there are any, otherwise return an empty list
        return rows if len(rows) > 0 else []
    # --
    def get_user_by_email(self, email: str) -> list:
        
        # an email need a least 3 char (@.es, @.com, etc)
        if len(email) < 4:
            return []
        
        query = "SELECT * FROM USER WHERE email = ?"
        
        cur = self._conn.cursor()
        
        cur.execute(query, [email])
        
        row = cur.fetchall()
        
        print(row)
        
        return row
    # --
    def get_project_data_by_userid(self, user_id: int) -> list:
        """Get all projects by the userID"""
        
        query = """SELECT * FROM projects WHERE userid = ? """
        
        cur = self._conn.cursor()
        
        try:
            cur.execute(query, [user_id])
            return cur.fetchall()
        except:
            print("ERROR: Data can not be found")
            return []
    # --
    def fecth_all_task(self, user_id: int) -> list:
        """Get all task from an user with the user_id"""
        query = "SELECT * FROM TASK where user"
        pass
    
    # --
    def create_project(self, user_id: int, name: str, description: str = "") -> int:
        """
        Create a new project
        :param user_id: -> unique Id of the owner of the project (must exits before)
        :param name: project name
        :param description: description of the project (empty by default) 
        :returns: id of the project created, (id > 0) Good, (id == 0) Bad
        """
        
        if len(name) < 3:
            print("Project name is too short, Try again with a different name")
            return -1
        
        query = "INSERT INTO projects VALUES(?, ?, ?)"
        
        cur = self._conn.cursor()
        
        cur.execute(query, [None, name, description])
        project_id = cur.lastrowid
        
        query = "INSERT INTO PROJECT_USER VALUES(?, ?)"
    
        cur.execute(query, [user_id, project_id])
        
        self._conn.commit()
        
        return project_id
    
    def add_user_to_project(self, user_id: int, project_id: int) -> bool:
        """ Add an user to a new project"""
        
        #TODO: verify is user not in project firts
        
        query = "INSERT INTO PROJECT_USER VALUES(?, ?)"
        
        try:  
            cur = self._conn.cursor()
            cur.execute(query, [user_id, project_id])
            self._conn.commit()
            return True
        except:
            return False
# -- End of class


if __name__ == '__main__':

    tables = ['user', 'projects', 'task', 'TASK_USER', 'PROJECT_USER', 'PROJECT_TASK']
  
    new_user = User(name="Raul Pichardo", email="raul022108@gmail.com", number="7873776957")
  
    conn = SQLiteConnection("./pythonsqlite.db")
    
    conn.init_db()
    
    # new_user.user_id = conn.create_user(new_user) 
    
    # conn.create_project(new_user, "Capstone", "Scrum capstone")
    
    # conn.add_user_to_project(2, 1)
    # conn.add_user_to_project(3, 1)
    # conn.add_user_to_project(4, 1)    
    
    # conn.get_user_by_email(User.email)
    
    for x in conn.get_table("user"):
        print(x)
    
    
