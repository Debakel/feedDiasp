#!/usr/bin/env python
# -*- coding: utf-8 -*-
import feedparser


class RSSParser:
    def __init__(self, url):
        self.url = url

    def update(self):
        self.feed = feedparser.parse(self.url)

    def get_entries(self):
        entries = []
        for entry in self.feed.entries:
            x = {}
            if 'id' in entry:
                x['id'] = entry.id
            elif 'link' in entry:
                x['id'] = entry.link
            else:
                # skip entry
                continue
            x['title'] = entry.title if 'title' in entry else ''
            x['link'] = entry.link if 'link' in entry else ''
            if 'content' in entry:
                x['content'] = entry.content[0].value
            elif 'summary' in entry:
                x['content'] = entry.summary
            elif 'description' in entry:
                x['content'] = entry.description
            else:
                x['content'] = ''
            entries.append(x)
        return reversed(entries)
