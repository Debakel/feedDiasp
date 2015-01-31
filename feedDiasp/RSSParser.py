#!/usr/bin/env python
# -*- coding: utf-8 -*-
import feedparser
class RSSParser:
	def __init__(self, url):
		self.url = url
	def update(self):
		self.feed = feedparser.parse(self.url)
	def get_entries(self):
		entries=[]
		for entry in self.feed.entries:
			x={}
			x['id'] = entry.id
			x['title'] = entry.title
			x['link'] = entry.link
			if 'content' in entry:
				x['content'] = entry.content[0].value
			else:
				x['content'] = entry.summary
			entries.append(x)
		return entries
