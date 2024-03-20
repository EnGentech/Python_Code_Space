from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LoginForm

app = Flask("na")

app.secret_key = 'e8f62ae662f9b5677fcb601ca848590801982d9a2b33adda'

posts = [
    {
        'author': "Gentle Inyang",
        'title': 'blog post 1',
        'content': 'First post content',
        'date_posted': '28 July 2022'
    },
{
        'author': "EnGentech services",
        'title': 'blog post 2',
        'content': 'Second post content',
        'date_posted': '20 July 2022'
    }
]

@app.route("/home")
@app.route("/", strict_slashes=False)
def home():
    return render_template("home.html", post=posts)

@app.route("/about", strict_slashes=False)
def about():
    return render_template("about.html", title="About")

@app.route("/register", strict_slashes=False, methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="register", form=form)

@app.route("/login", strict_slashes=False, methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'admin':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Check your login details or sign-up', 'danger')
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)