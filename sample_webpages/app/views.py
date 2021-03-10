from app import apps
from flask import render_template,request,redirect

@apps.route("/about")
def names():
    return "Hell world 123"

@apps.route("/index")
def names1():
    return render_template("/public/index.html")

@apps.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    return render_template("/public/signup_1.html")

# export FLASK_APP=run.py;export FLASK_ENV=development