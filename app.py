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


# ---adding route to home page incl.template for grades---
@app.route("/")
@app.route("/home")
def home():
    grades = list(mongo.db.comics.find().sort("grades", -1).limit(3))
    return render_template('home.html', grades=grades)


# ---Adding the route decorator for comics---
@app.route("/")
@app.route("/get_comics")
def get_comics():
    comics = list(mongo.db.comics.find())
    return render_template("comics.html", comics=comics)


# ---Search function----
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

        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
    # check if username already exists in db
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "fav_superhero": request.form.get("fav_superhero").lower(),
            "prof_image": request.form.get("prof_image"),
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


# ---build login functionality----
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
                flash("Incorrect Password")
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
            favorite = list(mongo.db.tags.find(
                {"created_by": username}))
        else:
            # Comics are only available to user
            user_comics = list(
                mongo.db.comics.find({"created_by": session["user"]}))
            favorite = list(mongo.db.tags.find(
                {"created_by": username}))

    prof_info = list(mongo.db.users.find({"username": session["user"]}))

    return render_template(
            "profile.html", username=username,
            user_comics=user_comics,
            favorite=favorite,
            prof_info=prof_info)
    return redirect(url_for("login"))


# ---favorites tag on comics for user in Profile---
@app.route("/tag_favorite/<comic_id>")
def tag_favorite(comic_id):
    # grabbing the session user
    if session.get("user"):
        user = mongo.db.users.find_one({"username": session["user"]})
        comic = mongo.db.comics.find_one({"_id": ObjectId(comic_id)})
        tag = {
            "user": user["_id"],
            "comic_id": comic["_id"],
            "superhero": comic["superhero"],
            "author": comic["author"],
            "date_released": comic["date_released"],
            "title": comic["title"],
            "grade_star": comic["grade_star"],
            "publisher": comic["publisher"],
            "cover_image": comic["cover_image"],
            "comment": comic["comment"],
            "created_by": session["user"]
        }

    mongo.db.tags.insert_one(tag)
    return redirect(url_for("profile", username=session['user']))


# ---Adding delete function for tags in profile.html---
@app.route("/delete_tag/<comic_id>")
def delete_tag(comic_id):
    mongo.db.tags.remove({"_id": ObjectId(comic_id)})
    flash("Be gone Evil Fiend!!")
    return redirect(url_for("profile", username=session['user']))


# ---Log out session---
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("home"))


# ---Adding Comics---
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

# ---Add rating/grader for cards---
    grades = mongo.db.grades.find().sort("grade_star", 1)
    return render_template("add_comics.html", grades=grades)


# ---Add edit decorator for comics---
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
    return redirect(url_for("get_comics"))


# ---Get Categories function---
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.catagories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# ---Add Categories function---
@app.route("/add_categories", methods=["GET", "POST"])
def add_categories():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.catagories.insert_one(category)
        flash("New Superhero Added!")
        return redirect(url_for("get_categories"))

    return render_template("add_categories.html")


# ---Edit Categories function---
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.catagories.update({"_id": ObjectId(category_id)}, submit)
        flash("Repaired - Just like new Again!")
        return redirect(url_for("get_categories"))

    category = mongo.db.catagories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# ---delete Categories--
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.catagories.remove({"_id": ObjectId(category_id)})
    flash("Be gone Evil Fiend!!")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
