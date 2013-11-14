from flask import Flask, render_template, url_for
# import Flask class. A instance of this class will be our WSGI(web server gateway interface) application

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

@app.route('/insert_collection/')
def insert_collection():
	return 'insert_collection'

@app.route('/query/')
def query():
	return 'query'

if __name__=='__main__':
	app.run()
# make the script be able to run in terminal
 