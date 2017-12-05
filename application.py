from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required
from datetime import datetime

import plotly.plotly as py
import plotly.graph_objs as go

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///wyguide.db")


@app.route("/")
@login_required
def index():
    new=db.execute("SELECT name, overall, comments FROM teacher_info ORDER BY timestamp ASC LIMIT 10")
    return render_template("index.html", teacher_info = new)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Where the hell is your password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("GET YOUR USERNAME AND PASSWORD RIGHT", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        # Check for username and password and that they match
        if not request.form.get("username"):
            return apology("Missing username!")
        if not request.form.get("password"):
            return apology("Missing password!")
        if not request.form.get("confirmation"):
            return apology("Retype your password!")
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords don't match!")

        # Check if username is already in database
        exists = db.execute("SELECT * FROM users WHERE username = :username",
                            username=request.form.get("username"))
        if len(exists) != 0:
            return apology("That username is taken!")
        # Encrypt password after storing user
        hash = generate_password_hash(request.form.get("password"))
        result = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)",
                             username=request.form.get("username"), hash=hash)

        # Log in automatically (copy from login)
        session["user_id"] = result

        return redirect("/")

@app.route("/change", methods=["GET", "POST"])
@login_required
def password():
    if request.method == "GET":
        return render_template("change.html")
    elif request.method == "POST":
        # Basically compare old password field to what the old password actually was, then compare new password and its confirmation like before
        if not request.form.get("password_1"):
            return apology("Missing original password!")
        if not request.form.get("password_2"):
            return apology("Must provide new password!")
        if not request.form.get("confirmation_2"):
            return apology("Retype your new password!")
        if request.form.get("password_2") != request.form.get("confirmation_2"):
            return apology("New passwords don't match!")

        hash_2 = db.execute("SELECT hash FROM users WHERE id=:id", id=session["user_id"])

        if not check_password_hash(hash_2[0]['hash'], request.form.get("password_1")):
            return apology("Original password is incorrect")
        passhash = generate_password_hash(request.form.get("password_2"))
        db.execute("UPDATE users SET hash=:hash WHERE id=:id", hash=passhash, id=session["user_id"])

        flash("Your password has been changed!")
        return redirect("/")

@app.route("/rank", methods=["GET", "POST"])
def rank():

    classes = db.execute("SELECT * FROM classes")
    teacher = db.execute("SELECT * FROM teachers")

    if request.method == "GET":
        return render_template("rank.html", classes=classes, teacher = teacher)
    elif request.method == "POST":
        teacher = request.form.get("teacher")
        class1 = request.form.get("class")
        session['teacher']=teacher
        session['class1']=class1

        reviews = db.execute("SELECT teacher FROM class_info WHERE name = :class1 AND teacher = :teacher", class1 = class1, teacher = teacher)
        if not reviews:
            return apology("This teacher and class combo is nonexistent!")
        else:
            new=db.execute("SELECT overall, friendliness, clarity, comments FROM teacher_info WHERE class_name = :class1 AND name = :teacher", class1 = class1, teacher = teacher)
            return render_template("ranked.html", class1=class1, teacher=teacher, teacher_info = new)
            return redirect("/ranked")


@app.route("/review", methods=["GET", "POST"])
@login_required
def review():

    classes = db.execute("SELECT * FROM classes")
    teacher = db.execute("SELECT * FROM teachers")

    if request.method == "GET":
        return render_template("review.html", classes=classes, teacher=teacher)
    elif request.method == "POST":
        teacher = request.form.get("teacher")
        session['teacher']=teacher
        class1 = request.form.get("class")
        session['class1']=class1
        reviews = db.execute("SELECT teacher FROM class_info WHERE name = :class1 AND teacher = :teacher", class1 = class1, teacher = teacher)
        if not reviews:
            return apology("This teacher and class combo is nonexistent!")
        else:
            return render_template("reviewed.html", class1=class1, teacher=teacher)

@app.route("/reviewed", methods=["GET", "POST"])
@login_required
def reviewed():
    if request.method == "GET":
        return render_template("reviewed.html")
    if request.method == "POST":
        reviews=db.execute("INSERT INTO teacher_info (name, class_name, overall, clarity, friendliness, comments) VALUES(:name, :class_name, :overall, :clarity, :friendliness, :comments)",
                    name=session.get('teacher'), class_name=session.get('class1'), overall=request.form.get("overall"), clarity=request.form.get("clarity"), friendliness=request.form.get("friendliness"),
                    comments=request.form.get("comments"))
        flash('You successfully submitted a review!')
        return redirect("/")



def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
