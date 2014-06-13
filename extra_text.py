def word_ladder(w1, w2):
	count = 0
	for i in range(len(w1)):
		if w1[i] != w2[i]:
			count = count + 1
	return count == 1
# function will return true if words differ at i

'''
name = raw_input("What is your name, friend?")
print "Hello", name

start = raw_input("Would you like to play? Enter yes or no.")
if start == "yes":
	print "Okay, let's get started."
else:
	print "I promise the word ladder will be fun!"

print "Welcome to the CS106B word ladder."
print "If you give me two English words, I will transform the first into the second."

method = raw_input("Do you want to know how I will do that?")
if method == "yes":
	print "Cool! I will change one letter at a time."
else:
	print "C'mon!"

w1 = raw_input(Please enter a valid English word.)
w2 = raw_input(Please enter a second word of the same length.)

if len(w1) == len(w2):
	print "Perfect! Let's proceed."
else:
	print "Please enter two English words of the same length."
'''

print word_ladder("code", "data", my_dict)