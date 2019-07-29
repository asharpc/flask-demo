from flask import Flask, request
import redis 

from rq import Queue

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