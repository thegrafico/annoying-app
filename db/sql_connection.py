"""
    Connect python to slqlite
    TODO: sanitaze the queries
    TODO: Create a new relational model of the database
"""
import sys
sys.path.insert(1, './engine')
import sqlite3
from sqlite3 import Error
from user import User

class SQLiteConnection:
    _conn = None
    
    def __init__(self, filename:str):
        """Connect to the sqlite filename is exits, if not exits then create a new file"""
        try:
            self._conn = sqlite3.connect(filename)
            print("Connected to the database '{}'".format(filename))
        except Error as e:
            print(e)
    #--
    def create_table(self, sql_query:str) -> bool:
        """
        Create a table in the database
        param: sql_query:str -> query statement for creation of table
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
    #--
    def init_db(self):
        """Create all the tables for the project"""
    
        if self._conn is None:
            print("ERROR: Can't connect to the database")

        #USERS TABLE
        sql_create_users_table = """CREATE TABLE IF NOT EXISTS USER (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    email text NOT NULL UNIQUE,
                                    number text NOT NULL
                                    );""" 
                                    
        #project table
        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS PROJECTS (
                                            id integer PRIMARY KEY,
                                            project_name text NOT NULL,
                                            description text DEFAULT ""
                                        ); """                                
        #TASK table
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
                                    userId integer,
                                    projectId integer,
                                    FOREIGN KEY (userId) REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE,
                                    FOREIGN KEY (projectId) REFERENCES projects (id) ON DELETE CASCADE ON UPDATE CASCADE
                                    );"""

        # sql_create_project_task_table = """CREATE TABLE IF NOT EXISTS PROJECT_TASK (
        #                         taskId integer NOT NULL,
        #                         projectId integer NOT NULL,
        #                         FOREIGN KEY (taskId) REFERENCES task (id) ON DELETE CASCADE ON UPDATE CASCADE,
        #                         FOREIGN KEY (projectId) REFERENCES projects (id) ON DELETE CASCADE ON UPDATE CASCADE
        #                         );"""

        #list of querys to create in the database
        db_tables = [sql_create_projects_table, sql_create_tasks_table, sql_create_users_table,
                      sql_create_project_user_table, sql_create_task_assignation_table]
        
        #create all the tables if not exits
        for query in db_tables:
            print(self.create_table(query))

    #-- 
    def create_user(self, user:User)->int:
        """
            Create a new user
            param: user_data -> User class
            :return: id of the user inserted
        """
    
        #query for insert
        sql = '''INSERT INTO user (id, name, email, number) VALUES(?,?,?,?);'''
        
        cur = self._conn.cursor()
        
        cur.execute(sql, [None, user.name, user.email, user.number])

        self._conn.commit()

        return cur.lastrowid
    #--
    def get_table(self, table:str)-> list:
        """
        Show the information of the table
        param: table -> table name
        return: list of tuples of all data
        """
        cur = self._conn.cursor()
        
        cur.execute("SELECT * FROM {}".format(table))
        
        rows = cur.fetchall()
        
        #return the data is there are any, otherwise return an empty list
        return rows if len(rows) > 0 else []
    #--
    def get_user_by_email(self, email:str):
        
        #an email need a least 3 char (@.es, @.com, etc)
        if len(email) < 4:
            return True
        
        query = "SELECT * FROM USER WHERE email = ?"
        
        cur = self._conn.cursor()
        
        cur.execute(query, [email])
        
        row = cur.fetchall()
        
        print(row)
        
        return False
    #--
    def get_project_data_by_userid(self, userId:str)->list:
        """Get all projects by the userID"""
        
        query = """SELECT * FROM projects WHERE userid = ? """
        
        cur = self._conn.cursor()
        
        try:
            cur.execute(query, [int(userId)])
            return cur.fetchall()
        except:
            print("ERROR: Data can not be found")
            return []
    #--
    def fecthAllTask(self, userId:int)->list:
        """Get all task from an user with the userId"""
        query = "SELECT * FROM TASK where user"
    #--
    def create_project(self, user:User, name:str, description:str = "")->bool:
        """
        Create a new project
        Param: userId -> unique Id of the owner of the project (must exits before)
        Param: name -> project name
        Param: description -> description of the project (empty by default) 
        return: project id 
        """
        if len(name) < 4:
            print("Project name is too short, Try again with a different name")
            return False
        
        query = "INSERT INTO projects VALUES(?, ?, ?)"
        
        cur = self._conn.cursor()
        
        cur.execute(query, [None, name, description])
        projectId = cur.lastrowid
        
        query = "INSERT INTO PROJECT_USER VALUES(?, ?)"
    
        cur.execute(query, [user.userId, projectId])
        
        self._conn.commit()
        
        return True
    
    def add_user_to_project(self, userId:int, projectId:int)->bool:
        """ Add an user to a new project"""
        
        #TODO: verify is user not in project firts
        
        query = "INSERT INTO PROJECT_USER VALUES(?, ?)"
        
        try:  
            cur = self._conn.cursor()
            cur.execute(query, [userId,projectId])
            self._conn.commit()
            return True
        except:
            return False

        
#-- End of class

#==run
if __name__ == '__main__':

    tables = ['user', 'projects', 'task', 'TASK_USER', 'PROJECT_USER', 'PROJECT_TASK']
  
    new_user = User(name = "Raul Pichardo", email="raul022108@gmail.com", number="7873776957")
  
    conn = SQLiteConnection("./pythonsqlite.db")
    
    conn.init_db()
    
    # new_user.userId = conn.create_user(new_user) 
    
    # conn.create_project(new_user, "Capstone", "Scrum capstone")
    
    # conn.add_user_to_project(2, 1)
    # conn.add_user_to_project(3, 1)
    # conn.add_user_to_project(4, 1)    
    
    # conn.get_user_by_email(User.email)
    
    for x in conn.get_table("user"):
        print(x)
    
    
