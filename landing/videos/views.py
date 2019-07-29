from landing import app
from flask import render_template, redirect, request, url_for

from .models import Video
# from db_setup import init_db


@app.route("/video/", methods=['GET','POST'])
def video_list():
	obj = Video.query.all()
	image_file = url_for('static', filename='video_thumbs/')
	return render_template("video/list.html",instance=obj, image_file=image_file)

@app.route("/video/<int:id>/", methods=['GET'])
def video_detail(id):
	obj = Video.query.filter_by(id=id).first_or_404()
	image_file = url_for('static', filename='video_thumbs/')
	return render_template("video/detail.html",instance=obj,image_file=image_file)

@app.route("/video/<title>/", methods=['GET'])
def video_slug(title):
	obj = Video.query.filter_by(title=title).first_or_404()
	return render_template("video/detail.html",instance=obj)

@app.route('/result/', methods=['POST', 'GET'])
def search_video():
	if request.method == "POST":
		data = request.form.get('q')
		result = Video.query.filter(Video.title.contains(data))
		print(result)
	return "ok"

