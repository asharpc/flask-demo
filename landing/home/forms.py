from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError

from .models import EmailSignUp

class LandingForm(FlaskForm):
	full_name = StringField('Full name',
		render_kw={"class": "form-control",
					"placeholder":"full name"

		},
		validators=[
		validators.DataRequired(
			message='Full name is required'
			)
		])
	email = StringField('Email',
		render_kw={"class":"form-control",
					"placeholder":"your email"

		},
		validators=[
			validators.Email(
				message='Enter a valid email'
				)
		])

	def validate_full_name(self, field):
		obj = EmailSignUp.query.filter_by(full_name=field.data).first()
		if obj is not None:
			raise ValidationError('take another username!')

	def validate_email(self, field):
		if field.data.endswith(".edu"):
			raise ValidationError("You cannot use a school email address.")
		obj = EmailSignUp.query.filter_by(email=field.data).first()
		if obj is not None:
			msg = 'this email is already taken'
			raise ValidationError(msg)	
class UpdateForm(FlaskForm):
	full_name = StringField('Full name',
		render_kw={"class": "form-control",
					"placeholder":"edit full name"

		},
		validators=[
		validators.DataRequired(
			message='Full name is required'
			)
		])
	email = StringField('Email',
		render_kw={"class":"form-control",
					"placeholder":"edit your email"

		},
		validators=[
			validators.Email(
				message='Enter a valid email'
				)
		])

