def greaterThanX(arr, x):
    count = 0
    for i in range(len(arr)):
        if arr[i] > x:
            count += 1
    return count

print(greaterThanX([1,2,3,4,5,6,7,8,9,10], 5))