def immediateGreater(arr,x):
    result = []
    arr.sort()
    for i in arr:
        if i > x:
            result.append(i)
    if len(result) == 0:
        return -1
    return result[0]

print(immediateGreater([1, 2, 3,  5, 6,3,2,1, 7, 8, 9, 10], 5))
print(immediateGreater([1, 2, 3, 4, 5], 1))
print(immediateGreater([1, 2, 3, 4, 5], 7))