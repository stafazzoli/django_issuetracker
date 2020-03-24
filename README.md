# Issue Tracker Web Application
This web application is developed using Django, a high-level Python Web framework. It uses `Python 3.6.3`, `Django 3.0.4` and SQLite database. 

This project includes two main apps:
1. Accounts:
  Using the built-in Django authentication app, the User model extended to include other properties and functionalities.
2. Projects:
  This app manages projects and reported issues for each project. Only superusers can create a project category in the admin panel. Logged in users can create new projects and issues. A project can only be updated/ deleted by its creator.
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
After creating an issue for a project, the assignee can update the issue status to Done, In Progress or Cancelled. 
  Each user can see the issues that are assigned to herself in another view. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Both class-based views and function-based views are used in this application.
  We also used `django-tables2` and `django-filter` for the project list page to employ their DRY features in table rendering and filtering.

The issue tracker web application is also deployed on Heroku:
https://theissuetracker.herokuapp.com/

## Installation
Install dependencies via `requirements.txt`
```shell script
pip3 install requirements.txt
```

## Setting the Environment Variables
Before starting the web application, the value for environment variables should be set. 
For generating value for SECRET_KEY variable, run the following code:
```python
import secrets
generated_value = secrets.token_hex(24)
```
Set the value of the following variables in your OS. In mac, you can add them to `~/.bash_profile` as follows:
```text
export SECRET_KEY='generated_value'
export EMAIL_USER='your_username'
export EMAIL_PASS='your_password'
```
In order to use your Gmail account to send confirmation emails, follow this link to give access to other apps:
https://myaccount.google.com/lesssecureapps

## Running the Web Application
Run the following commands in terminal to have the app running at http://127.0.0.1:8000:
 ```shell script
python manage.py migrate
python manage.py runserver
```
To access the admin panel at http://127.0.0.1:8000/admin, create a superuser with the following command:
```shell script
python manage.py createsuperuser
```

## Installation via Docker
Instead of installing the application and its dependencies on your local machine, you can set up an isolated environment and run the application in a container.
The `Dockerfile` includes the instruction for building the image file for the application. 
`docker-compose.yml` is the services for multi-container docker application. Though being a single-container, we used compose to be able to change the database easily in the future (to PostgreSQL) and also manage environment variables.

Before building the image:
1. Change directory to the root project (`mysite`).
2. Set up environment variables: Create a `.env` file in the root directory of the project (where `Dockerfile` and `docker-compose.yml` are located).
The contents of `.env` the file should be set as `KEY=VALUE`. 
3. Run the following commands to build the image and run the container respectively:
```shell script
docker-compose build
docker-compose up
```
4. The application will be running at http://0.0.0.0:8000/