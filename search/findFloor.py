def findFloor(arr, n, x):
        low = 0
        high = n - 1
        floor = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] <= x:
                floor =mid
                #floor = arr[mid]
                low = mid + 1
            else:
                high = mid - 1

        return floor

print(findFloor([1, 2, 8, 10 ,11, 12, 19], 6, 5))  # Output: 4        