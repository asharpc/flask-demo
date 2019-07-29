from flask import Flask, request
import redis 

from rq import Queue


from landing import app
from flask import render_template


import time

r = redis.Redis()

q = Queue(connection=r)

def background_task(n):
	delay = 2
	print("Task running")
	print(f"simulating {delay} second delay")

	time.sleep(delay)
	print(len(n))
	print("task complete")

	return len(n)


@app.route("/task")
def add_task():
	if request.args.get("n"):
		job = q.enqueue(background_task, request.args.get("n"))
		q_len = len(q)
		return f"flask {job.id}  added to queue at {job.enqueued_at} , {q_len} tasks in the queue"