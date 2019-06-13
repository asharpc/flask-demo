from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError

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

	def validate_email(self, field):
		if field.data.endswith(".edu"):
			raise ValidationError("You cannot use a school email address.")
