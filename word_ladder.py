import sys

class Queue(object):
	def __init__(self):
		self.items = []
	def contents(self):
		return self.items
	def enqueue(self, element):
		self.items.append(element)
	def dequeue(self):
		if len(self.items) == 0:
			return None
			# print "The queue is empty."
		else:
			popping = self.items[0]
			self.items = self.items[1:]			
			return popping
	def empty(self):
		return len(self.items) == 0

class Stack(object):
	def __init__(self):
		self.items = []
	def contents(self):
		return self.items
	def push(self,element):
		self.items.append(element)
	def pop(self):
		if len(self.items) == 0:
			return None
		else:
			popping = self.items[-1]
			self.items = self.items[:-1]
			return popping
	def peek(self):
		if len(self.items) == 0:
			return None
		else:
			return self.items[-1]
	def copy(self):
		s_copy = Stack()
		s_copy.items = self.items[:] # make a deep copy
		return s_copy

def word_ladder(w1, w2, dictionary):
	my_q = Queue()
	# create a stack, add w1 to the stack
	# add the stack to the queue
	my_s = Stack()
	my_s.push(w1)

	my_q.enqueue(my_s)

	encountered = [w1]
	alphabet = "abcdefghijklmnopqrstuvwxyz"

	while not my_q.empty():
		my_s = my_q.dequeue()
		cur_word = my_s.peek()
		if cur_word == w2:
			return my_s.items
		else:
			tmp_list = list(cur_word)
			for pos in xrange(len(cur_word)):
				neighbor_word = cur_word
				for letter in alphabet:
					# neighbor_word[pos] = letter

					# strings are immutable, so we need a hacky way of
					# replacing a single character
					tmp_list = list(neighbor_word)
					tmp_list[pos] = letter
					neighbor_word = ''.join(tmp_list)

					if neighbor_word in dictionary:
						if neighbor_word not in encountered:

							print neighbor_word

							encountered.append(neighbor_word)

							new_stack = my_s.copy()
							new_stack.push(neighbor_word)
							my_q.enqueue(new_stack)


# read f and convert its contents into an array
f = open("dictionary.txt", "r")
my_dict = []
for line in f.readlines():
	my_dict.append(line.strip())
f.close()

script, w1, w2 = sys.argv

print word_ladder(w1, w2, my_dict)