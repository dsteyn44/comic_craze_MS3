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


# ----------------------------------------adding route to home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


# adding the decorator that includes a route to function
@app.route("/")
@app.route("/get_comics")
def get_comics():
    comics = list(mongo.db.comics.find())
    return render_template("comics.html", comics=comics)


# search function
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    mongo.db.comics.create_index([("superhero", "text"), (
        "title", "text")])
    comics = list(mongo.db.comics.find({"$text": {"$search": query}}))
    return render_template("comics.html", comics=comics)


# ---Our sign-up page---
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
            "fav_superhero": request.form.get("fav_superhero").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Welcome aboard, {}".format(
            request.form.get("username")))
        return redirect(url_for("profile", username=session["user"]))

    return render_template("signup.html")


# ---build login functionality
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
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("signin.html")


# ---Creating profile function---
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
     # Users can access only
    if not session.get("user"):
        return render_template("error_handlers/404.html")
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        if session["user"] == "admin":
            user_comics = list(mongo.db.comics.find())
        else:
            # Comics are only available to user
            user_comics = list(
                mongo.db.comics.find({"created_by": session["user"]}))
        return render_template(
            "profile.html", username=username, user_comics=user_comics)
    return redirect(url_for("login"))


# log out session
@app.route("/logout")
def logout():
    # remove session cookies
    flash("Sad to see you go! {}".format(
                            request.form.get("username")))
    session.pop("user")
    return redirect(url_for("login"))


# Build the POST method
@app.route("/add_comics", methods=["GET", "POST"])
def add_comics():
    if not session.get("user"):
        return render_template("error_handlers/404.html")

    if request.method == "POST":
        ad_comic = {
            "superhero": request.form.get("superhero"),
            "author": request.form.get("author"),
            "date_released": request.form.get("date_released"),
            "title": request.form.get("title"),
            "grade_star": request.form.get("grade_star"),
            "publisher": request.form.get("publisher"),
            "cover_image": request.form.get("cover_image"),
            "comment": request.form.get("comment"),
            "created_by": session["user"]
            }

        mongo.db.comics.insert_one(ad_comic)
        flash("Comic Successfully Added")
        return redirect(url_for("profile", username=session['user']))

# Add rating/grader for cards
    grades = mongo.db.grades.find().sort("grade_star", 1)
    return render_template("add_comics.html", grades=grades)


# Add edit decorator for comics
@app.route("/edit_comic/<comic_id>", methods=["GET", "POST"])
def edit_comic(comic_id):
    if request.method == "POST":
        submit = {
            "superhero": request.form.get("superhero"),
            "author": request.form.get("author"),
            "date_released": request.form.get("date_released"),
            "title": request.form.get("title"),
            "grade_star": request.form.get("grade_star"),
            "publisher": request.form.get("publisher"),
            "cover_image": request.form.get("cover_image"),
            "comment": request.form.get("comment"),
            }

        mongo.db.comics.update({"_id": ObjectId(comic_id)}, submit)
        flash("Task Successfully Updated")

    comic = mongo.db.comics.find_one({"_id": ObjectId(comic_id)})
    grades = mongo.db.grades.find().sort("grade_star", 1)
    return render_template("edit_comics.html", comic=comic, grades=grades)


# ---Adding delete function for comics in comic.html---
@app.route("/delete_comic/<comic_id>")
def delete_comic(comic_id):
    mongo.db.comics.remove({"_id": ObjectId(comic_id)})
    flash("Be gone Evil Fiend!!")
    return redirect(url_for("profile", username=session['user']))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
