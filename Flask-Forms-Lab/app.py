from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "PeterVal"
password = "112358"
facebook_friends=["Steve","Gamadul","Cunt", "Stav", "Hochberg", "Guy"]

@app.route('/home')
def home():
	return render_template("home.html", friends= facebook_friends)


@app.route('/', methods= ["GET", "POST"])  # '/' for the default page
def login():
	if request.method == "POST":
		user = request.form["username"]
		pas = request.form["password"]
		if user == username and pas == password:
			return render_template("home.html")
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)