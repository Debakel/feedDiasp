#!/usr/bin/env python
# -*- coding: utf-8 -*-
class PostDB:
	# Textdatei mit IDs bereits veröffentlicher Einträge
	def __init__(self, filename):
		self.filename=filename
		self.db = open(filename, 'a+')
		self.liste = self.db.read()
	def mark_as_posted(self, post_id):
		self.liste = self.liste + '\n' + post_id
		self.db.write(post_id+'\n')
	def is_published(self, post_id):
		if post_id in self.liste:
			return True
		else:
			return False	
