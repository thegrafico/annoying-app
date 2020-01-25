import engine.encryption as Encrypt
from db.sql_connection import SQLiteConnection as Sql

# key for encryption
KEY = Encrypt.read_key_from_file(file_path="./key.key")  # use default parameter path

# options when application startup
login_options = " 1. Create Account\n 2. Login\n 3. Forgot password"

# CRUD project
project_options = " 1. Create Project\n 2. Show Projects\n 3. Select a Project\n 4. Remove project"

working_in_project_options = " 1. Add user\n 2. Add Task\n 3. Assign Task\n 4. Remove user from Task\n" \
                             " 5. Remove Task\n 6. Information\n 7. Select another project"

# Error Message
invalid_option_message = "Invalid option, Please try again. Type 0 to end the program"


# DATABASE CONNECTION
conn = Sql("./pythonsqlite.db")
conn.init_db()

