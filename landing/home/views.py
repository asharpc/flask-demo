from landing import app
from flask import render_template,request,redirect
import json



from .forms import LandingForm
from .models import EmailSignUp

@app.route("/home/", methods=['GET','POST'])
def home():
	form = LandingForm()
	if form.validate_on_submit():
		data = form.data
		print(data)
		if 'csrf_token' in data:
			del data['csrf_token']
		obj = EmailSignUp.query.filter_by(email=form.email.data).first()
		if obj is None:
			obj = EmailSignUp(**data)
			obj.save()
		form = LandingForm()
		return render_template('home.html',form=form)
	return render_template('home.html', form=form)

@app.route("/item/<int:id>/", methods=['GET'])
def item_detail(id):
	instance = EmailSignUp.query.filter_by(id=id).first_or_404()
	return render_template('items/detail.html', instance=instance)


@app.route("/item/<int:id>/update/", methods=['GET','POST'])
def item_update(id):
	instance = EmailSignUp.query.filter_by(id=id).first_or_404()
	form = LandingForm(obj=instance)
	if form.validate_on_submit():
		data = fom.data
		print(data)
	return render_template('items/form.html', instance=instance, form=form)