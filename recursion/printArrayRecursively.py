def printArrayRecursively(arr,n):
    if n == 0:
        return
    printArrayRecursively(arr,n-1)
    print(arr[n-1])

    # Driver program


arr = [1, 2, 3, 4, 5]
n = len(arr)
printArrayRecursively(arr, n)