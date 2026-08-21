from flask import Flask, request, render_template, session
from v3_bcrypt import *

app = Flask(__name__)
app.secret_key = "super_secret_key"
users = load_users()

@app.route("/")
def home():
    return render_template("index.html", message="") 

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():

    username = request.form["username"]
    password = request.form["password"]

    if username in users:
        return render_template(
            "register.html",
            message="USER ALREADY EXISTS"
        )
    
    if not validate_password(password):
        return render_template(
            "register.html",
            message="INVALID PASSWORD"
        )
    
    hashed_password = hash_password(password)

    users[username] = {
        "password": hashed_password,
        "attempts": 0
    }

    save_users(users)
    
    return render_template(
        "register.html",
        message="USER REGISTERED SUCCESFULLY"
    )

@app.route("/login", methods=["POST"])
def login():


    username = request.form["username"]
    password = request.form["password"]

    if username not in users:
        return render_template(
            "index.html",
            message="INVALID USERNAME OR PASSWORD"
        )

    stored_password = users[username]["password"]

    if users[username]["attempts"] >= 3:
        return render_template(
            "index.html",
            message="ACCESS DENIED"
        )

    password_correct = check_password(password, stored_password)

    if password_correct:
        session["username"] = username

        users[username]["attempts"] = 0
        save_users(users)

        return render_template(
            "dashboard.html",
            username=username
        )

    users[username]["attempts"] += 1
    save_users(users)

    attempts_left = 3 - users[username]["attempts"]

    if users[username]["attempts"] >= 3:
        return render_template(
            "index.html",
            message="ACCOUNT LOCKED"
        )

    return render_template(
    "index.html",
    message=f"INVALID USERNAME OR PASSWORD ({attempts_left} ATTEMPTS LEFT)"
    )

@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return render_template(
            "index.html",
            message="Please login first"
        )
    
    return render_template(
        "dashboard.html",
        username=session["username"]
    )

@app.route("/logout")
def logout():

    session.clear()

    return render_template(
        "index.html",
        message="Logged out succesfully"
    )

if __name__ == "__main__":
    app.run(debug=True)
