#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
from Diasp import Diasp
from PostDB import PostDB
from RSSParser import RSSParser
from FBParser import FBParser
class FeedDiasp:
	def __init__(self, pod, username, password, db, parser, keywords=None, append=None):
		#UnicodeEncodeError Workaround
		reload(sys);
		sys.setdefaultencoding("utf8")
		
		#Quelle
		self.feed = parser
				
		#Diaspora
		self.pod = pod
		self.username = username
		self.password = password
		if keywords is not None:
			self.keywords = keywords
		else:
			self.keywords = []
		self.append = append
		self.diasp = Diasp(pod=self.pod, username=self.username, password=self.password)
				
		self.db = PostDB(filename=db) #markiert bereits veröffentlichte Einträge
		
		self.logged_in = False
	def find_hashtags(self, content, keywords):
		hashtags=[]
		for keyword in keywords:
			if keyword in content:
				hashtags.append(keyword)
		return hashtags
	def publish(self):
		if not self.diasp.logged_in:
			self.diasp.login()
		self.feed.update()
		posts = self.feed.get_entries()
		for post in posts:
			if not self.db.is_published(post['id']):
				print 'Veröffentliche: ' + post['title']
				hashtags = self.find_hashtags(post['content'], self.keywords)				
				try:
					self.diasp.post(text=post['content'], title=post['title'], hashtags=hashtags, source=post['link'], append=self.append)
					self.db.mark_as_posted(post['id'])
				except Exception as e:
					print 'Fehler beim veröffentlichen: ' + str(e)		

