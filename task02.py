# Build a start list and an end list
def build(numbers):
	a = []
	b = []

	length = len(numbers)

	a.append(numbers[0])
	for i in range(1,length):
		if numbers[i] - numbers[i-1] > 1:
			a.append(numbers[i])
			b.append(numbers[i-1])
	b.append(numbers[length-1])
	
	return a, b

# Input data into list
def input():
	numbers = []
	
	print('Enter integer numbers:')
	while True:
		str = raw_input()
		if not str:
			break
		numbers.append(int(str))
	
	numbers.sort()
	return numbers

# Format and display data	
def display(a, b):

	zipped = zip(a, b)

	for i in zipped:
		(start, end) = i
		print("[" + str(start) + ", " + str(end) + "]" + " with consecutive count of " + str(end-start+1))

# Main code
numbers = input()
a, b = build(numbers)
display(a, b)