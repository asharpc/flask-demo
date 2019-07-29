from landing import app,api
from flask import render_template,request,redirect
import json


from flask_restful import Resource
from .forms import LandingForm,UpdateForm
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
		# form = LandingForm()
		# return render_template('home.html',form=form)
		return redirect("/item/{}/".format(obj.id))
	return render_template('home.html', form=form)

@app.route("/item/<int:id>/", methods=['GET'])
def item_detail(id):
	instance = EmailSignUp.query.filter_by(id=id).first_or_404()
	return render_template('items/detail.html', instance=instance)


@app.route("/item/<int:id>/update/", methods=['GET','POST'])
def item_update(id):
	instance = EmailSignUp.query.filter_by(id=id).first_or_404()
	form = UpdateForm(obj=instance)
	if form.validate_on_submit():
		data = form.data
		print(data)
	return redirect("/item/{}/".format(id))
	return render_template('items/form.html', instance=instance, form=form)

class HelloWorld(Resource):
	def get(self):
		return {'Hello': 'world'}


todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


api.add_resource(HelloWorld, '/api/home')
api.add_resource(TodoSimple, '/api/<string:todo_id>')