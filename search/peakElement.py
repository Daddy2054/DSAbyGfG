def peakElement(arr,n):
    # Code here
    if n == 1:
        return 0
    for i in range(n):
        if i == 0:
            if arr[i] >= arr[i + 1]:
                return i
        elif i == n - 1:
            if arr[i] >= arr[i - 1]:
                return i
        else:
            if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
                return i
    return -1

print(peakElement([1, 2, 3,5,2,1], 6))