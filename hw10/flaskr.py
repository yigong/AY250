## import everything we need in the future
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect,\
				  url_for, abort, render_template, flash
from contextlib import closing
from werkzeug import secure_filename

UPLOAD_FOLDER = './'



app = Flask(__name__)
# app is the instance created. 
# '__name__' is the name used to find resources on the file system; 
# '__name__' gives Flask an idea what belongs to your application(???)

# turn on debug mode 1) server provides a helpful debugger 2) server reloads it self on code changes 

app.config.update(dict(DATABASE ='/tmp/flaskr.db', DEBUG = True))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
## configuration

#SECRET_KEY = 'key'
#USERNAME = 'admin'
#PASSWORD = 'default'

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
	'''a function connects database'''
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv

def init_db():
	'''initiate a database'''
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

def get_db():
	'''open a new database connection if there is none for current application'''
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

@app.route('/')
def main_page():
	return render_template('main_page.html')
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

@app.route('/query/', methods=['GET', 'POST'])
def query():
	if request.method == 'POST':
		query_str = request.form['query_str']
		return redirect(url_for('with_query', q_str=query_str))
	return render_template('no_query.html')


@app.route('/query/<q_str>', methods=['GET', 'POST'])
def with_query(q_str):
	if request.method == 'POST':
		query_str = request.form['query_str']
		return redirect(url_for('with_query', q_str=query_str))
	db = get_db()
	cur = db.execute(q_str)
	entries = cur.fetchall()
	return render_template('with_query.html', db_entries=entries)




## create a little application
#app.config.from_object(__name__)

if __name__ == '__main__':
	init_db()
	app.run()