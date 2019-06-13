from landing import app
from flask import render_template,request
import json



from .forms import LandingForm
@app.route("/home/", methods=['GET','POST'])
def home():
	# form = LandingForm()
	# print("json",request.data)
	# print(request.form)
	# if request.method == 'POST':
	# 	data = request.stream.read().decode('utf-8')
	# 	print(data)
		# final_data = json.load(data)
		# print(final_data['hello'])
	form = LandingForm()
	if form.validate_on_submit():
		print(form.full_name.data)
		print(form.email.data)
	return render_template('home.html',form=form)