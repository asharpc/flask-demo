from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return '<h1>Hello World Flask</h1>'


@app.route("/about-us/")
def about_us():
	return '<h1>About Us Page</h1>'

@app.route("/user/<username>/")
def profile(username):
	return "<h1>Hello {username}</h1>".format(username=username)

# if __name__ == '__main__':
#     app.run()