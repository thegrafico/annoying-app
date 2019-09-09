# Project management with super-power

Application to control project management. We can create projects, In each project we can add users, assign tasks, etc.

This application uses the CRUD system, so we can create, read, update and delete any project that is created and we also can do the same with task or users that are added to any project.

This application uses SQlite for data persistence.

## functionalities

    -Create project
    
    -Add user to a project
    
    -Add task to a project and an user

    -Give time to complete the task

    -If the program if running, an automated message will be send to all users in the project
    at specific time every 2 days (Owner of the project can change this time)

    -Send email to all users with their task and date-limit 

    -Send whastapp message to the user with their task and date-limit

    -If the user has not completed the task, the time for send the remainder will decrese from two day to one day.

### How to send emails to users in a project
To do so, we have to setup a sender email in the aplicaction (Only Gmail works) and we have to enable insecures-apps in the email configuration, after that, in the applicacion we select the option: ***Setup sender email***.

    Step:
    - Create a new email (Gmail)
    - Go to configuration and allow less secure apps
    - Add credentials in the application

To configure Gmail less secure app [Click Here](https://support.google.com/accounts/answer/6010255?hl=en)

When you complete the step above you are done to send email to any user with any email.

### How to send emails to users in a project
For now, this options only work with google chrome.

When you select this option, google chrome will open a new task to scan your WhatsApp user, when you scan the tag, you are set
to send any automated message through the main application. DO NOT CLOSE THIS NEW TAG, if you do so, you will have to start the same process of scan the tag, but if you keep the task open, you can send any message in any time

### Prerequisites

For now you need Python 3 and install the requirements file. To do so:

in the terminal or command-line:
```
pip install -r requirements.txt
```

## Running the tests

Donwload this repo and open the terminal in the project folder. For now the application works only in the terminal

```
python3 engine/project.py
```

## Authors

* **Raul Pichardo Avalo, Computer Enginner Student with a minor in Computer Science** 

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) file for details


## NOTES:

**This project its still under development**
