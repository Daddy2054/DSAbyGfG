# Python3 program for linear search
#Given an array, arr of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.
# 
def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


# Driver code
arr = [1, 2, 3, 4, 5,7,9]
search_element = 5

# Function call
print(search(arr, search_element))