import diaspy
from diaspy.errors import LoginError, DiaspyError
from DB import Store, Feed
import dataset
import json

from bottle import route, run, template, post, get, request



@post('/add')
def add():
	fb = request.forms.get('fb')
	feed = request.forms.get('feed_url')
	username = request.forms.get('username')
	password=request.forms.get('password')
	pod=request.forms.get('pod')
	print username+password+pod

	try:
		c=diaspy.connection.Connection(pod=pod,username=username, password=password)
		c.login()

		db=Store()
		if fb is not None and len(fb) > 1:
			source_type='fb'
			source=fb
		else:
			source_type='rss'
			source=feed
		db = dataset.connect('sqlite:///mydatabase.db')
		if db['user'].find_one(username=username, pod=pod, source=source) is None:
			db['user'].insert(dict(source=source, username=username, password=password, pod=pod, source_type=source_type))
			success = True
			message = 'Eintrag hinzugefuegt.'
		else:
			success = False
			message = 'Bereits in Datenbank  (' + username + ' auf ' + pod + ')' 	
	except Exception as e:
		success=False
		message='Login nicht moeglich.'
		
	return json.dumps(dict(success=success, message=message))
@get('/add')	
@route('/')
def index():
	return template('add')

run(host='localhost', port=8080, debug=True)

