from flask import Flask, render_template, request
from openexcel import read_data
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def handle_login():
    if request.method == "POST":
        username = request.form["username"]
        pwd = request.form["password"]
    else:
        username = request.args.get("username")
        pwd = request.args.get("password")

    data = read_data()

    # usually a db query checking if a user exists and what are his/her priviliges

    # TASK 1. Create a db.txt file containing 5 usernames and passwords. Then
    # Check if username and pwd submitted via the form match and if they math
    # proceed to the welcome screen. Otherwise, display an empty form again with a message
    # "Wrong username or password".
   
    # TASK 2. Check a username and password against data held in Excel file.
    # Write a read_file function inside openexcel.py to retreive information or do it alternatively.
    # Algorithm should work as in Task 1.

    return render_template("welcome.html", username=username, password=pwd)


if __name__ == "__main__":
    app.run(debug=True)