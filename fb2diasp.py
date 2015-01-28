#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import diaspy
import feedparser
import sys
class Diasp:
	def __init__(self, pod=None, username=None, password=None):
		self.pod	= pod
		self.username = username
		self.password = password
		self.logged_in = False
	def login(self):
		self.c = diaspy.connection.Connection(pod=self.pod, username=self.username, password=self.password)
		self.c.login()	
		self.stream = diaspy.streams.Stream(self.c)
	def post(self, text):
		self.stream.post(text)
class RSSParser:
	def __init__(self, url):
		self.url = url
	def parse(self):
		self.feed = feedparser.parse(self.url)
	def get_posts(self):
		return self.feed.entries
class PostDB:
	def __init__(self, filename):
		self.filename=filename
		self.db = open(filename, 'a+')
		self.liste = self.db.read()
	def mark_as_posted(self, post_id):
		self.liste = self.liste + '\n' + post_id
		self.db.write(post_id+'\n')
	def already_posted(self, post_id):
		if post_id in self.liste:
			return True
		else:
			return False		
class FB2Diasp:
	def __init__(self, feed_url, pod, username, password, db, hashtags=None):
		#UnicodeEncodeError Workaround
		reload(sys);
		sys.setdefaultencoding("utf8")
		
		self.feed_url = feed_url
		self.pod = pod
		self.username = username
		self.password = password
		self.hashtags = hashtags
		
		self.feed = RSSParser(url=feed_url)
		self.diasp = Diasp(pod=self.pod, username=self.username, password=self.password)
		self.db = PostDB(filename=db)
		self.logged_in = False
	def log(self, msg):
		print msg
	def login(self):
		try:
			print 'Anmelden.'
			self.diasp.login()
			self.logged_in = True
		except:
			print 'Fehler beim Anmelden.'
	def publish(self):
		if not self.logged_in:
			self.login()
		print 'Feed einlesen.'
		self.feed.parse()
		for post in self.feed.get_posts():
			if not self.db.already_posted(post.id):
				print 'Neuer Post: ' + post.title
				try:
					text = '### ' + post.title + '\n\n'
					if hasattr(post, 'content'):
						text += post.content[0].value
					else:
						text += post.summary
					text  += '\n\n\nVon: ' + post.link
					text += '\n\n'
					if self.hashtags is not None:
						for hashtag in self.hashtags:
							text += '#' + hashtag + ' '
					self.diasp.post(text)
					self.db.mark_as_posted(post.id)
				except Exception as e:
					print 'Fehler beim posten.'		
					print e

