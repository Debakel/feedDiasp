#!/usr/bin/env python
# -*- coding: utf-8 -*-
import feedparser
class RSSParser:
	def __init__(self, url):
		self.url = url
	def parse(self):
		self.feed = feedparser.parse(self.url)
	def get_posts(self):
		return self.feed.entries
