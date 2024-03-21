import sqlite3
from flask import Flask, redirect, render_template, request


app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure SQLite3 Library to use SQLite database
# Manage that in routes


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    conn = sqlite3.connect("birthdays.db")
    cur = conn.cursor()
    if request.method == "POST":
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        if not all([name, month, day]):
            return redirect("/")

        cur.execute("INSERT INTO birthdays(name, month, day) VALUES (?, ?, ?)", (name, int(month), int(day)))
        conn.commit()
        return redirect("/")

    else:
        items = cur.execute("SELECT * FROM birthdays")
        return render_template("index.html", items=items)
