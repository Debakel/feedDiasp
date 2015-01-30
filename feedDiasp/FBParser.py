#!/usr/bin/env python
# -*- coding: utf-8 -*-
import facepy
class FBParser:
	def __init__(self, user, auth_token):
		self.user = user
		self.auth_token = auth_token
		self.graph = facepy.GraphAPI(self.auth_token)
	def update(self):
		pass
	def get_entries(self):
		statuses = self.graph.get(self.user+'/statuses')['data']
		entries=[]
		for status in statuses:
			x={}
			x['id'] = status['id']
			x['content'] = status['message']
			x['title'] = self.build_title(status['message'])
			x['link'] = 'https://facebook.com/' + status['id']
			
			entries.append(x)
		return entries
	def build_title(self, message):
		return ''
		#return message.split(str='\n')
