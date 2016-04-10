#!/usr/bin/env python
# -*- coding: utf-8 -*-
import diaspy


class Diasp:
    def __init__(self, pod=None, username=None, password=None, provider_name=''):
        self.pod = pod
        self.username = username
        self.password = password
        self.logged_in = False
        self.provider_name = provider_name

    def login(self):
        print 'Login as ' + self.username + ' to ' + self.pod
        try:
            self.connection = diaspy.connection.Connection(pod=self.pod, username=self.username, password=self.password)
            self.connection.login()
            self.stream = diaspy.streams.Stream(self.connection, fetch=False)
            self.logged_in = True
            return True
        except Exception as e:
            print 'Failed to login: ' + str(e)
            raise LoginException(str(e))

    def post(self, text, title=None, hashtags=None, source=None, append=None):
        if not self.logged_in:
            self.login()
        if title is not None and len(title) > 0:
            text = '### ' + title + '\n\n' + text
        if source is not None:
            text += '\n\n' + source
        if hashtags is not None and len(hashtags) > 0:
            text += '  \n'
            for hashtag in hashtags:
                text += '#' + hashtag + ' '
        if append is not None:
            text += '  \n' + append
        self.stream.post(text, provider_display_name=self.provider_name)


class LoginException(Exception):
    pass
