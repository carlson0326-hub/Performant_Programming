# Gator Click
Repository to hold the Gator Click project for the Performant Programming with Python Class

# Purpose 
The purpose of this project is to create web app solely design for the University of Florida
The objective is to allow professors to create questions and popup quiz for students during their
lecutres. It will mainly serve as a form of interactive learning to keep the student engage with 
the course material.

# Features
1) Allow Administrators/Professor to register student to a class
2) Allow students to signup for enrolled course for the semester
3) Allow professor to create questions (essays/multiple choices)
4) Analyze student votes

# Deployment
### Initializing 
To initialize the project, run `pip install virtualenv` in a terminal to make sure you have virtualenv installed. 

Then, cd into the project's first "SemesterProj" folder (the one before the SemesterProj folder with the manage.py file).

### Creating the Virtual Environment
If you're using **Python 2.x**, to create the virtual environment "venv" you run, 
```
virtualenv venv
```

If you're using **Python 3.x**, to create the virtual environment "venv" you run,
```
python3 -m venv venv
```

### Activating the Virtual Environment
Before you can start working, you need to activate the virtual environment. <br>
If you're **Windows** you run,
```
venv\Scripts\activate.bat
```

If you're **Mac** you run,
```
source venv/bin/activate
```

### Installing Django
Once the virtual environment is running, it should have a "(venv)" precedint your terminal prompt. It should look something like this:
```
(.env) aalonso@MacBook-Pro ClickerApplication $
```
Moving forward, all the python pakcages will be installed inside the virtual environment. You must make sure it is activated before installing anything.

Now, we need to install Django to begin working. To do this, we run
```
pip install Django
```

### Starting up the server
Go inside the project directory, called "SemesterProj". Inside you should see the *manage.py* file. 
To start up the server, run
```
python manage.py runserver
```

### Development
Most development will be done in the "Quiz" application, so create views and models here. 
# Developers
### Moise Jean:  
BackEnd developer
### Carlson A Joseph:
Project Manager
### Alejandro Alonso:
Front End developer
### Hannah E Mceachern:
Front End developer
### Andrew So:
Back End developer
