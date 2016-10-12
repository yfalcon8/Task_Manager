## <<<<<<< HEAD
from jinja2 import StrictUndefined

# Flask: A class that we import. An instance of this class will be the
# WSGI application.

from flask import Flask, render_template, request, flash, redirect, url_for, jsonify

#######################
#### configuration ####
#######################

# Instantiates Flask. "__name__" is a special Python variable for the name of
# the current module. This is needed so that Flask knows where to look for
# templates, static files, and so on.
app = Flask(__name__)

# Raises an error when an undefined variable is used in Jinja2.
app.jinja_env.undefined = StrictUndefined

# Prevents the need to restart server when HTML/CSS is changed.
app.jinja_env.auto_reload = True


# @app.route('/') is a Python decorator. '/' in the decorator maps directly
# to the URL the user requested which is the homepage. The index function
# is triggered when the URL is visited.
# =======
"""Server file for Task Manager."""

#Import necessary modules, etc.
#Access local env variables
import jinja2
import os
import sys
import quickstart

#Utilize Jinja for HTML templates
from jinja2 import StrictUndefined
#Utilize Flask libraries
from flask import Flask, render_template, request, flash, redirect, session, url_for, jsonify

#Use toolbar for debugging
# from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db

#Instantiates Flask and "__name__" informs Flask where to find files
app = Flask(__name__, static_url_path='/static')
#Set a secret key to enable the flask session cookies and the debug toolbar
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "seKriTz")
#Raises an error when an undefined variable is used in Jinja2
app.jinja_env.undefined = StrictUndefined
#Prevents the need to restart server when HTML/CSS is changed
app.jinja_env.auto_reload = True


###################### Core Routes ##########################

################ Render information on goals and tasks from Model #############

# @app.route('/goals/<int:user_id>', methods=['GET'])
# # @login_form_required
# def render_goals():
#     """Queries DB to render the user's goals and takes them to goals.html"""

#     goals = db.session.query(Goal.active_goals).all()
#     description = db.session.query(Goal.description).all()

#     return render_template("goals.html",
#                            active_goals=goals,
#                            description=description)


# @app.route('/tasks/<int:user_id>', methods=['GET'])
# # @login_form_required
# def render_tasks():
#     """Queries DB for user's tasks and takes them to tasks.html"""

#     tasks = db.session.query(Task.task_name).all()
#     due_date = db.session.query(Task.due_date).all()

#     return render_template("tasks.html",
#                            tasks=tasks,
#                            due_date=due_date)


# # @login_form_required
# # def make_new_task(task_name, due_date, priority, date_added, open_close_status, task_frequency):
# #     """Add a new task to the DB"""

# #     QUERY = """INSERT INTO Task (task_name, due_date, priority, date_added, open_close_status)
# #                VALUES (:task_name, :due_date, :priority, :date_added, :open_close_status)"""
# #     db_cursor = db.session.execute(QUERY, {'task_name': task_name,
# #                                            'due_date': due_date,
# #                                            'priority': priority,
# #                                            'date_added': date_added,
# #                                            'open_close_status': open_close_status})

#     db.session.commit()

#     print "Successfully added task: {}".format(task_name)

# ################ Login/out Registration #####################


# @app.route("/go_register")
# def register_page():
#     """Send to registration form"""

#     return render_template("register.html")


# @app.route("/register", methods=['POST'])
# def register_form():
#     """Register user"""

#     #Accept data from input fields
#     email = request.form.get('email')
#     username = request.form.get('username')
#     password = request.form.get('password')
#     phone_number = request.form.get('phone_number')

#     #Commit new user details to the database
#     user = User(email=email,
#                 username=username,
#                 password=password,
#                 phone_number=phone_number,
#                 )
#     db.session.add(user)
#     db.session.commit()

#     #Send confirmation msg and back to home page
#     flash("Welcome, new user. Let's get things done!")
#     return redirect("/")


# @app.route('/login', methods=['POST'])
# def login_form():
#     """Process login form"""

#     #Accept data from input fields
#     username = request.form.get("username")
#     password = request.form.get("password")

#     #Do these credentials align within the database?
#     uq = User.query
#     user_object = uq.filter_by(email=username).first()
#     if user_object.email == username and user_object.password == password:
#         flash("Hi again!")
#         session["user_email"] = user_object.email
#         session["user_id"] = user_object.user_id
#         user_id = user_object.user_id
#     else:
#         flash("Oops! Email / Password mismatch: Try again.")

#     return redirect("/")


# @app.route('/logout', methods=['POST'])
# def logout_form():
#     """Process logout form"""

#     #Remove session and notify user
#     session.clear()
#     flash("Logged out. Don't be gone for too long!")
#     return redirect("/")

@app.route('/googlecalendar', methods=['GET'])
def google_map():
    return render_template("index-test.html")

@app.route('/testing')
def test_page():
    return render_template("testpage.html")
    
################### Helper Functions #######################

# Listening or requests
if __name__ == "__main__":

    connect_to_db(app)
    #Create tables from models.py
    db.create_all(app=app)
    #Set debug=True in order to invoke the DebugToolbarExtension
    # app.debug = True

    # app.config['TRAP_HTTP_EXCEPTIONS'] = True
    # app.config['Testing'] = True
    #Use of debug toolbar
    # DebugToolbarExtension(app)

    #Run app locally (simple)
    app.run(host='0.0.0.0')
    app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = True


    #Run app locally (full)
    #Points to port to use and turns on debugger
    app.run(port=5000, debug=True, host='0.0.0.0')

    #Run app via Heroku
    # PORT = int(os.environ.get("PORT", 5000))
    # app.run(host="0.0.0.0", port=PORT)
#>>>>>>> rshen91/rachel
