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
		statuses = self.graph.get(self.user+'/posts')['data']
		entries=[]
		htmlparser = HTMLParser.HTMLParser()
		for status in statuses:
			# skip, if post on wall
			if status['from']['id'] != self.user_id:
				continue
				
			post={}
			post['id'] = status['id']
			if 'link' in status:
				post['link'] = status['link']
			post['title']=''
			if status['type'] == 'photo':
				# format Photo
				post['content'] = self.format_photo(self.graph.get(status['object_id']))
				post['content'] += htmlparser.unescape(status['message'])
			elif status['type'] == 'event':
				# format Event
				print "ID: " + status['object_id']
				post['content'] = self.format_event(self.graph.get(status['object_id']))
				post['link'] = 'https://facebook.com/' + status['id']
			else:
				# format Post
				post['content'] = htmlparser.unescape(status['message'])

			entries.append(post)
		return reversed(entries)
	def get_access_token(self, app_id, app_secret):
		graph = facepy.GraphAPI()
		result = graph.get('oauth/access_token?client_id=' + app_id +'&client_secret='+app_secret+'&grant_type=client_credentials')
		access_token = result.replace("access_token=","")
		print access_token
		return access_token
		
	def format_photo(self, json):
		url = json['images'][0]['source']
		markup =  '![]('+url+')'
		return markup
	def format_event(self, json):
		print "JSON: " + str(json)
		
		venue = json['venue']
		if 'latitude' in venue:
			longitude=str(venue['longitude'])
			latitude=str(venue['latitude'])
		location=json['location']
		start_time=json['start_time']
		name=json['name'].replace("*","\*")
		owner=json['owner']
		event_id=str(json['id'])
		description=json['description'].replace('\n', '  \n')

		if 'latitude' in locals():
			osm_link = 'http://www.openstreetmap.org/?mlat=' + latitude + '&mlon=' + longitude + '&zoom=17'
		else:
			osm_link = 'www.openstreetmap.org/search?query=' + location
			
		event = ('### Event: [*' + name + '*](https://facebook.com/' + event_id +')  \n'
				'**Location:** [' + location + '](' + osm_link + ' "search in OpenStreetMaps")  \n'
				'**Time:** ' + start_time+'  \n'
				'\n---  \n'
				''+description+'  \n'
				)
		return event
