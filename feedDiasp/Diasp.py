#!/usr/bin/env python
# -*- coding: utf-8 -*-
import diaspy
class Diasp:
  def __init__(self, pod=None, username=None, password=None, provider_name=''):
    self.pod  = pod
    self.username = username
    self.password = password
    self.logged_in = False
    self.provider_name = provider_name
  def login(self):
    print 'Login as '+self.username+' to '+self.pod   
    try:
      self.c = diaspy.connection.Connection(pod=self.pod, username=self.username, password=self.password)
      self.c.login()  
      self.stream = diaspy.streams.Stream(self.c)
      self.logged_in = True
    except Exception as e:
      print 'Failed to login: ' + str(e)
      raise LoginException(str(e))
  def post(self, text, title=None, hashtags=None, source=None, append=None):
    if not self.logged_in:
      self.login()
    # Title is a href to source
    if (title and len(title) > 0) and (source and len(source) > 0):
      post = '### ' + '[' + title + '](' + source + ')' + '\n'
    # normal title
    elif title and len(title) > 0:
      post = '### ' + title + '\n'
    # just source
    elif source and len(source) > 0:
      post = '### ' + source + '\n\n'
    post += text
    if hashtags and len(hashtags) > 0:
      post += '  \n'
      for hashtag in hashtags:
        post += '#' + hashtag + ' ' 
    if append:
      post += '  \n' + append
    self.stream.post(post, provider_display_name=self.provider_name)

class LoginException(Exception):
  pass
