from flask import Flask, render_template, render_template_string, request, redirect, request, url_for, make_response
from db import *

# Initialize App
app = Flask(__name__, static_folder='templates/static', static_url_path='')

# SQL Login Page
@app.route('/', methods=['GET', 'POST'])
def index():
	msg = None

	# If the user sents a POST request (i.e. they submit a form) run this logic
	if request.method == 'POST':
		
		# Grab the username and password the user submitted via the form
		user = request.form['username']
		password = request.form['password']

		# Function from db.py that creates a query searching for the username and password in the database
		data = query_username(user, password)

		# If the user left on of the fields blank, return incorrect password
		if user == "" or password == "":
			msg = ["Incorrect Password"]
			resp = make_response(render_template('login.html', msg=msg))
		
		# If the query returns more than on item, return all of the items
		if len(data) > 1:
			msg = data
			resp = make_response(render_template('login.html', msg=msg))

		# If a user logs in with the correct username and password, redirect to the profile page
		elif request.form['username'] == "crounds3" and request.form['password'] == "niBhfz33d5":
			msg = request.form['username']
			resp = redirect(url_for('profile'))

		# If they log in with the wrong credentials, return an incorrect password
		else:
			msg = ["Incorrect Password"]
			resp = make_response(render_template('login.html', msg=msg))
		
		return resp

	If the user sends a POST request (i.e. they open the page without submitting a form) just return the webpage
	if request.method == 'GET':
		resp = make_response(render_template('login.html', msg=msg))
		return resp

@app.route('/profile', methods=['GET', 'POST'])
def profile():
	
	usr = 'crounds3'
		
	# If someone submits a comment, run this logic
	if request.method == 'POST':

		# Grab the comment from the form data and then create a query that inserts the comment into the database
		post = request.form['comment']
		data = query_posts(post)
			
		# If they submitted a blank comment, do nothing
		if post == "":
			msg = None

		# If they submit a comment, return the output from the database
		else:
			msg = data
		resp = make_response(render_template('profile.html', msg=msg, usr=usr))
		return resp

	# If they do not submit a form to the page, just open the page normally
	elif request.method == 'GET':
		msg = None
	return render_template('profile.html', msg=msg, usr=usr)


if __name__ == '__main__':
	app.run(debug = True)
