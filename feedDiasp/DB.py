import minidb

class Store:
	def __init__(self):
		self.db = minidb.Store('db.sqlit3')
	def save(self, obj):
		self.db.save(obj)
		self.db.commit()
	def load(self, obj):
		return self.db.load(obj)
class Feed(object):
	__slots__ = {'feed': str, 'username': str, 'password': str, 'pod': str}
	def __init__(self, feed, username, password, pod):
		self.feed=feed
		self.username=username
		self.password=password
		self.pod=pod

