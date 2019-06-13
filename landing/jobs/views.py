from landing import app
from flask import render_template

@app.route("/jobs/<username>/<job_id>/")
def jobs(username,job_id):
	context = {'job_id':job_id}
	if job_id == '007':
		context['right_user_message'] = 'yheaa you are james bond'
	else:
		context['right_user_message'] = 'you are a regular employee'	
	return render_template('job_detail.html',context=context,username=username,job_ids=[3434,564,6,5656,56,6,56,56456])


@app.route("/jobs/")
def job_list():
	return	render_template('job_list.html') 

from flask import jsonify
@app.route("/jobs/api/")
def jobs_api():
	data = {'jobs_id': 65756, 'tasks': [12,4543,654654,56,5765]}
	return jsonify(data)