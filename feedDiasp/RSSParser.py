#!/usr/bin/env python
# -*- coding: utf-8 -*-
import feedparser
from html2text import html2text
import os
import pypandoc
class RSSParser:
    def __init__(self, url):
        self.url = url

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
                new_post['content'] = html2markup(entry.content[0].value)  # html2markup() converts HTML to Markup
            elif 'summary' in entry:
                new_post['content'] = html2markup(entry.summary)
            elif 'description' in entry:
                new_post['content'] = html2markup(entry.description)
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


def html2markup(text):
    try:
        output = pypandoc.convert(text, 'md', format='html')
    except OSError:
        # Pandoc not installed. Switching to html2text instead
        print "Warning: Pandoc not installed. Pandoc is needed to convert HTML-Posts into Markdown. Try sudo apt-get install pandoc."
        output = html2text(text)
    return output
