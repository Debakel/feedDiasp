#!/usr/bin/env python
# -*- coding: utf-8 -*-
from FeedDiasp import FeedDiasp
from DB import Store, Feed

db=Store()
for feed in db.load(Feed):
	print feed.username
	bot = FeedDiasp(feed_url=feed.feed, pod=feed.pod, username=feed.username, password=feed.password, db='posts.db', keywords=keywords)
	bot.publish()


