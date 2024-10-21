#Given an array arr[], find the position of the first repeating element. 
# The element should occur more than once and the index 
# of its first occurrence should be the smallest.
def firstRepeated(arr):
        d = {}
        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]] += 1
            else:
                d[arr[i]] = 1
        for key in list(d.keys()):
            if d[key] < 2:
                del d[key]
        for i in range(len(arr)):
            if arr[i] in d:
                return i+1
        return -1


print(firstRepeated([1, 5, 3, 4, 3, 5, 6]))
print(firstRepeated([1, 2, 3, 4, 5]))
print(firstRepeated([5, 10, 5, 4, 10]))