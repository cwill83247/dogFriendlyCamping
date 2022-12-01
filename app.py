import os                                   

from flask import (                         
    Flask, flash, render_template,
    redirect, request, session, url_for)                    

from flask_pymongo import PyMongo               
from bson.objectid import ObjectId              
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):                
    import env

#flask instance called app
app = Flask(__name__)                   
#Creating DB Connection
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")   
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)     

#homepage
@app.route("/")
def homepage():                            
    return render_template("index.html")


#register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(                        
            {"username": request.form.get("username").lower()})

        if existing_user:                                               
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {                                                           
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))    
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()            
        flash("Thank you for registering!")
        return redirect(url_for("homepage", username=session["user"]))            
    
    return render_template("register.html")


#login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(                       
            {"username": request.form.get("username").lower()})        

        if existing_user:                                          
            # ensure hashed password matches user input
            if check_password_hash(                                             
                existing_user["password"], request.form.get("password")):   
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for("homepage", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


#logout
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")                             
    return redirect(url_for("login"))


#add a DFC venue
@app.route("/add_venue", methods=["GET", "POST"])        
def add_venue():
    if request.method == "POST":                                     
        venue = {                                                              
            "venue_name": request.form.get("venuename"),
            "venue_type": request.form.get("venuetype"),
            "location": request.form.get("location"),
            "description": request.form.get("description"),
            "dog_specific_features": request.form.get("dog_specific_features"),
            "date_visited": request.form.get("datevisited"),
            "added_by": session["user"]                       # adding users session so that we have a record of who created it --- 
        }
        mongo.db.campingVenues.insert_one(venue)                             # inserting task variable into the DB
        flash("Thanks for adding a venue")                            # message to user
        return redirect(url_for("homepage"))                       # then going back  to the get_tasks function but is actually tasks.html 

    venueType = mongo.db.venueType.find().sort("venue_type", 1)
    return render_template("add_venue.html", venueType=venueType)


#list the campsites
@app.route("/list_venues")
def list_venues():                            #function
    venues = list(mongo.db.campingVenues.find())            
    return render_template("list_venues.html", venues=venues)       


#tell app how and when to run
if __name__ == "__main__":                              
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),          
            debug=True)          

