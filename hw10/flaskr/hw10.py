from flask import Flask, render_template, url_for, request, redirect
# import Flask class. A instance of this class will be our WSGI(web server gateway interface) application
from werkzeug import secure_filename
import os

app = Flask(__name__)
# app is the instance created. 
# '__name__' is the name used to find resources on the file system; 
# '__name__' gives Flask an idea what belongs to your application(???)

app.debug = True
# turn on debug mode 1) server provides a helpful debugger 2) server reloads it self on code changes 

@app.route('/')
def main_page():
	return render_template('main_page.html',
							IC_page=url_for('insert_collection'),
							RQ_page=url_for('query'))
# use route() decorator to tell Flask what url should trigger what view function
# render_template: use a template to help write HTML 

@app.route('/insert_collection/', methods=['GET', 'POST'])
def insert_collection():
	if request.method == 'POST':
		# request object is used to access incoming data
		Bib_file = request.files['file']
		print Bib_file.filename
		# file object is stored in files attribute of the request object
		filename = secure_filename(Bib_file.filename)
		# 'never trust user input'; secure the filename
		Bib_file.save(os.path.join('~/Desktop', filename))
		# save the file
		return redirect(url_for('main_page'), filename=filename)
	return render_template('insert_collection.html',
							m_page=url_for('main_page'))

@app.route('/query/')
def query():
	return 'query'

if __name__=='__main__':
	app.run()
# make the script be able to run in terminal
 