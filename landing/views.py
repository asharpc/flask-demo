from landing import app, db
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from landing.models import User
from landing.forms import *


@app.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('hello'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data, password=form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Your account has been created! You are now able to log in', 'success')
		return redirect(url_for('login'))
	return render_template('signup.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            login_user(user)
            # next_page = request.args.get('next')
            return redirect(url_for('hello'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route("/")
def hello():
	return '<h1>Hello World Flask</h1>'


@app.route("/about-us/")
def about_us():
	return '<h1>About Us Page</h1>'

@app.route("/myprofile/")
@login_required
def profile():
	if current_user.is_authenticated:
		print("login user")
	user = current_user
	print(dir(user))
	return "<h1>Hello {username}</h1>".format(username=user.username)