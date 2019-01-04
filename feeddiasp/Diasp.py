#!/usr/bin/env python3
import diaspy


class Diasp:
    def __init__(self, pod=None, username=None, password=None, provider_name=''):
        """Default constructor
        :param pod: Diaspora* pod
        :param username: login / username
        :param password: uhm ... the password
        :param provider_name: usually feedDiasp*
        """
        self.connection = None
        self.stream = None

        self.pod = pod
        self.username = username
        self.password = password
        self.logged_in = False
        self.provider_name = provider_name

    def login(self):
        """Initialize the connection to the Diaspora* pod """
        print('Login as ' + self.username + ' to ' + self.pod)
        try:
            self.connection = diaspy.connection.Connection(pod=self.pod, username=self.username, password=self.password)
            if self.connection is None:
                print('Cannot connect to ' + self.pod)
                return False
            self.connection.login()
            self.stream = diaspy.streams.Stream(self.connection)
            self.logged_in = True
            return True
        except Exception as e:
            print('Failed to login: ' + str(e))
            raise LoginException(str(e))

    def post(self, text, title=None, hashtags=None, source=None, append=None):
        """
        Post given message to Diaspora*
        :param title: the post title (default is None)
        :param text: the message to post
        :param hashtags: hashtags list (default is None)
        :param source: the source of information at the origin of the post (default is None)
        :param append: text to be added at the end (default is None)
        """
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
