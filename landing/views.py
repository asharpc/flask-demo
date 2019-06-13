from landing import app

@app.route("/")
def hello():
	return '<h1>Hello World Flask</h1>'


@app.route("/about-us/")
def about_us():
	return '<h1>About Us Page</h1>'

@app.route("/user/<username>/")
def profile(username):
	return "<h1>Hello {username}</h1>".format(username=username)