import datetime
from status import Status


class Task:
    task_id: int  # Unique identifier
    description: str
    priority: int
    status: Status
    creating_date: str
    end_date: str
    project_id: int  # project id where the task belong
    creator_id: int  # user id which created the task
    assigned_ids: [int]  # user id in which task is assigned

    def __init__(self, task_id: int, project_id: int, creator_id: int = None, assign_to: [int] = [],
                 description: str = None):
        self.task_id = task_id
        self.project_id = project_id
        self.creator_id = creator_id
        self.assigned_ids = assign_to
        self.creating_date = str(datetime.datetime.today())
        self.status = Status.INCOMPLETE
        self.description = description
        self.users = list()

    # --
    def assign_users(self, user_id: int):
        """
        Assign user to the task
        param: user_id -> id of the user to add
        """

        if user_id < 1:
            return

        if user_id not in self.assigned_ids:
            self.assigned_ids.append(user_id)
    # --
    def remove_user(self, user_ids: [int]):
        """
        remove one or multiple user from task
        user_id: list of user_id to remove task
        """
        # verify is empty
        if not len(user_ids):
            return

        # Iter in all user_ids
        for ID in user_ids:

            # verify is user_id is have this task assigned
            if ID in self.assigned_ids:

                # remove the user
                self.assigned_ids.remove(ID)

    def change_status(self, status: Status):
        """Change the status of the task"""
        if self.status != status:
            if status == Status.COMPLETED:
                self.end_date = str(datetime.datetime.today())
            self.status = status
        # TODO: update the database

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

    def get_users(self):
        return self.assigned_ids if len(self.assigned_ids) > 0 else []
