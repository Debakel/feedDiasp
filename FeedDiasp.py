#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
from Diasp import Diasp
from PostDB import PostDB
from RSSParser import RSSParser

class FeedDiasp:
	def __init__(self, feed_url, pod, username, password, db, keywords=None):
		#UnicodeEncodeError Workaround
		reload(sys);
		sys.setdefaultencoding("utf8")
		
		#RSS Quelle
		self.feed_url = feed_url
		self.feed = RSSParser(url=feed_url)
		
		#Diaspora
		self.pod = pod
		self.username = username
		self.password = password
		self.keywords = keywords
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
		self.feed.parse()
		posts = self.feed.get_posts()
		for post in posts:
			if not self.db.is_published(post.id):
				print 'Veröffentliche: ' + post.title
				try:
					if 'content' in post:
						text = post.content[0].value
					else:
						text = post.summary
					hashtags = self.find_hashtags(text, self.keywords)
					self.diasp.post(text, title=post.title, hashtags=hashtags, source=post.link)
					self.db.mark_as_posted(post.id)
				except Exception as e:
					print 'Fehler beim veröffentlichen: ' + str(e)		

