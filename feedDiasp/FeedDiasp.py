#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
from Diasp import Diasp
from PostDBCSV import PostDBCSV
from RSSParser import RSSParser
from FBParser import FBParser


def isstring(s):
    try:
        return isinstance(s, basestring)
    except NameError:
        return isinstance(s, str)


class FeedDiasp:
    def __init__(self, pod, username, password, db, parser, keywords=None, hashtags=None, append=None):
        # UnicodeEncodeError Workaround
        reload(sys);
        sys.setdefaultencoding("utf8")

        # Feed
        self.feed = parser

        # Diaspora
        self.pod = pod
        self.username = username
        self.password = password
        self.diasp = Diasp(pod=self.pod, username=self.username, password=self.password, provider_name="feedDiasp*")

        self.keywords = keywords if keywords is not None else []
        # self.hashtags = hashtags if hashtags is not None else []
        self.hashtags = hashtags
        self.append = append

        # if the db is a string, use it as a filename for CSV-based db
        if isstring(db):
            self.db = PostDBCSV(filename=db)
        else:  # otherwise use the DB supplied
            self.db = db

        self.logged_in = False

    def find_hashtags(self, content, keywords):
        hashtags = []
        for keyword in keywords:
            if keyword in content:
                hashtags.append(keyword)
        return hashtags

    def publish(self):
        if not self.diasp.logged_in:
            self.diasp.login()
        self.feed.update()
        posts = self.feed.get_entries
        for post in posts:
            if not self.db.is_published(post['id']):
                print 'Published: ' + post['title']
                hashtags = self.find_hashtags(post['content'], self.keywords)
                if self.hashtags is not None:
                    hashtags.extend(self.hashtags)
                try:
                    self.diasp.post(text=post['content'], title=post['title'], hashtags=hashtags, source=post['link'],
                                    append=self.append)
                    self.db.mark_as_posted(post['id'])
                except Exception as e:
                    print 'Failed to publish: ' + str(e)
