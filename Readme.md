**Employee Management Microservice**

This is a microservice-based employee management system built using Flask and PostgreSQL. The application allows for CRUD operations on employee records, a user authentication system using Flask-Login, and the ability to view and manage employees through a user-friendly interface.

**Features**

**Authentication:** Login and session management using Flask-Login.

**Employee Management:**

Add new employees

View all employees in a tabular format

Update employee details

Delete employee records

**RESTful API:** JSON endpoints to manage and query employees programmatically.

**Microservice Architecture:**
Modular file organization for scalability and maintenance.
Database: PostgreSQL integration using SQLAlchemy ORM.

**Installation and Setup**

**Prerequisites**

Python 3.8 or higher installed.
PostgreSQL/MySQL database.
Docker (optional, for containerized deployment).

**Steps to Run the Application**

Clone the Repository

Install the requirements

Setup the env variables in the .env.base file

Comment out line number 13 in the main file if your db password does not need parsing.

Run the main.py file, which will start the application, and create the necessary tables in the db.

Run this query manually in your db: INSERT INTO users (username, password) VALUES ('admin', '<hashed_password>');
Give your desired password as input in the  file create_pass and run it, you will the get the hashed password which can be used in the above query

Navigate to http://127.0.0.1:5000/auth/login

This will open the login.html

Login using your username and password which you entered manually in db(Use the original password, not the hashed one.)

Now you can test the functionalities.




