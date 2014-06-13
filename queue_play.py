import Queue

q = Queue.Queue()

for i in range(5):
	q.put(i)

while not q.empty():
	print q.get()

class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

class A(object):
	def __init__(self):
		self.x = 'Hello'

	def method_a(self, foo):
		print self.x + '' + foo


