#!/usr/bin/env python
# -*- coding: utf-8 -*-
import facepy
import HTMLParser


class FBParser:
    def __init__(self, user, auth_token):
        self.user = user
        self.auth_token = auth_token
        self.graph = facepy.GraphAPI(self.auth_token)
        self.user_id = self.graph.get(self.user)['id']

    def update(self):
        pass

    def get_entries(self):
        statuses = self.graph.get(self.user + '/posts')['data']
        entries = []
        htmlparser = HTMLParser.HTMLParser()
        for status in statuses:
            # skip, if post on wall
            if status['from']['id'] != self.user_id:
                continue
            post = {}
            post_id = status['id']
            if 'link' in status:
                link = status['link']
            else:
                link = 'https://facebook.com/' + status['id']
            message = status['message'] if 'message' in status else None
            description = status['description'] if 'description' in status else None
            if status['type'] == 'photo':
                # format Photo
                content = self.format_photo(self.graph.get(status['object_id']))
                if message:
                    content += htmlparser.unescape(message)
            elif status['type'] == 'event':
                # format Event
                content = self.format_event(self.graph.get(status['object_id']))
                link = None
            elif status['type'] == 'link':
                # format Link
                content = message if message else ""
                if description:
                    content += "\n---  \n" if message else ""
                    content += description
            else:
                # format Post
                content = htmlparser.unescape(status['message'])

            post['id'] = post_id
            post['title'] = ''
            post['content'] = content
            post['link'] = link
            entries.append(post)
        return reversed(entries)

    def get_access_token(self, app_id, app_secret):
        graph = facepy.GraphAPI()
        result = graph.get(
            'oauth/access_token?client_id=' + app_id + '&client_secret=' + app_secret + '&grant_type=client_credentials')
        access_token = result.replace("access_token=", "")
        return access_token

    def format_photo(self, json):
        url = json['images'][0]['source']
        markup = '![](' + url + ')'
        return markup

    def format_event(self, json):
        venue = json['venue']
        if 'latitude' in venue:
            longitude = str(venue['longitude'])
            latitude = str(venue['latitude'])
        location = json['location']
        start_time = json['start_time']
        name = json['name'].replace("*", "\*")
        owner = json['owner']
        event_id = str(json['id'])
        description = json['description'].replace('\n', '  \n')

        if 'latitude' in locals():
            osm_link = 'http://www.openstreetmap.org/?mlat=' + latitude + '&mlon=' + longitude + '&zoom=17'
        else:
            osm_link = 'www.openstreetmap.org/search?query=' + location

        event = ('### Event: [*' + name + '*](https://facebook.com/' + event_id + ')  \n'
                                                                                  '**Location:** [' + location + '](' + osm_link + ' "search in OpenStreetMaps")  \n'
                                                                                                                                   '**Time:** ' + start_time + '  \n'
                                                                                                                                                               '\n---  \n'
                                                                                                                                                               '' + description + '  \n'
                 )
        return event
