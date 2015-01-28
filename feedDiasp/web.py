from bottle import route, run, template, post, get, request

import diaspy
from diaspy.errors import LoginError, DiaspyError
from DB import Store, Feed
@post('/add')
def add():
	feed = request.forms.get('feed_url')
	username = request.forms.get('username')
	password=request.forms.get('password')
	pod=request.forms.get('pod')
	#try login
	try:
		c=diaspy.connection.Connection(pod=pod,username=username, password=password)
		c.login()
		success=True
	except LoginError:
		success=False
	except DiaspyError:
		sucess=False
	except Exception as e:
		success=False
		return str(e)
	if success:
		db=Store()
		feed=Feed(feed=feed, username=username, password=password, pod=pod)
		db.save(feed)
		return 'OK'
		
	else:
		return 'NE'
	
@route('/')
def index():
	return '''
        <form action="/add" method="post">
            Feed: <input name="feed_url" type="text" />
            User: <input name="username" type="text" />
            Passwort: <input name="password" type="text" />
            Pod: <input name="pod" type="text" />
            
            <input value="Eintragen" type="submit" />
        </form>
    '''

run(host='localhost', port=8080)
