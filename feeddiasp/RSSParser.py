#!/usr/bin/env python3
from typing import List

import feedparser
import pypandoc
from html2text import html2text

from feeddiasp.dataclasses import Post


class RSSParser:
    def __init__(self, url):
        self.url = url
        self.feed = None

    def update(self):
        self.feed = feedparser.parse(self.url)
        if self.feed.bozo == 1:
            # Feed is malformed
            # See https://pythonhosted.org/feedparser/bozo.html
            raise self.feed.bozo_exception

    def get_entries(self) -> List[Post]:
        """ Return the feed entries as a list of diaspora post instances.
        """
        entries = []
        for entry in self.feed.entries:
            if not ('id' in entry or 'link' in entry):
                # Skip entry, since it has no unique identifier
                continue

            post = Post(
                id=entry.id if 'id' in entry else entry.link,
                title=getattr(entry, 'title', ''),
                link=getattr(entry, 'link', ''),
                content=self._extract_content(entry),
                tags=self._extract_tags(entry)
            )
            entries.append(post)

        entries.reverse()
        return entries

    def _extract_content(self, entry) -> str:
        """ Extract the content of an rss entry and return it as Markdown-structured text.
        """
        if 'content' in entry:
            content = entry.content[0].value
        elif 'summary' in entry:
            content = entry.summary
        elif 'description' in entry:
            content = entry.description
        else:
            return ''

        return html2markdown(content)

    def _extract_tags(self, entry) -> List[str]:
        """ Extract and return the tags of the given rss entry.
        """
        tags = []
        if 'tags' in entry:
            for tag in entry['tags']:
                if 'term' in tag:
                    tags.append(tag['term'])
        return tags


def html2markdown(html: str) -> str:
    """
    Returns the given HTML as equivalent Markdown-structured text.
    """
    try:
        return pypandoc.convert_text(html, 'md', format='html')
    except OSError:
        msg = "It's recommended to install the `pandoc` library for converting " \
              "HTML into Markdown-structured text. It tends to have better results" \
              "than `html2text`, which is now used as a fallback."
        print(msg)
        return html2text(html)
