import os

from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)

from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# flask instance called app
app = Flask(__name__)

# Creating DB Connection
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# homepage
@app.route("/")
def homepage():
    return render_template("index.html")


# search
@app.route("/search", methods=["GET", "POST"])
def search():
    userssearch = request.form.get("userssearch")
    venues = list(mongo.db.campingVenues.find(
        {"$text": {"$search": userssearch}}))

    if len(venues) > 0:
        return render_template("list_venues.html", venues=venues)

    flash("Sorry no results found please try again")
    return redirect(url_for("list_venues"))


# register
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


# login
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
                return redirect(url_for("myprofile",
                                        username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# users profile
@app.route("/myprofile/<username>", methods=["GET", "POST"])
def myprofile(username):
    venues = list(mongo.db.campingVenues.find())
    # getting the session user 's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("myprofile.html", username=username, venues=venues)


# logout
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# add a DFC venue
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
            "venue_image_url": request.form.get("image_url"),
            "added_by": session["user"]
        }
        mongo.db.campingVenues.insert_one(venue)
        flash("Thanks for adding a venue")
        return redirect(url_for("add_venue"))

    venueType = mongo.db.venueType.find().sort("venue_type", 1)
    return render_template("add_venue.html", venueType=venueType)


# list the campsites
@app.route("/list_venues")
def list_venues():
    venues = list(mongo.db.campingVenues.find())
    return render_template("list_venues.html", venues=venues)


# add a Venue Type
@app.route("/add_venuetype", methods=["GET", "POST"])
def add_venuetype():
    if request.method == "POST":
        venuetype = {
            "venue_type": request.form.get("venuetype"),
            "added_by": session["user"]
        }
        mongo.db.venueType.insert_one(venuetype)
        flash("Thanks for adding a venue type")
        return redirect(url_for("add_venuetype"))

    venueType = mongo.db.venueType.find().sort("venue_type", 1)
    return render_template("add_venuetype.html", venueType=venueType)


# Edit a DFC venue
@app.route("/edit_venue/<venue_id>", methods=["GET", "POST"])
def edit_venue(venue_id):
    if request.method == "POST":
        submit = {"$set": {
            "venue_name": request.form.get("venuename"),
            "venue_type": request.form.get("venuetype"),
            "location": request.form.get("location"),
            "description": request.form.get("description"),
            "dog_specific_features": request.form.get("dog_specific_features"),
            "date_visited": request.form.get("datevisited"),
            "venue_image_url": request.form.get("image_url")

        }}
        mongo.db.campingVenues.update_one({"_id": ObjectId(venue_id)}, submit)
        flash("Venue Updated !")
        return redirect(url_for("list_venues"))

    venue = mongo.db.campingVenues.find_one({"_id": ObjectId(venue_id)})
    venueType = mongo.db.venueType.find().sort("venue_type", 1)
    return render_template("edit_venue.html", venue=venue, venueType=venueType)


# delete venue
@app.route("/delete_venue/<venue_id>")
def delete_venue(venue_id):
    mongo.db.campingVenues.delete_one({"_id": ObjectId(venue_id)})
    flash("Successfully Deleted")
    return redirect(url_for("list_venues"))


# Edit Venue Type
@app.route("/edit_venuetype/<venueType_id>", methods=["GET", "POST"])
def edit_venuetype(venueType_id):
    if request.method == "POST":
        submit = {"$set": {
            "venue_type": request.form.get("venuetype")
        }}
        mongo.db.venueType.update_one({"_id": ObjectId(venueType_id)}, submit)
        flash("Updated !")
        return redirect(url_for("add_venuetype"))

    venueType = mongo.db.venueType.find_one({"_id": ObjectId(venueType_id)})
    return render_template("edit_venuetype.html", venueType=venueType)


# delete venue type
@app.route("/delete_venuetype/<venueType_id>")
def delete_venuetype(venueType_id):
    mongo.db.venueType.delete_one({"_id": ObjectId(venueType_id)})
    flash("Successfully Deleted")
    return redirect(url_for("add_venuetype"))


# tell app how and when to run
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
