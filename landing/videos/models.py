from landing import db
from landing import admin

from flask_admin.contrib.sqla import ModelView


class Video(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255), nullable=True)
	link = db.Column(db.String(255), nullable=True)
	thumbanil = db.Column(db.String(20), nullable=False, default='default_thumb.jpg')

	def save(self, commit=True):
		if commit:
			instance = self
			if not instance.id:
				db.session.add(instance)
			try:
				db.session.commit()
			except Exception as e:
				print("Exception occured\n", e, '\n')
				db.session.rollback()
				return False
			return True
		return False

	def delete(self, commit=True):
		if self.id:
			db.session.delete(self)
			try:
				db.session.commit()
			except Exception as e:
				print("Exception occured\n", e, '\n')
				db.session.rollback()
				return False
			return True
		return False

# admin.add_view(ModelView(Video, db.session))