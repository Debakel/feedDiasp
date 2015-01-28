#!/usr/bin/env python
# -*- coding: utf-8 -*-
import diaspy
class Diasp:
	def __init__(self, pod=None, username=None, password=None):
		self.pod	= pod
		self.username = username
		self.password = password
		self.logged_in = False
	def login(self):
		print 'Anmelden als '+self.username+' bei '+self.pod		
		try:
			self.c = diaspy.connection.Connection(pod=self.pod, username=self.username, password=self.password)
			self.c.login()	
			self.stream = diaspy.streams.Stream(self.c)
			self.logged_in = True
		except Exception as e:
			print 'Fehler beim Login: ' + str(e)
	def post(self, text, title=None, hashtags=None, source=None, append=None):
		if not self.logged_in:
			self.login()
		if title is not None:
			text = '### ' + title + '\n\n' + text	
		if source is not None:
			text  += '\n\n\nVon: ' + source
		if hashtags is not None and len(hashtags) > 0:
			text += '\n\nHashtags: '
			for hashtag in hashtags:
				text += '#' + hashtag + ' '	
		if append is not None:
			text += '\n' + append
		self.stream.post(text)
