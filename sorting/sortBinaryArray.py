
'''
Sort a binary array using one traversal using partition function of quicksort:
This concept is related to partition of quick sort . In the quick sort partition function, after one scan, the left of the array is the smallest and the right of the array is the largest of the selected pivot element


Follow the given steps to solve the problem:

Create a variable index say j = -1
Traverse the array from start to end
If the element is 0 then swap the current element with the element at the index( jth ) position and increment the index j by 1.
If the element is 1 keep the element as it is.
Below is the implementation of the above approach:
'''
# A Python program to sort a
# binary array


def sortBinaryArray(a, n):
    j = -1
    for i in range(n):

        # if number is smaller
        # than 1 then swap it
        # with j-th number
        if a[i] < 1:
            j = j + 1

            # swap
            a[i], a[j] = a[j], a[i]


# Driver code
if __name__ == "__main__":
    a = [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1,
         1, 1, 0, 0, 1, 1, 0, 1, 0, 0]
    n = len(a)

    # Function call
    sortBinaryArray(a, n)

    for i in range(n):
        print(a[i], end=" ")

# This code is contributed by Shrikant13.
