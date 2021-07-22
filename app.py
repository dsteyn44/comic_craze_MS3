import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

# adding the decorator that includes a route to function
@app.route("/")
@app.route("/get_comics")
def get_comics():
    comics = mongo.db.comics.find()
    return render_template("comics.html", comics=comics)

# building the registation funtionailty
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check username already in db
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("This town ain't big enough for two of you! Try Again!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Welcome aboard!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("signup.html")

# build login functionality
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check username already in db
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check password matches
            if check_password_hash(
                existing_user["password"], request.form.get("passowrd")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else: 
                # invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # belongs to username
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("signin.html")

# Creating profile function
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab seeion user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)
    # first username from htmnl 2nd from var above 


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
            