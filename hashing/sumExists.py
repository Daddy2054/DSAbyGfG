#Function to check if there is a pair with the given sum in the array.
def sumExists(arr, N, sum):
    # Create an empty set
    s = set()

    # Traverse the array
    for i in range(N):
        # Calculate the complement of the current element
        complement = sum - arr[i]

        # If the complement exists in the set, return True
        if complement in s:
            return 1

        # Add the current element to the set
        s.add(arr[i])

    # If no pair is found, return False
    return 0


print(sumExists([1, 2, 3, 4, 5], 5, 9))  # Output: 1
print(sumExists([1, 2, 3, 4, 5], 5, 10))  # Output: 0