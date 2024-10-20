'''
Count 1's in a sorted binary array using binary search iteratively:

Follow the steps below for the implementation:

Do while low <= high
Calculate the middle index say mid
Check if arr[mid] is less than 1 then move the high to left side (i.e, hight = mid - 1)
If the element is not last 1 then move the low to the right side (i.e, low = mid + 1)
Check if the element at the middle index is last 1 then return mid + 1
Otherwise move to low to right (i.e, low = mid + 1)
'''

'''package whatever #do not write package name here '''


def countOnes(arr, n):
        low = 0
        high = n - 1
        while (low <= high):  # get the middle index
            mid = (low + high) // 2

            # check if the element at middle index is last 1
            if ((mid == n - 1 or arr[mid + 1] == 0) and arr[mid] == 1):
                return mid + 1

            # check for 1 on left side
            if (arr[mid] == 0):
                high = mid - 1

            # check for 1 on right side
            elif(arr[mid] == 1):
                low = mid + 1

        return 0


# Driver code
if __name__ == '__main__':

    arr = [1, 1, 1, 1, 0, 0, 0]
    n = len(arr)

    print("Count of 1's in given array is ", countOnes(arr, n))
