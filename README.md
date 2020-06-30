# Performant_Programming
Repository to hold the project for the Performant Programming with Python Class

To initialize the project, run `pip install virtualenv` in a terminal to make sure you have virtualenv installed. 

Then, cd into the project's first "ClickerApplication" folder (the one before the ClickerApplication folder with the manage.py file).

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
Go inside the project directory, called "ClickerApplication". Inside you should see the *manage.py* file. 
To start up the server, run
```
python manage.py runserver
```

### Development
Most development will be done in the "Quiz" application, so create views and models here. 
