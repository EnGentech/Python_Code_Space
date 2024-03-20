from flask import Flask, flash, redirect, url_for, render_template, request, session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3' # users here refers
# the table while others are just the configuration code
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# the above line removes warnings we get sometimes and its optional
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=3)

db = SQLAlchemy(app)  # this creates a db

# Lets create a model for our database
class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        users = request.form['nm']
        session['user'] = users

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session['email'] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.commit()

        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/logout")
def logout():
    if "user" in session:
        logout_user = session["user"]
        flash("You have been logged out @ {}".format(logout_user), "info")
    session.pop('user', None)
    session.pop('email', None)
    return redirect(url_for("login"))

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        use = session['user']

        if request.method == 'POST':
            email = request.form['email']
            session['email'] = email
            flash("Email was saved!", 'info')
        else:
            if 'email' in session:
                email = session['email']

        return render_template("user.html", email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/test")
def test():
    return render_template("new.html")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)