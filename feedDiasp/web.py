from bottle import route, run, template, post, get, request

import diaspy
from diaspy.errors import LoginError, DiaspyError
from DB import Store, Feed
import dataset

	
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
		success=True
	#except LoginError as e:
	#except DiaspyError as e:
	except Exception as e:
		success=False
		return str(e)
	if success:
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
			return 'OK'
		else:
			return 'Bereits in Datenbank: ' + username + ' auf ' + pod
		
	else:
		return 'NE'
@get('/add')	
@route('/')
def index():
	return template('add')

run(host='localhost', port=8080, debug=True)

