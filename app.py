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
            "username": request.form.get("username".lower(),
            "password": generate_password_hash(request.form.get("password")))
        }
        mongo.db.users.insert_one(register)


        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Welcome aboard!")
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)