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

#tell app how and when to run
if __name__ == "__main__":                              
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),          
            debug=True)          

