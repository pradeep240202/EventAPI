# How to Run Locally

# Clone the Repo
git clone https://github.com/pradeep240202/EventAPI.git

# Navigate to Project folder
cd EventAPI

# Run command 
docker-compose up -d

# It will install all project dependecies and also add 2 sample user , one admin second user(normal)

# For testing of Roles login with admin user first you can create another admin user and also event 
# but if you login with normal user then you can only register yourself and purchase ticket , event creation not allowed

# Admin User Details
username : admin
password : password

# Normal User Details
username : user
password : password

# APIS :

 For register : /api/register/   
 - payload :
 - {
    "username": "",
    "password": "",
    "role": ""  # User or Admin
  } 
 For login : api/login
  - payload :
    {
    "username":"",
    "password":""
    }

# For Events 
  POST /api/events/ - Create a new event (Admin only).
  -payload : 
    {
    "name":"sample",
    "date":"YYYY-MM-DD",
    "total_tickets": 10  # any int value
    }
	GET /api/events/ - Fetch all events (Admin and User).

 # Ticket Purchase 
 POST /api/events/{id}/purchase/ - Purchase tickets for an event.
 - payload :
   {
    "quantity": 10   # any int value 
   }

   # SQl QUERY

   queries.sql

 

 _______________Manual Setup (Without Docker) ___________________

 # Clone the repo
 git clone https://github.com/pradeep240202/EventAPI.git

 # Create virtual env
 python3 -m venv env
 source env/bin/activate

 # Install Dependencies
 pip install -r requirements.txt

 # Change database configuration(I hard coded it to save time in Real time I used to create .env file and use decouple and os to pass value dynamically)
 
 # Run script
 python create_users.py

 # Login to Admin or User(Normal User)

 # Rest Is Same As Above.....................
 

 
