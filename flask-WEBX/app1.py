from flask import Flask, request, jsonify, render_template
import csv
import os
import re

app = Flask(__name__)

FILE_NAME = "users.csv"


def username_exists(username):
    if not os.path.exists(FILE_NAME):
        return False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[3] == username:
                return True
    return False


def save_user(data):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    email = request.form["email"]
    age = request.form["age"]
    username = request.form["username"]
    password = request.form["password"]

    if len(name) < 3:
        return jsonify({"status": "error", "message": "Name must be at least 3 characters"})

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"status": "error", "message": "Invalid email format"})

    if int(age) <= 0:
        return jsonify({"status": "error", "message": "Age must be positive"})

    if len(password) < 6:
        return jsonify({"status": "error", "message": "Password must contain at least 6 characters"})

    if username_exists(username):
        return jsonify({"status": "error", "message": "Username already exists"})

    save_user([name, email, age, username, password])

    return jsonify({"status": "success", "message": "Registration Successful"})


if __name__ == "__main__":
    app.run(debug=True)