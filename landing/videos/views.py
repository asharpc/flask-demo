from landing import app
from flask import render_template, redirect, request, url_for

from .models import Video

from landing import static

import os

@app.route("/video/", methods=['GET','POST'])
def video_list():
	obj = Video.query.all()
	image_file = url_for('static', filename='video_thumbs/')
	return render_template("video/list.html",instance=obj, image_file=image_file)