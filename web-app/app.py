from flask import Flask, render_template, request, redirect, url_for, make_response
from bson.objectid import ObjectId
from dotenv import dotenv_values
from utils import *

import pymongo
import datetime

# instantiate the app
app = Flask(__name__, static_url_path='/static')

# set up the database
cxn = pymongo.MongoClient("db",27017)
db = cxn['containerizedTest']


# set up the routes

# route for the home page
@app.route('/<uid>/')
def home(uid):
    """
    Route for the home page after login
    """
    user = db.users.find_one({'username': uid}) # sort in descending order of created_at timestamp
    return render_template('user_home.html', user=user)

@app.route('/')
def index():
	"""
    Route for the home page before login
    """
	return render_template('guest_home.html')



####################
# login and register
####################

@app.route('/login/', methods=['POST', 'GET'])
def login():
	username=request.form.get('username')
	password=request.form.get('password') 
	user = db.users.find_one({"username": username})
	if db.users.count({"username": username}) > 0 and user["password"] == password:
		return redirect(url_for('home', uid=user['username']))
	else:
        # login unsuccessful
		return render_template('login.html', error='Wrong username or password!')

@app.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        favourite_apt = request.form.get('favourite_apt')
        if db.users.count({"username": username}) > 0:
            return render_template('register.html', error='User already exists!')

        elif len(username) >= 50:
            return render_template('register.html', error='Please enter a valid username!')
		
        elif len(email) >= 50 or len(email.split("@")) != 2:
            return render_template('register.html', error='Please enter a valid username!')

        elif len(favourite_apt) >= 100:
            return render_template('register.html', error='Your favourite_apt name is too long!')

        else:
            # md5_pass = md5(password.encode('utf-8')).hexdigest()
            # new_id = mt.root_new_user_gen_id(user='root')
            user = {
                "username": username,
                "password": password,
                "email": email,
                "favourite_apt": favourite_apt,
                }
            db.users.insert(user);  
            # user = db.users.findOne({"username": username})      
            return redirect(url_for('home', uid=username))

@app.route('/apartments/<address_id>', methods = ['GET','POST'])
def viewApartment():
    pass

@app.route('/reviews/<address_id>', methods = ['GET'])
def reviews(address_id):
    reviews = db.reviews.find({'address_id': address_id})
    print(reviews, flush=True)
    return render_template('reviews.html', reviews=reviews, address_id=address_id)


@app.route('/add_review/<address_id>', methods=['GET','POST'])
def add_review(address_id):
    if request.method == 'GET':
        return render_template('add_review.html', address_id=address_id)
    else: 
        # create a new review with the data the user entered
        review = {
            "comments": request.form.get('comments'),
            "rating": request.form.get('rating',type=int), 
            "added_at": datetime.datetime.utcnow(),
            "address_id": address_id
        }
        db.reviews.insert_one(review) # insert a new review
        return redirect(url_for('reviews',  address_id=address_id))
    

# run the app
if __name__ == "__main__":
	app.run()


# # load credentials and configuration options from .env file
# # if you do not yet have a file named .env, make one based on the template in env.example
# config = dotenv_values(".env")

# # turn on debugging if in development mode
# if config['FLASK_ENV'] == 'development':
# 	# turn on debugging, if in development
# 	app.debug = True # debug mnode

# cxn = pymongo.MongoClient(config['MONGO_URI'], serverSelectionTimeoutMS=5000)
# try:
# 	# verify the connection works by pinging the database
# 	cxn.admin.command('ping') # The ping command is cheap and does not require auth.
# 	db = cxn[config['MONGO_DBNAME']] # store a reference to the database
# 	print(' *', 'Connected to MongoDB!') # if we get here, the connection worked!
# except Exception as e:
# 	# the ping command failed, so the connection is not available.
# 	# render_template('error.html', error=e) # render the edit template
# 	print(' *', "Failed to connect to MongoDB at", config['MONGO_URI'])
# 	print('Database connection error:', e) # debug