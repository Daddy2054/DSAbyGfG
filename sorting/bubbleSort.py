def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):

        for j in range(n - i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


l = [10, 8, 20, 5]

bubbleSort(l)

print(*l)
