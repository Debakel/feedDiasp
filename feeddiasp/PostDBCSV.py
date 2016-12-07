#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import os


class PostDBCSV:
    # CSV text file-based database for published posts
    def __init__(self, filename):
        self.filename = filename
        self.entries = []
        if os.path.exists(filename):
            self.db = open(filename, "r+")
            self.entries = self.db.readlines()
        else:
            self.db = open(filename, "a+")

    # need to define enter/exit methods to use with 'with' statement
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.db.close()

    def create_entry(self, post_id):
        return str(datetime.today()) + ',' + post_id

    def mark_as_posted(self, post_id):
        entry = self.create_entry(post_id)
        self.entries.append(entry)
        self.db.write(entry + '\n')
        self.db.flush()

    def is_published(self, post_id):
        for entry in self.entries:
            if post_id in entry:
                return True
        return False
