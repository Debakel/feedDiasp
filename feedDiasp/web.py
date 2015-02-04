#!/usr/bin/env python
# -*- coding: utf-8 -*-
import diaspy
from diaspy.errors import LoginError, DiaspyError
from DB import Store, Feed
import dataset
import json

from bottle import route, run, template, post, get, request, static_file

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')
@post('/add')
@get('/add')
@post('/api/add')
@get('/api/add')
def add():
	import feedparser
	
	# Get Postdata
	fb = request.forms.get('fb')
	feed = request.forms.get('feed_url')
	username = request.forms.get('username')
	password=request.forms.get('password')
	pod=request.forms.get('pod')
	if not ('https://' in pod or 'https://' in pod):
		pod = 'https://' + pod

	# Check login data	
	try:
		c=diaspy.connection.Connection(pod=pod,username=username, password=password)
		c.login()
	except Exception as e:
		return api_response(False, 'Loginfehler.')
	
	# Facebook or RSS?
	if fb is not None and len(fb) > 1:
		source_type='fb'
		source=fb
	else:
		source_type='rss'
		source=feed
		# Check feed
		if feedparser.parse(feed).bozo:
			return api_response(False, 'Ungültiger Feed.')
	
	# Save to DB
	try:
		db = dataset.connect('sqlite:///mydatabase.db')
		if db['user'].find_one(username=username, pod=pod, source=source) is None:
			db['user'].insert(dict(source=source, username=username, password=password, pod=pod, source_type=source_type))
			return api_response(True, 'Gespeichert.')
		else:
			return api_response(False, 'Bereits gespeichert.')
	except:
		return api_response(False, 'Datenbankfehler.')
def api_response(success, message):
	return json.dumps(dict(success=success, message=message))	
@get('/api/delete')
@post('/api/delete')
def delete():
	data = request.query
	db = dataset.connect('sqlite:///mydatabase.db')
	users=db['user']
	
	if 'source' not in data:
		result = users.delete(username=data.username, pod=data.pod, password=data.password)
	else:
		result = users.delete(username=data.username, pod=data.pod, password=data.password, source=data.source)
	
	if result:
		message = 'Einträge entfernt.'
	else:
		message = 'Eintrag nicht vorhanden.'
	return json.dumps(dict(success=result, message=message))
@route('/')
def index():
	return template('add')

		
# run server		
run(host='localhost', port=8080, debug=True)
