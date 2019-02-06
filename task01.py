# Aggregate data by key OR by value
def aggregate(a, b):
	aa = []
	bb = []
	length = len(a)

	for i in range(length):
		if a[i] in aa:
			indx = aa.index(a[i])
			bb[indx] = bb[indx] + b[i]
		else:
			aa.append(a[i])
			bb.append(b[i])
			
	return aa, bb

# Input data into lists
def input():
	key = []
	val = []
	
	print('Enter key value pairs:')
	while True:
		str = raw_input()
		if not str:
			break
		l = str.split()
		key.append(l[0])
		val.append(int(l[1]))
	
	return key, val

# Take the second element of a pair
def takeSecond(elem):
	return elem[1]

# Format and display the result	
def display(a, b):

	zipped = zip(a, b)
	zipped.sort(key=takeSecond, reverse=True)

	for i in zipped:
		(key, val) = i
		key_list = list(key)
		key_list.sort()
		print(', '.join(key_list) + ": " + str(val))

# Main code		
key_1, val_1 = input()
key_2, val_2 = aggregate(key_1, val_1)
val_3, key_3 = aggregate(val_2, key_2)
display(key_3, val_3)