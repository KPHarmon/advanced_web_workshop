from flask import Flask, render_template, render_template_string, request, redirect, request, url_for, make_response
from db import *

# Initialize App
app = Flask(__name__, static_folder='templates/static', static_url_path='')

# SQL Login
@app.route('/', methods=['GET', 'POST'])
def index():
	msg = None
	if request.method == 'POST':
		user = request.form['username']
		password = request.form['password']

		data = query_username(user, password)
		if user == "" or password == "":
			msg = ["Incorrect Password"]
			resp = make_response(render_template('login.html', msg=msg))
		
		if len(data) > 1:
			msg = data
			resp = make_response(render_template('login.html', msg=msg))

		elif request.form['username'] == "crounds3" and request.form['password'] == "niBhfz33d5":
			msg = request.form['username']
			resp = redirect(url_for('profile'))
		else:
			msg = ["Incorrect Password"]
			resp = make_response(render_template('login.html', msg=msg))
		
		return resp

	if request.method == 'GET':
		resp = make_response(render_template('login.html', msg=msg))
		return resp

@app.route('/profile', methods=['GET', 'POST'])
def profile():
	
	usr = 'crounds3'
		
	if request.method == 'POST':
		post = request.form['comment']
		data = query_posts(post)
			
		if post == "":
			msg = None
		else:
			msg = data
		resp = make_response(render_template('profile.html', msg=msg, usr=usr))
		return resp

	elif request.method == 'GET':
		msg = None
	return render_template('profile.html', msg=msg, usr=usr)


if __name__ == '__main__':
	app.run(debug = True)
