import os
from unittest import TestCase

from feeddiasp import Diasp, RSSParser

RSS_FEED_URL = "http://www.spiegel.de/schlagzeilen/tops/index.rss"


class DiaspClientTestCase(TestCase):
    def setUp(self):
        self.pod = os.environ['FEEDDIASP_TEST_POD']
        self.username = os.environ['FEEDDIASP_TEST_USERNAME']
        self.password = os.environ['FEEDDIASP_TEST_PASSWORD']

    def test_login(self):
        client = Diasp(
            pod=self.pod,
            username=self.username,
            password=self.password)

        try:
            client.login()
        except Exception as e:
            self.fail(e)


class RSSParserTestCase(TestCase):
    def test_get_posts(self):
        rss = RSSParser(url=RSS_FEED_URL)
        rss.update()
        posts = rss.get_entries()

        self.assertTrue(len(posts) > 0)
