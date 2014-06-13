f = open("dictionary.txt", "r")

# read f and convert its contents into an array

my_dict = []
for line in f.readlines():
	my_dict.append(line.strip())

f.close()

print my_dict