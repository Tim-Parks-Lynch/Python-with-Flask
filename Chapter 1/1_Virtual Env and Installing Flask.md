# Info

I'm following Miguel's Mega Tutorial on flask

# Create Virtual Environment

Same as npm install, keeps modules seperate from other project. Use this all the time, if you don't people will know you are a junior developer. Create the virtual environment first and then activate it

in terminal in vs code type:

1. python3 -m venv venv
2. source venv/bin/activate
   > (venv) $\_ is what you should see in the terminal

# Installations

in terminal in vscode in the virtual environment:

1. pip install flask

# Create a package

1. In vscode create a folder called app: mkdir app
2. Inside of app folder create a `__init__.py` file, this makes it a package where it can be imported

# Files in chapter 1 and how they relate

So the app folder in Chapter 1 folder is actually a python package we created by creating a `__init__.py` file. This means it can be imported. The `__init__.py` file itself imports flask, creates an instance of the Flask class (web server) called 'app' and finally also imports app from routes.py. Apparently this import on the bottom of the code is done to handle a circular import issue that is common with flask.

Finally the microblog.py file imports the app variable we created in `__init__.py`. Which if I'm reading this correctly calls the routes.py and makes the whole server available with those routes. We can now run the app in development mode (listed below) and see if it works.

# Importing before running app

We actually need to export an environment variable before running the command flask run

in terminal in venv:

1. export FLASK_APP=microblog.py

# Run app in development

flask run = Command for development to run the app, don't use in production

# Exporting environment variables for flask to use later

You can create environment variable files for flask to use like in JS.

in terminal:

1. pip install python-dotenv
2. Create a file named `.flaskenv` located in the top-level directory of ythe project
3. Inside that file type:
   FLASK_APP=microblog.py

# Stop App in development

Ctrl + C

That is it for now. Deactivate your environment and move onto the next chapter.
