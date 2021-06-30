# Implements a registration form, storing registrants in a dictionary, with error messages

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

SPORTS = {
    "Dodgeball":0,
    "Flag Football":0,
    "Soccer":0,
    "Volleyball":0,
    "Ultimate Frisbee":0,
}

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():

    # Validate submission
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")

    # Update registrant count
    SPORTS[sport] += 1

    # Confirm registration
    return redirect("/counts")


@app.route("/counts")
def registrants():
    return render_template("counts.html", sports=SPORTS)
