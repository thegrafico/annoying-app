import datetime
import status


class Task:
    def __init__(self, task_id: int, project_id: int, creator_id: int = None, description: str = None):
        self.task_id = task_id
        self.project_id = project_id
        self.creator_id = creator_id
        self.creating_date = str(datetime.datetime.today())
        self.status = status.Status.INCOMPLETE
        self.description = description
        self.users = list()
        self.start_date = str(datetime.datetime.today())
        self.end_date = None
        self.priority = 0

    # --
    def assign_user(self, user_id: int):
        """
        Assign user to the task
        param: user_id -> id of the user to add
        """

        if user_id < 1:
            return

        if user_id not in self.users:
            self.users.append(user_id)
    # --
    def remove_user(self, user_id: int):
        """
        remove one or multiple user from task
        user_id: list of user_id to remove task
        """
        # verify is empty
        if user_id < 1:
            return

        # verify is user_id is have this task assigned
        if user_id in self.users:
            # remove the user
            self.users.remove(user_id)

    def edit(self, new_values: dict) -> bool:
        """
        param: new_values -> dictionaries with the value
        return True is task was edit
        """
        attr_changed = False

        # verify is have any value
        if not len(new_values):
            return attr_changed

        # key of the new values to add
        keys = list(new_values.keys())

        if "description" in keys:
            self.description = new_values["description"]
            attr_changed = True
        if "status" in keys:
            self.status = new_values["status"]
            attr_changed = True
        if "priority" in keys:
            self.priority = new_values["priority"]
            attr_changed = True

        return attr_changed
    # ==
    def get_users(self):
        return self.users
