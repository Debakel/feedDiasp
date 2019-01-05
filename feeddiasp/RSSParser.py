#!/usr/bin/env python3

import feedparser
from html2text import html2text
import os
import pypandoc


class RSSParser:
    def __init__(self, url):
        self.url = url
        self.feed = None

    def update(self):
        self.feed = feedparser.parse(self.url)

    def get_entries(self):
        entries = []
        for entry in self.feed.entries:
            new_post = {}
            if 'id' in entry:
                new_post['id'] = entry.id
            elif 'link' in entry:
                new_post['id'] = entry.link
            else:
                # skip entry
                continue
            new_post['title'] = entry.title if 'title' in entry else ''
            new_post['link'] = entry.link if 'link' in entry else ''
            if 'content' in entry:
                new_post['content'] = html2markdown(entry.content[0].value)
            elif 'summary' in entry:
                new_post['content'] = html2markdown(entry.summary)
            elif 'description' in entry:
                new_post['content'] = html2markdown(entry.description)
            else:
                new_post['content'] = ''
            # tags
            tags = []
            if 'tags' in entry:
                for tag in entry['tags']:
                    if 'term' in tag:
                        tags.append(tag['term'])
            # append tags at the end of the content
            new_post['tags'] = tags
            entries.append(new_post)
        entries.reverse()
        return entries


def html2markdown(html: str):
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
