## import everything we need in the future
import sqlite3
from flask import Flask, request, session, g, redirect,\
				  url_for, abort, render_template, flash
from contextlib import closing

## configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'key'
USERNAME = 'admin'
PASSWORD = 'default'

def connect_db():
	'''a function connects database'''
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()
## create a little application
app = Flask(__name__)
app.config.from_object(__name__)

if __name__ == '__main__':
	app.run()