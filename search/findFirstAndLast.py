# A Naive Approach:

# The idea to solve this problem is iterate on the elements of given array and check given elements in an array and keep track of first and last occurrence of the found element’s index.

# Python 3 program to find first and
# last occurrence of an elements in
# given sorted array


# Function for finding first and last
# occurrence of an elements
def findFirstAndLast(arr, n, x):
	first = -1
	last = -1
	for i in range(0, n):
		if (x != arr[i]):
			continue
		if (first == -1):
			first = i
		last = i

	if (first != -1):
		print("First Occurrence = ", first,
			" \nLast Occurrence = ", last)
	else:
		print("Not Found")


# Driver code
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
x = 8
findFirstAndLast(arr, n, x)
