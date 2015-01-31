#!/usr/bin/env python
# -*- coding: utf-8 -*-
from FeedDiasp import FeedDiasp
from RSSParser import RSSParser
from FBParser import FBParser
import dataset
db = dataset.connect('sqlite:///mydatabase.db')
for user in db['user']:
	print user['username'] + '@' + user['pod']  + ': ' + user['source'] 
	if user['source_type'] == 'fb':
		print 'FB ausgelassen'
	elif user['source_type'] == 'rss':
		print 'RSS'
		parser = RSSParser(user['source'])
		diasp = FeedDiasp(parser=parser, username=user['username'], password=user['password'], pod=user['pod'], db='posts.db')
		diasp.publish()
