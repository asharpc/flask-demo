from landing import db

class EmailSignUp(db.Model):
	id  = db.Column(db.Integer,  primary_key=True)
	full_name = db.Column(db.String(120), nullable=True)
	email = db.Column(db.String(120), unique=True, nullable=False)