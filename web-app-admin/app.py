from flask import Flask, render_template, request, redirect, url_for, make_response, flash
from bson.objectid import ObjectId
from dotenv import dotenv_values

import pymongo
import datetime

# instantiate the app
app = Flask(__name__, static_url_path='/static')
app.secret_key = 'secret'  # Change this!

# modules for user authentication
import flask_login
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

#set up flask-login for user authentication
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

config = dotenv_values(".env")

# turn on debugging if in development mode
if config['FLASK_ENV'] == 'development':
    # turn on debugging, if in development
    app.debug = True # debug mnode

# connect to the database
cxn = pymongo.MongoClient(config['MONGO_URI'], serverSelectionTimeoutMS=5000)
try:
    # verify the connection works by pinging the database
    cxn.admin.command('ping') # The ping command is cheap and does not require auth.
    db = cxn[config['MONGO_DBNAME']] # store a reference to the database
    print(' *', 'Connected to MongoDB!') # if we get here, the connection worked!
except Exception as e:
    # the ping command failed, so the connection is not available.
    # render_template('error.html', error=e) # render the edit template
    print(' *', "Failed to connect to MongoDB at", config['MONGO_URI'])
    print('Database connection error:', e) # debug

# class to represent user
class User(flask_login.UserMixin):
    def __init__(self,data):
        self.id = data['_id'] # shortcut to _id field
        self.username = data['username']
        self.data = data # all user 

def locate_user(user_id=None, username=None):
    '''
    Return a User object for the user with the given id or email address, or None if no such user exists.
    @param user_id: the user_id of the user to locate
    @param email: the email address of the user to locate
    '''
    if user_id:
        criteria = {"_id":ObjectId(user_id)}
    else:
        criteria = {"username":username}
    
    doc = db.admins.find_one(criteria) # find user w/ this email
    # if user exists, create user object and return
    if doc:
        user = User(doc)
        return user
    #else
    return None

@login_manager.user_loader
def user_loader(user_id):
    #   This function is called automatically by flask-login with every request the browser makes to the server.
    return locate_user(user_id=user_id)

# make the currently-logged-in user, if any, available to all templates as 'user'
@app.context_processor
def inject_user():
    # print(flask_login.current_user)
    return dict(user=flask_login.current_user)

# set up the routes

# route for the home page
@app.route('/')
def home():
    """
    Route for the home page before login
    """
    if flask_login.current_user.is_authenticated:
        return render_template('user_home.html', username=flask_login.current_user.data['username'])
    return redirect(url_for('login'))
        
	
####################
# login and register
####################

@app.route('/login',methods=['GET'])
def login():
    if (flask_login.current_user.is_authenticated):
        flash('You are already logged in!')
        return redirect(url_for('home'))
    return render_template('login.html', error='')


@app.route('/login',methods=['POST'])
def login_submit():
    username = request.form['username']
    password = request.form['password']
    user = locate_user(username=username)
    print(user)
    if user and check_password_hash(user.data['password'],password):
        flask_login.login_user(user)
        flash('Welcome back!')
        return redirect(url_for('home'))
    return render_template('login.html', error = 'Wrong Password')

@app.route('/logout')
def logout():
    flask_login.logout_user()
    flash('You have been logged out.  Bye bye!')
    return redirect(url_for('login'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    if (flask_login.current_user.is_authenticated):
        flash('You are already logged in!')
        return redirect(url_for('home'))
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        password = generate_password_hash(password)
        email = request.form.get('email')
        if locate_user(username=username):
            return render_template('register.html', error='User already exists!')
        elif len(username) >= 50:
            return render_template('register.html', error='Please enter a valid username!')
        elif len(email) >= 50 or len(email.split("@")) != 2:
            return render_template('register.html', error='Please enter a valid username!')
        else:
            user = {
                "username": username,
                "password": password,
                "email": email
                }
            user_id = db.admins.insert_one(user).inserted_id
            return redirect(url_for('login'))

@app.route('/add', methods=['POST', 'GET'])
def add_apartment():
    if not flask_login.current_user.is_authenticated:
        return redirect(url_for('login'))
    if request.method == 'GET':
        return render_template('add_apartment.html', username=flask_login.current_user.data['username'])
    else:
        admin_id = flask_login.current_user.id
        name = request.form.get('name')
        address = request.form.get('address')
        borough = request.form.get('borough')
        photo = request.form.get('photo')
        year_of_construction = int(request.form.get('year_of_construction'))
        price = float(request.form.get('price'))
        if request.form.get('pet_friendly') == 'pet_friendly':
            pet_friendly = True
        else:
            pet_friendly = False
        if request.form.get('doorman') == 'doorman':
            doorman = True
        else:
            doorman = False
        if request.form.get('laundry_in_building') == 'laundry_in_building':
            laundry_in_building = True 
        else:
            laundry_in_building = False
        if request.form.get('parking') == 'parking':
            parking = True
        else:
            parking = False
        if request.form.get('elevator') == 'elevator':
            elevator = True
        else:
            elevator = False
        if request.form.get('gym') == 'gym':
            gym = True
        else:
            gym = False
        # if locate_user(username=username):
        #     return render_template('register.html', error='User already exists!')
        # elif len(username) >= 50:
        #     return render_template('register.html', error='Please enter a valid username!')
        # elif len(email) >= 50 or len(email.split("@")) != 2:
        #     return render_template('register.html', error='Please enter a valid username!')
        # else:
        apartment = {
            "admin_id": admin_id,
            "name": name,
            "address": address,
            "borough": borough,
            "photo": photo,
            "year_of_construction": year_of_construction,
            "price": price,
            "pet_friendly": pet_friendly,
            "doorman": doorman,
            "laundry_in_building": laundry_in_building,
            "parking": parking,
            "elevator": elevator,
            "gym": gym
            }
        apt_id = db.apartments.insert_one(apartment).inserted_id

        new_apartment = db.apartments.find_one({"_id": apt_id})
        print(new_apartment)
        return redirect(url_for('home'))

# run the app
if __name__ == "__main__":
	app.run()
