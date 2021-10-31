from flask import Flask, request, render_template, url_for,redirect
import random
from database import *

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

## Your code goes here! ##
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/form', methods=['GET','POST'])
def form():
  if request.method == "GET":
    return render_template('form.html')
  elif request.method == "POST":
    name = request.form['name']
    email = request.form['email']
    place = request.form['place']
    jobtype = request.form['jobtype']
    when = request.form['when']
    worker = request.form['worker']
    add_user(name,email,place,jobtype,when,worker)
    return redirect(url_for('sendto') )
    
@app.route('/sendto')
def sendto():
  return render_template('sendto.html', people=session.query(User).all())

@app.route('/delete/<int:id>')
def delete(id):
  delete_user(id)
  return redirect(url_for('sendto'))



## And doesn't go after this line. ##

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)